from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import os

from utils.pdf_extractor import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.matcher import compute_skill_similarity, compute_text_similarity
from utils.scorer import calculate_weighted_score, get_score_label
from utils.suggestions import generate_suggestions

app = FastAPI(
    title="Resume Analyzer & Job Matcher",
    description="AI-powered resume analysis using Hugging Face Transformers",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend static files
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")


@app.get("/")
async def root():
    index_path = os.path.join(frontend_path, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Resume Analyzer API is running. POST to /analyze"}


@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(..., description="PDF resume file"),
    job_description: str = Form(..., description="Job description text")
):
    # Validate file type
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    if not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

    # Step 1: Extract text from PDF
    file_bytes = await resume.read()
    if len(file_bytes) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    resume_text = extract_text_from_pdf(file_bytes)
    if not resume_text.strip():
        raise HTTPException(status_code=422, detail="Could not extract text from PDF. Ensure it is not scanned/image-based.")

    # Step 2: Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    if not job_skills:
        raise HTTPException(
            status_code=422,
            detail="No recognizable skills found in the job description. Please provide a more detailed description."
        )

    # Step 3: Semantic skill matching
    match_result = compute_skill_similarity(resume_skills, job_skills)

    # Step 4: Overall text similarity
    text_sim = compute_text_similarity(resume_text, job_description)

    # Step 5: Weighted score
    score_data = calculate_weighted_score(
        match_result["matched_skills"],
        match_result["missing_skills"],
        text_sim
    )

    # Step 6: Suggestions
    suggestions = generate_suggestions(match_result["missing_skills"])

    return {
        "status": "success",
        "candidate": {
            "resume_skills": resume_skills,
            "total_skills_found": len(resume_skills)
        },
        "job": {
            "required_skills": job_skills,
            "total_skills_required": len(job_skills)
        },
        "match": {
            "score": score_data["final_score"],
            "label": get_score_label(score_data["final_score"]),
            "skill_score": score_data["skill_score"],
            "text_similarity_score": score_data["text_score"],
            "breakdown": score_data["breakdown"],
            "matched_skills": match_result["matched_skills"],
            "missing_skills": match_result["missing_skills"]
        },
        "suggestions": suggestions
    }


@app.get("/health")
async def health():
    return {"status": "healthy", "model": "all-MiniLM-L6-v2"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
