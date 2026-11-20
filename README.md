# SmartHire – AI Resume Screening & Job Matching

SmartHire automatically analyses PDF resumes, compares them with a job description, and ranks candidates by suitability, so recruiters can shortlist faster.

## Problem Statement
Recruiters spend a lot of time reading hundreds of resumes manually. SmartHire automates the initial screening and gives a ranked, explainable shortlist.

## Features
- Upload multiple PDF resumes at once
- Extracts name, email, phone, education and years of experience
- Identifies technical and soft skills
- Calculates a match score using TF-IDF + cosine similarity and skill overlap
- Shows matched and missing skills for each candidate
- Ranks candidates and applies an adjustable shortlist threshold
- Interactive charts and candidate summaries
- Exports the full report and the shortlist to CSV
- Stores results in an SQLite database

## Tech Stack
| Technology | Purpose |
|---|---|
| Python | Main language |
| Streamlit | Web interface |
| pdfplumber | Text extraction from PDFs |
| Scikit-learn | TF-IDF and cosine similarity |
| Pandas, NumPy | Data processing |
| Plotly, Matplotlib | Visualisation |
| SQLite | Storing candidate data |

## Project Structure
    AI Automation project/
    ├── app.py               # Streamlit dashboard
    ├── resume_parser.py     # PDF text and detail extraction
    ├── skill_extractor.py   # Skill detection
    ├── job_matcher.py       # Scoring and ranking
    ├── requirements.txt
    ├── data/resumes/        # Sample resumes
    └── outputs/             # Generated reports

## How It Works
1. The recruiter pastes a job description and uploads PDF resumes.
2. `resume_parser.py` extracts text and basic details.
3. `skill_extractor.py` finds skills in the resume and in the job description.
4. `job_matcher.py` computes:
   - Text similarity: TF-IDF vectors + cosine similarity
   - Skill match: matched skills / required skills
   - Final score = (w1 × text similarity) + (w2 × skill match), with weights adjustable in the app
5. Candidates are ranked and shown on the dashboard, and the report can be downloaded as CSV.

## Installation
    pip install -r requirements.txt

## Run
    streamlit run app.py

Then open http://localhost:8501 in your browser.

## Screenshots
![Dashboard](screenshots/dashboard.png)
![Ranking](screenshots/ranking.png)

## Sample Results
[Add a short table of 3–5 candidates with their scores, or describe how your ranking compared with a manual ranking, e.g. "System ranking matched my manual ranking for 8 of 10 resumes."]

## Limitations
- Works only with text-based PDFs (scanned resumes need OCR)
- Name detection is rule-based and may fail on unusual layouts
- Keyword matching does not understand synonyms (e.g. "ML" vs "machine learning")

## Future Improvements
- LLM-generated candidate summaries (Gemini API)
- spaCy named entity recognition for better extraction
- Semantic matching with sentence embeddings
- OCR support for scanned resumes
- Support for DOCX resumes

## Author
Anubhuti Parmar