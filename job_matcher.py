#TF_IDF cosine similarity + skill overlap.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skill_extractor import extract_skills

def tfidf_scores(job_description, resume_texts):
    docs = [job_description] + list(resume_texts)
    vec =  TfidfVectorizer(stop_words="english", ngram_range=(1,2))
    matrix = vec.fit_transform(docs)
    return cosine_similarity(matrix[0:1], matrix[1:]).flatten()

def match_candidates(job_description, candidates, w_text=0.5, w_skill=0.5):
    """candidates: liist of dicts from parse_resume(). returns the list with scores added."""
    job_skills = extract_skills(job_description)
    sims = tfidf_scores(job_description,[c["text"] for c in candidates])

    for c, sim in zip(candidates,sims):
        c["skills"] = extract_skills(c["text"])
        matched = [s for s in job_skills if s in c["skills"]]
        missing = [s for s in job_skills if s not in c["skills"]]
        skill_score = len(matched) / len(job_skills) if job_skills else 0
        c["text_score"] = round(sim * 100, 1)
        c["skill_score"] = round(skill_score * 100, 1)
        c["match_score"] = round((w_text * sim + w_skill * skill_score) * 100, 1)
        c["matched_skills"] = matched
        c["missing_skills"] = missing
    return sorted(candidates, key=lambda x: x["match_score"], reverse=True)

def make_summary(c):
    """rule based summary"""
    return(f"{c['name']} scores {c['match_score']}% for this role, matching "
           f"{len(c['matched_skills'])} required  skills "
           f"({', '.join(c['matched_skills'][:5]) or 'none'}). "
           f"Missing: {', '.join(c['missing_skills'][:5]) or 'none'}. "
           f"Experience mentioned: {c['experience_years']} year(s).")
        