import os
import json
import google.generativeai as genai
from typing import List, Dict, Optional

# Get API Key from Environment Variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def perform_full_audit(resume_text: str, job_description: str, bert_results: Dict, bert_score: float) -> Dict:
    """
    Hybrid Neural Audit: Takes local BERT results and uses Gemini to refine 
    the context-aware score and course suggestions.
    """
    if not GEMINI_API_KEY:
        print("// NEURAL AUDIT ERROR: GEMINI API KEY NOT DETECTED.")
        return {}

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    You are a Senior Neural Auditor reviewing a Local Technical Match (BERT).
    
    LOCAL AUDIT DATA (BERT):
    - Raw Compatibility Score: {bert_score}%
    - Detected Matches: {", ".join([m['job_skill'] for m in bert_results['matched_skills']])}
    - Identified Gaps: {", ".join(bert_results['missing_skills'])}
    
    RESUME CONTEXT:
    {resume_text[:3000]}
    
    JOB MANDATE:
    {job_description[:3000]}
    
    TASKS:
    1. Review the BERT Score ({bert_score}%). Refine it into a 'Context Match Score' (0-100).
    2. Analyze 'Identified Gaps'. If the resume actually has experience related to these gaps (synonyms), mark them as 'Partial Matches'.
    3. FOR TRUE MISSING SKILLS: Provide at least 2 high-quality top course recommendations.
    4. DISTINGUISH between 'Free' and 'Paid' courses for each skill.
    5. Provide a 'Reviewer Rationale': Explain WHY you adjusted the score from the BERT base.
    
    RETURN ONLY RAW JSON:
    {{
      "score": 78,
      "label": "Strong Match",
      "rationale": "...",
      "matched": ["skill1", "skill2"],
      "missing": [
        {{
          "skill": "skill_name",
          "protocol": "Brief learning path",
          "top_courses": [
            {{ "name": "Course Name", "url": "https://...", "type": "Free" }},
            {{ "name": "Best Paid Course", "url": "https://...", "type": "Paid" }}
          ]
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
        
        top_courses = []
        if "course_url" in info:
            top_courses.append({
                "name": f"Recommended {skill} Course",
                "url": info["course_url"],
                "type": "Mixed"
            })
        else:
            top_courses.append({
                "name": f"Search {skill} on Google",
                "url": f"https://www.google.com/search?q=best+course+to+learn+{skill.replace(' ', '+')}",
                "type": "Free/Paid"
            })

        suggestions.append({
            "skill": skill,
            "protocol": " | ".join(info.get("resources", [])),
            "top_courses": top_courses
        })
    return suggestions
