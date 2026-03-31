
# 🚀 AI Resume Analyzer & Job Matcher

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![NLP](https://img.shields.io/badge/NLP-Transformers-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🔗 Live Demo
👉 https://resume-analyzer-m7op.onrender.com/

---

## 📌 Overview

An AI-powered system that analyzes resumes and matches them with job descriptions using **semantic NLP**.

Unlike traditional keyword-based systems, this project understands **contextual meaning** using Transformers and provides:

- **Match Score (0–100)**
- **Matched vs Missing Skills**
- **Actionable Improvement Suggestions**

---

## 🧠 Features

- 📄 Resume upload with PDF parsing  
- 🔍 Rule-based skill extraction using structured taxonomy  
- 🤖 Semantic matching using BERT-based embeddings  
- 📊 Weighted scoring system for accurate evaluation  
- ⚠️ Missing skill identification  
- 💡 Personalized improvement suggestions  
- 🌐 REST API using FastAPI  

---

## ⚙️ Tech Stack

- **Backend:** FastAPI, Uvicorn  
- **NLP:** Sentence Transformers (`all-MiniLM-L6-v2`)  
- **ML:** Scikit-learn (Cosine Similarity)  
- **Processing:** pdfplumber, Regex  

---

## 🏗️ Architecture

```

Resume + Job Description
↓
PDF Parsing
↓
Skill Extraction
↓
Embedding Generation
↓
Cosine Similarity
↓
Score Calculation
↓
Suggestions
↓
API Response

```

---

## 📊 How It Works

1. Extracts text from resume PDF  
2. Identifies skills using predefined taxonomy  
3. Converts skills into embeddings  
4. Computes similarity using cosine similarity  
5. Calculates final score using weighted formula  

```

Final Score = (Skill Score × 75%) + (Text Score × 25%)

````

---

## 📈 Example Output

```json
{
  "match_score": 82,
  "matched_skills": ["Python", "FastAPI", "SQL"],
  "missing_skills": ["Docker", "AWS"],
  "suggestions": [
    "Learn Docker",
    "Gain experience with AWS"
  ]
}
````

---

## 🚀 Run Locally

```bash
git clone https://github.com/VELLANKI-NITISH-BALA-SOURI-RAJ/resume-analyzer
cd resume-analyzer
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🌐 API

### POST `/analyze`

**Input:**

* `resume` → PDF file
* `job_desc` → text

**Output:**

* Match score
* Skill analysis
* Suggestions

---

## ⚠️ Limitations

* No OCR support (scanned PDFs not supported)
* Rule-based skill extraction (not ML-based)
* No database/storage

---

## 🔮 Future Improvements

* OCR integration (Tesseract)
* ML-based skill extraction (NER models)
* Database integration (PostgreSQL)
* Async processing (Celery)

---

## 👨‍💻 Author

**Nitish Bala Souri Raj**
📧 [nitishvraj17042006@gmail.com](mailto:nitishvraj17042006@gmail.com)
🔗 [https://github.com/nitishv2006-github](https://github.com/nitishv2006-github)

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐

