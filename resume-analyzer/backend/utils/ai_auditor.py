import os
import json
import google.generativeai as genai
from typing import List, Dict

# Get API Key from Environment Variable (Render Setup)
# Get your key here: https://aistudio.google.com/
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

def generate_ai_suggestions(missing_skills: List[str], job_context: str = "") -> List[Dict]:
    """
    Generate high-quality course suggestions and learning paths using Gemini.
    """
    if not GOOGLE_API_KEY:
        return [] # Fallback to static if key not provided
        
    prompt = f"""
    You are an Elite Career Auditor. I have found the following 'Neural Discrepancies' (missing skills) 
    in a candidate's resume for a role with this context: "{job_context[:300]}".
    
    FOR EACH MISSING SKILL:
    1. Identify the BEST high-quality, reputable, and specific course (Coursera, edX, Udemy, or official documentation).
    2. Provide a DIRECT URL to that course.
    3. Write a short, authoritative 'Actionable Protocol' (learning path).
    
    Skills to analyze: {", ".join(missing_skills)}
    
    RETURN ONLY A JSON ARRAY like this:
    [
      {{
        "skill": "skill_name",
        "resources": ["Step 1", "Step 2"],
        "course_url": "https://example.com/course",
        "priority": "high/medium/low"
      }}
    ]
    """
    
    try:
        response = model.generate_content(prompt)
        # Handle cases where Gemini might return markdown blocks
        clean_json = response.text.strip().replace("```json", "").replace("```", "")
        return json.loads(clean_json)
    except Exception as e:
        print(f"Gemini Error: {e}")
        return []

def get_static_suggestions(missing_skills: List[str]) -> List[Dict]:
    # (Keeping our highly curated dictionary as a fallback)
    from backend.utils.suggestions_dict import SKILL_SUGGESTIONS, DEFAULT_SUGGESTION
    
    suggestions = []
    for skill in missing_skills:
        skill_lower = skill.lower()
        info = SKILL_SUGGESTIONS.get(skill_lower, DEFAULT_SUGGESTION)
        suggestions.append({
            "skill": skill,
            "resources": info.get("resources", []),
            "course_url": info.get("course_url") if "course_url" in info else f"https://www.google.com/search?q=learn+{skill.replace(' ', '+')}",
            "priority": _get_priority(skill_lower)
        })
    return suggestions

def _get_priority(skill: str) -> str:
    high = ["python", "javascript", "java", "aws", "docker", "kubernetes", "ml", "sql", "git"]
    if skill in high: return "high"
    return "medium"
