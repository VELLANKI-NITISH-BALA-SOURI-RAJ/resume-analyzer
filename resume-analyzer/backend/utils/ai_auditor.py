import os
import json
import google.generativeai as genai
from typing import List, Dict

def generate_ai_suggestions(missing_skills: List[str], job_context: str = "") -> List[Dict]:
    """
    Generate high-quality course suggestions and learning paths using Gemini.
    Specifically pulls NEW courses for any skill not in the predefined list.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("// NEURAL AUDIT ERROR: GEMINI API KEY NOT DETECTED IN ENVIRONMENT.")
        return []
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    You are an Elite Career Technical Auditor. Analyze these missing skills for a role with context: "{job_context[:300]}".
    
    FOR THE FOLLOWING SKILLS: {", ".join(missing_skills)}
    
    1. Find the BEST reputable course (Coursera, Udemy, edX, or Official Docs).
    2. Provide a REAL direct URL to that specific course.
    3. Provide a 2-step 'Actionable Learning Protocol'.
    
    RETURN ONLY JSON (No markdown blocks, no text):
    [
      {{
        "skill": "skill_name",
        "resources": ["Step 1", "Step 2"],
        "course_url": "https://direct-course-link.com",
        "priority": "high"
      }}
    ]
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # Clean specific markdown wrappers
        if "```" in text:
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        
        results = json.loads(text.strip())
        if not results:
            print("// NEURAL AUDIT: GEMINI RETURNED EMPTY RESULTS.")
        return results
    except Exception as e:
        print(f"// NEURAL AUDIT [GEMINI] FAILED. ERROR: {e}")
        # Log the raw text for debugging if it failed during parsing
        try: print(f"// RAW GEMINI OUTPUT: {response.text[:200]}...")
        except: pass
        return []

def get_static_suggestions(missing_skills: List[str]) -> List[Dict]:
    """
    Static fallback for basic skills.
    """
    # Import locally to avoid circular deps
    from backend.utils.suggestions_dict import SKILL_SUGGESTIONS, DEFAULT_SUGGESTION
    
    suggestions = []
    for skill in missing_skills:
        skill_lower = skill.lower()
        info = SKILL_SUGGESTIONS.get(skill_lower, DEFAULT_SUGGESTION)
        suggestions.append({
            "skill": skill,
            "resources": info.get("resources", []),
            "course_url": info.get("course_url") if "course_url" in info else f"https://www.google.com/search?q=best+course+to+learn+{skill.replace(' ', '+')}",
            "priority": "high"
        })
    return suggestions
