from typing import List, Dict
from backend.utils.skill_extractor import get_skill_category

# Category weights — higher = more important for scoring
CATEGORY_WEIGHTS = {
    "programming_languages": 1.5,
    "ml_ai": 1.4,
    "web_backend": 1.3,
    "cloud_devops": 1.3,
    "databases": 1.2,
    "web_frontend": 1.2,
    "data_engineering": 1.2,
    "tools_practices": 1.0,
    "security": 1.1,
    "certifications": 0.8,
    "soft_skills": 0.6,
    "general": 1.0,
}


def calculate_weighted_score(
    matched_skills: List[Dict],
    missing_skills: List[str],
    text_similarity: float
) -> Dict:
    if not matched_skills and not missing_skills:
        return {"final_score": 0, "skill_score": 0, "text_score": 0, "breakdown": {}}

    total_weight = 0.0
    matched_weight = 0.0

    all_job_skills = [m["job_skill"] for m in matched_skills] + missing_skills

    for skill in all_job_skills:
        category = get_skill_category(skill)
        weight = CATEGORY_WEIGHTS.get(category, 1.0)
        total_weight += weight

    for match in matched_skills:
        category = get_skill_category(match["job_skill"])
        weight = CATEGORY_WEIGHTS.get(category, 1.0)
        # Scale by semantic similarity score (partial credit)
        matched_weight += weight * match["score"]

    skill_score = (matched_weight / total_weight) * 100 if total_weight > 0 else 0.0
    text_score = text_similarity * 100

    # Weighted blend: 75% skill match, 25% overall text similarity
    final_score = (skill_score * 0.75) + (text_score * 0.25)
    final_score = min(round(final_score, 1), 100.0)

    return {
        "final_score": final_score,
        "skill_score": round(skill_score, 1),
        "text_score": round(text_score, 1),
        "breakdown": {
            "total_job_skills": len(all_job_skills),
            "matched_count": len(matched_skills),
            "missing_count": len(missing_skills),
            "weighted_match_ratio": round(matched_weight / total_weight, 4) if total_weight else 0
        }
    }


def get_score_label(score: float) -> str:
    if score >= 85:
        return "Excellent Match"
    elif score >= 70:
        return "Strong Match"
    elif score >= 55:
        return "Good Match"
    elif score >= 40:
        return "Partial Match"
    elif score >= 25:
        return "Weak Match"
    return "Poor Match"
