from typing import List, Dict, Tuple
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load once at module level (cached after first load)
_model = None


def get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def get_embeddings(texts: List[str]) -> np.ndarray:
    model = get_model()
    return model.encode(texts, convert_to_numpy=True)


def compute_skill_similarity(resume_skills: List[str], job_skills: List[str]) -> Dict:
    if not resume_skills or not job_skills:
        return {
            "matched_skills": [],
            "missing_skills": job_skills,
            "similarity_scores": {},
            "raw_score": 0.0
        }

    resume_embeddings = get_embeddings(resume_skills)
    job_embeddings = get_embeddings(job_skills)

    # Cosine similarity matrix: (num_job_skills x num_resume_skills)
    sim_matrix = cosine_similarity(job_embeddings, resume_embeddings)

    matched_skills = []
    missing_skills = []
    similarity_scores = {}
    MATCH_THRESHOLD = 0.72

    for i, job_skill in enumerate(job_skills):
        best_score = float(np.max(sim_matrix[i]))
        best_match_idx = int(np.argmax(sim_matrix[i]))
        best_resume_skill = resume_skills[best_match_idx]

        similarity_scores[job_skill] = round(best_score, 4)

        if best_score >= MATCH_THRESHOLD:
            matched_skills.append({
                "job_skill": job_skill,
                "resume_skill": best_resume_skill,
                "score": round(best_score, 4)
            })
        else:
            missing_skills.append(job_skill)

    raw_score = len(matched_skills) / len(job_skills) if job_skills else 0.0

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "similarity_scores": similarity_scores,
        "raw_score": raw_score
    }


def compute_text_similarity(resume_text: str, job_text: str) -> float:
    embeddings = get_embeddings([resume_text[:512], job_text[:512]])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(float(score), 4)
