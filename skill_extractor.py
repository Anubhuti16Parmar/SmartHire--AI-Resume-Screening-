#Find skills in text using a keyword dictionary.
import re
TECH_SKILLS = [
    "python", "java", "c++", "javascript", "typescript", "sql", "mysql", "postgresql", "django",
    "html", "css", "react", "node.js", "mongodb", "flask", "fastapi", "streamlit", "pandas", "numpy",
    "scikit-learn", "tensorflow", "pytorch", "keras", "ML", "deep learning", "nlp",
    "data analysis", "data visualization", "power bi", "tableau", "excel", "git", "github", "docker", 
    "azure", "linux", "rest api", "matplotlib", "plotly", "statistics", "hadoop",
]
SOFT_SKILLS = [
    "communication", "teamwork", "leadership", "problem solving", "time management", "critical thinking",
    "creativity", "collaborationn", "presentation",
]

ALL_SKILLS = TECH_SKILLS + SOFT_SKILLS

def _has(skill, text):
    return re.search(r"(?<![\w])" + re.escape(skill) + r"(?![\w])", text) is not None


def extract_skills(text, skill_list=ALL_SKILLS):
    t = text.lower()
    return sorted({s for s in skill_list if _has(s, t)})

def split_skills(skills):
    tech = [s for s in skills if s in TECH_SKILLS]
    soft = [s for s in skills if s in SOFT_SKILLS]
    return tech,soft