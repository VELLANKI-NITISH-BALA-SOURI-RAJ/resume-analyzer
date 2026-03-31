#  AI Resume Analyzer & Job Matcher

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![NLP](https://img.shields.io/badge/NLP-Transformers-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🔗 Live Demo
👉 *Add your live link here when deployed* (https://resume-analyzer-m7op.onrender.com/)

---

## 📌 Overview

An AI-powered system that analyzes resumes and matches them with job descriptions using **semantic NLP**. 

Unlike traditional keyword-matching systems, this project understands **contextual meaning** using Transformers and provides:

* **Match Score** (0–100)
* **Matched Skills** vs. **Missing Skills**
* **Actionable Improvement Suggestions**

---

## 🧠 Features

* 📄 **Resume Upload:** Supports PDF parsing.
* 🔍 **Skill Extraction:** Rule-based identification of technical proficiencies.
* 🤖 **Semantic Matching:** Leverages BERT embeddings for deeper context.
* 📊 **Intelligent Scoring:** Weighted scoring system for accurate assessment.
* 🌐 **REST API:** Fast and lightweight backend powered by FastAPI.

---

## ⚙️ Tech Stack

* **Backend:** FastAPI, Uvicorn
* **NLP:** Sentence Transformers (`all-MiniLM-L6-v2`)
* **ML:** Scikit-learn (Cosine Similarity)
* **Processing:** pdfplumber, Regex

---

## 🏗️ Architecture

```text
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
