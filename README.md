# Resume Analyzer

A smart, web-based resume evaluation application designed to seamlessly analyze candidate resumes against specific job descriptions. By leveraging advanced AI models and vector embeddings, this tool automates the screening process, providing accurate match scores and actionable insights for recruiters.

## 🚀 Key Features

* **AI-Powered Evaluation:** Utilizes Google Gemini 2.5 Pro to intelligently analyze how well a candidate's skills and experience match a job posting.
* **Intelligent Document Processing:** Extracts text efficiently from PDF resumes using PyMuPDF and smartly chunks sections for deep analysis.
* **Vector Search Integration:** Uses ChromaDB to store and retrieve document embeddings, ensuring fast and context-aware candidate matching.
* **Role-Based Access:** Dedicated dashboards for both Applicants (to track submissions) and Recruiters (to create job postings and analyze candidate pools).
* **Secure Environment:** Protects sensitive API credentials and database configurations using environment variables.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript 
* **AI & Machine Learning:** Google Gemini 2.5 Pro API
* **Vector Database:** ChromaDB
* **Document Parsing:** PyMuPDF
* **Authentication & Security:** Werkzeug security hashing 

## 📂 Project Structure

* `/app.py` - Main application entry point and routing.
* `/models/` - Database schemas for users, job postings, and analysis history.
* `/services/` - Core business logic including the resume extractor, embedding service, and AI analyzer.
* `/templates/` - HTML files for the web interface (dashboards, login, results).
* `/static/` - CSS styling and client-side scripts.
* `/chroma_db/` - Local vector store for document embeddings.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/vasantkumar16/resume_analyzer.git](https://github.com/vasantkumar16/resume_analyzer.git)
   cd resume_analyzer
