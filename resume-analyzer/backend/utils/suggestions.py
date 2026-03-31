from typing import List, Dict
from backend.utils.ai_auditor import generate_ai_suggestions, get_static_suggestions

def generate_suggestions(missing_skills: List[str], job_context: str = "") -> List[Dict]:
    """
    Tries AI Audit (Gemini) first, falls back to Curated Static Dictionary.
    """
    if not missing_skills:
        return []
        
    ai_results = generate_ai_suggestions(missing_skills, job_context)
    
    if ai_results:
        print("// NEURAL AUDIT: GEMINI LIVE RESULTS ACTIVE.")
        return ai_results
        
    print("// NEURAL AUDIT: CURATED STATIC DICTIONARY ACTIVE.")
    return get_static_suggestions(missing_skills)
