import os
import json
import google.generativeai as genai
from typing import List, Dict, Optional

# Get API Key from Environment Variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def perform_full_audit(resume_text: str, job_description: str) -> Dict:
    """
    Perform a complete AI-first audit to determine the final match score,
    matched skills, and missing skills with high-quality course links.
    """
    if not GEMINI_API_KEY:
        print("// NEURAL AUDIT ERROR: GEMINI API KEY NOT DETECTED.")
        return {}

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    You are an Elite Technical Recruiter performing a "Dhurandhar" Neural Audit.
    Analyze this Resume against the Job Description. Be strictly objective but recognize synonyms.
    
    RESUME TEXT:
    {resume_text[:4000]}
    
    JOB DESCRIPTION:
    {job_description[:4000]}
    
    TASKS:
    1. Determine a Final Match Score (0-100) based on actual competency and experience depth.
    2. Identify "Optimal Matches": Specifically, what critical skills from the JD are found in the resume.
    3. Identify "Neural Discrepancies": Critical JD skills missing in the resume.
    4. FOR EVERY MISSING SKILL: Provide a DIRECT URL to a high-quality learning course (Coursera, Udemy, or Official Docs).
    5. Provide a 1-sentence "Technical Rationale" for the score.
    
    RETURN ONLY RAW JSON (No markdown blocks, no text):
    {{
      "score": 85,
      "label": "Strong Match",
      "rationale": "High competency in Python/ML but missing deep AWS deployment cloud experience.",
      "matched": ["skill1", "skill2"],
      "missing": [
        {{
          "skill": "skill_name",
          "protocol": "Step 1 | Step 2",
          "course_url": "https://direct-link-to-course.com"
        }}
      ]
    }}
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        if "```" in text:
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        
        audit_data = json.loads(text.strip())
        return audit_data
    except Exception as e:
        print(f"// NEURAL AUDIT [FULL] FAILED. ERROR: {e}")
        return {}

def get_static_fallback(missing_skills: List[str]) -> List[Dict]:
    """
    Static fallback if Gemini fails.
    """
    from backend.utils.suggestions_dict import SKILL_SUGGESTIONS, DEFAULT_SUGGESTION
    suggestions = []
    for skill in missing_skills:
        skill_lower = skill.lower()
        info = SKILL_SUGGESTIONS.get(skill_lower, DEFAULT_SUGGESTION)
        suggestions.append({
            "skill": skill,
            "protocol": " | ".join(info.get("resources", [])),
            "course_url": info.get("course_url") if "course_url" in info else f"https://www.google.com/search?q=best+course+to+learn+{skill.replace(' ', '+')}"
        })
    return suggestions
