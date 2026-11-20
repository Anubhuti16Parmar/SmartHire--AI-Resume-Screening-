"""Extract text and basic info from a PDF resume."""
import re
import pdfplumber

EMAIL_RE = re.compile(r"[\w\.\-+]+@[\w\.\-]+\.\w+")
PHONE_RE = re.compile(r"(\+?\d[\d\s\-]{8,13}\d)")
EDU_WORDS = ["b.tech", "btech", "b.e", "m.tech", "mtech", "bca", "mca", "b.sc", "m.sc", "bsc", "msc", "mba", "bachleor", "master", "phd", "diploma", "university", "colllege"]

def extract_text(file) -> str:
    """ file =  path or file -like object (Streamlit upload). """
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") +"\n"
    return text

def extract_email(text):
    m = EMAIL_RE.search(text)
    return m.group(0) if m else ""

def extract_phone(text):
    m = PHONE_RE.search(text)
    return m.group(0).strip() if m else ""

def extract_name(text, fallback=""):
    """Heuristic: first short alphabetic line near the top."""
    for line in text.splitlines()[:6]:
        line = line.strip()
        words = line.split()
        if 2 <= len(words) <= 4 and all(w.replace(".", "").isalpha() for w in words):
            return line.title()
    return fallback

def extract_education(text):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    found = [l for l in lines if any(w in l.lower() for w in EDU_WORDS)]
    return"; ".join(found[:3])

def extract_experience_years(text):
    nums = [int(n) for n in re.findall(r"(\d{1,2})\+?\s*(?:years?|yrs?)", text.lower())]
    return max(nums) if nums else 0

def parse_resume(file, filename=""):
    text =  extract_text(file)
    return{
        "filename": filename,
        "name": extract_name(text, fallback=filename.rsplit(".", 1)[0]),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "education": extract_education(text),
        "experience_years": extract_experience_years(text),
         "text": text,
    }