# 🤖 AI Resume Analyzer & Job Matcher

An AI-powered platform that analyzes resumes against job descriptions using **Hugging Face Transformers** (BERT-based sentence embeddings) to produce match scores, skill gap analysis, and personalized improvement suggestions.

---

## 🏗 Project Structure

```
resume-analyzer/
├── backend/
│   ├── main.py                  # FastAPI app + /analyze endpoint
│   └── utils/
│       ├── pdf_extractor.py     # PDF → text extraction
│       ├── skill_extractor.py   # NLP skill detection from text
│       ├── matcher.py           # Semantic similarity via sentence-transformers
│       ├── scorer.py            # Weighted 0–100 score calculation
│       └── suggestions.py       # Personalized improvement suggestions
├── frontend/
│   └── index.html               # Full UI (HTML/CSS/JS)
├── requirements.txt
├── render.yaml                  # Render deployment config
├── Procfile                     # Railway deployment config
└── README.md
```

---

## ⚙️ How It Works

```
PDF Upload → Text Extraction (pdfplumber)
         → Skill Extraction (regex + taxonomy)
         → Embeddings (all-MiniLM-L6-v2)
         → Cosine Similarity (sklearn)
         → Weighted Score (0–100)
         → Suggestions (curated knowledge base)
```

### NLP Pipeline
1. **Skill Extraction** — regex-based matching against a 150+ skill taxonomy across 11 categories
2. **Semantic Matching** — `sentence-transformers/all-MiniLM-L6-v2` encodes skills into 384-dim vectors
3. **Cosine Similarity** — each job skill is matched against all resume skills; best score ≥ 0.72 = match
4. **Weighted Scoring** — skills weighted by category importance (ML/AI > soft skills), blended with full-text similarity (75/25 split)

---

## 🚀 Local Setup

### Prerequisites
- Python 3.10+
- pip

### 1. Clone & Install

```bash
git clone <your-repo-url>
cd resume-analyzer
pip install -r requirements.txt
```

> First run downloads the `all-MiniLM-L6-v2` model (~90MB) automatically.

### 2. Start the Backend

```bash
cd backend
uvicorn main:app --reload --port 8000
```

### 3. Open the Frontend

Open `frontend/index.html` directly in your browser, **or** visit:
```
http://localhost:8000
```
(The FastAPI server also serves the frontend at `/`)

---

## 📡 API Reference

### `POST /analyze`

**Content-Type:** `multipart/form-data`

| Field | Type | Description |
|-------|------|-------------|
| `resume` | File (PDF) | Candidate's resume |
| `job_description` | string | Full job description text |

**Response:**
```json
{
  "status": "success",
  "candidate": {
    "resume_skills": ["python", "docker", "aws"],
    "total_skills_found": 3
  },
  "job": {
    "required_skills": ["python", "kubernetes", "aws", "terraform"],
    "total_skills_required": 4
  },
  "match": {
    "score": 72.5,
    "label": "Strong Match",
    "skill_score": 80.0,
    "text_similarity_score": 45.2,
    "breakdown": {
      "total_job_skills": 4,
      "matched_count": 3,
      "missing_count": 1
    },
    "matched_skills": [
      { "job_skill": "python", "resume_skill": "python", "score": 1.0 }
    ],
    "missing_skills": ["terraform"]
  },
  "suggestions": [
    {
      "skill": "terraform",
      "priority": "medium",
      "resources": ["HashiCorp Learn (free)", "Terraform: Up & Running (book)"],
      "certifications": ["HashiCorp Certified Terraform Associate"],
      "tools": ["Terraform Cloud", "Terragrunt"]
    }
  ]
}
```

### `GET /health`
Returns `{ "status": "healthy", "model": "all-MiniLM-L6-v2" }`

---

## ☁️ Deployment

### Deploy Backend on Render (Free)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your repo
4. Render auto-detects `render.yaml` — click **Deploy**
5. Note your service URL (e.g. `https://resume-analyzer-api.onrender.com`)

### Deploy Backend on Railway

1. Install Railway CLI: `npm i -g @railway/cli`
2. `railway login && railway init && railway up`
3. Railway uses the `Procfile` automatically

### Host Frontend

After deploying the backend, update `API_BASE` in `frontend/index.html`:

```javascript
const API_BASE = "https://your-backend-url.onrender.com";
```

Then host the frontend on any of:
- **GitHub Pages** — push `frontend/` to a `gh-pages` branch
- **Netlify** — drag & drop the `frontend/` folder at netlify.com
- **Vercel** — `vercel --cwd frontend`

---

## 🎯 Interview Talking Points

- **Model choice**: `all-MiniLM-L6-v2` is a distilled BERT model optimized for semantic similarity — 5x faster than full BERT with 95% of the accuracy
- **Cosine similarity**: measures the angle between embedding vectors, not magnitude — ideal for skill matching
- **Weighted scoring**: domain-specific skills (ML, cloud) weighted higher than soft skills, reflecting real hiring priorities
- **Threshold tuning**: 0.72 cosine similarity threshold balances precision vs recall for skill matching
- **Modular design**: each utility is independently testable and replaceable

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI, Python 3.11 |
| NLP Model | sentence-transformers/all-MiniLM-L6-v2 |
| PDF Parsing | pdfplumber |
| Similarity | scikit-learn cosine_similarity |
| Frontend | Vanilla HTML/CSS/JS |
| Deployment | Render / Railway / Netlify |
