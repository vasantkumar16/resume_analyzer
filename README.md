# 🚀 AI-Powered Resume Analyzer

An intelligent, AI-powered web application that evaluates candidate resumes against job descriptions using **Retrieval-Augmented Generation (RAG)**, semantic embeddings, and **Google Gemini 2.5 Pro**. 

This system moves beyond traditional keyword-matching to understand the actual meaning and context of resumes, helping applicants optimize their profiles and enabling recruiters to rank multiple candidates efficiently.

---

## 📌 Project Overview
Traditional applicant tracking systems (ATS) often fail because they rely on exact keyword matches. For example, if a job requires *"predictive modeling"* and a resume says *"machine learning classification"*, a basic system might miss the connection. 

By leveraging semantic search and RAG, this application retrieves contextually relevant information from a candidate's resume and uses Generative AI to provide a deeply accurate, human-like evaluation.

### 👥 User Roles
*   **👤 Applicant:** Uploads a resume, enters a job description, and gets a detailed breakdown of their match score, strengths, and skill gaps.
*   **🧑‍💼 Recruiter:** Creates job postings, uploads batches of candidate resumes, sets cutoff scores, and automatically ranks the best talent.

---

## ✨ Features

### 👤 Applicant Features
*   **Secure Authentication:** Password-hashed registration and login.
*   **Document Parsing:** Seamless upload of PDF and DOCX formats.
*   **AI-Powered Analysis:** 
    *   Calculates a precise Resume-to-Job match score.
    *   Identifies exact matching skills and critical missing skills.
    *   Generates a professional summary and highlights strengths/weaknesses.
*   **History Tracking:** View and retrieve past analyses without spending extra processing time.

### 🧑‍💼 Recruiter Features
*   **Job Management:** Create and manage detailed job postings (Title, Company, Location, Employment Type).
*   **Batch Processing:** Upload multiple candidate resumes to a single job posting.
*   **Automated Ranking:** Generate AI match scores for the entire candidate pool.
*   **Cutoff Filtering:** Set a minimum score threshold to instantly shortlist top candidates.
*   **Recruitment History:** Maintain a secure log of all past recruitment sessions and candidate evaluations.

---

## 🧠 The RAG & AI Pipeline

The application uses a **Retrieval-Augmented Generation (RAG)** approach to ensure the AI analyzes the right information without getting overwhelmed by irrelevant text.

**Workflow:**
`Resume` ➔ `Text Extraction` ➔ `Section Detection` ➔ `Semantic Chunking` ➔ `Gemini Embeddings` ➔ `ChromaDB` ➔ `Semantic Retrieval` ➔ `Relevant Chunks` ➔ `Google Gemini` ➔ `Final Analysis`

### 📄 Document Processing & Section Detection
*   **PDFs** are extracted using `PyMuPDF`.
*   **DOCX** files are extracted using `python-docx`.
*   The system intelligently detects common resume sections (e.g., *Summary, Skills, Experience, Education, Certifications*).

### ✂️ Semantic Chunking
Large resumes are divided into smaller, highly meaningful chunks using a recursive text splitter before embedding.
*   `chunk_size = 800`
*   `chunk_overlap = 100`
*   **Metadata:** Each chunk retains its `resume_id`, `candidate_name`, and `section` so the AI knows exactly where the context came from.

### 🔎 Vector Search with ChromaDB
We utilize **ChromaDB** as our local vector database (stored in `/chroma_db/`). When a job description requires specific skills (e.g., *Python, ML, SQL*), the system searches ChromaDB to retrieve only the semantically related chunks from the resume.

### 🤖 AI Analysis (Google Gemini)
The retrieved chunks are fed to Google Gemini, which returns a structured JSON evaluation:
```json
{
    "overall_score": 82.5,
    "matching_skills": ["Python", "Machine Learning", "SQL"],
    "missing_skills": ["Docker", "AWS"],
    "summary": "The candidate has a strong foundation in Python and machine learning...",
    "strengths": ["Strong Python knowledge", "Relevant ML projects"],
    "weaknesses": ["Limited cloud experience"]
}
♻️ Duplicate Analysis DetectionTo save processing time and API limits, the system hashes both the Resume and the Job Description. If the same combination is uploaded again, it retrieves the existing database record rather than re-running the AI.🛠️ Technology StackCategoryTechnologyLanguagePythonBackend FrameworkFlaskFrontendHTML5, CSS3, Jinja2DatabaseSQLite, Flask-SQLAlchemyAI ModelGoogle Gemini 2.5 ProEmbeddingsGemini EmbeddingsVector DatabaseChromaDBText ProcessingLangChain, PyMuPDF, python-docxSecurityWerkzeug (Password Hashing), Flask Sessions🗃️ Database ModelsBuilt using SQLite and Flask-SQLAlchemy, the system relies on the following core models:User: ID, Name, Email, Password Hash, Role.JobPosting: Job ID, Recruiter ID, Title, Company, Location, Description, Hash, Status.AnalysisHistory: Applicant analysis records (Scores, Skills, Strengths, Weaknesses, Timestamps).RecruitmentSession: Recruiter sessions mapping jobs to cutoff scores.CandidateResult: Individual candidate evaluations tied to a specific recruitment session.📂 Project StructurePlaintextAI-Resume-Analyzer/
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── models/
│   ├── user.py, job_posting.py, analysis_history.py...
├── services/
│   ├── embedding_service.py, resume_analyzer.py, vector_store.py...
├── utils/
│   ├── hash_utils.py, timezone.py
├── templates/
│   ├── index.html, applicant_dashboard.html, recruiter_dashboard.html...
├── static/
│   └── style.css
├── uploads/
│   └── resumes/
├── chroma_db/
└── instance/
    └── resume_analyzer.db
⚙️ Installation & Setup1. Clone the RepositoryBashgit clone [https://github.com/vasantkumar16/resume_analyzer.git](https://github.com/vasantkumar16/resume_analyzer.git)
cd resume_analyzer
2. Create a Virtual EnvironmentBash# Windows
python -m venv venv
venv\Scripts\activate

# PowerShell
.\venv\Scripts\Activate.ps1
3. Install DependenciesBashpip install -r requirements.txt
4. Set Up Environment VariablesCreate a .env file in the root directory and add your secure keys. (Never commit this file to GitHub!)Code snippetGEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_secure_flask_session_key
5. Run the ApplicationBashpython app.py
Open your browser and navigate to http://127.0.0.1:5000.🔒 Security & Privacy ConsiderationsPassword Hashing: Passwords are never stored in plain text.Role-Based Access: Protected routes ensure applicants cannot access recruiter dashboards.Data Privacy: Uploaded resumes (/uploads) and vector stores (/chroma_db) are strictly kept out of version control.For Production: It is recommended to add CSRF protection, HTTPS, file-size restrictions, and migrate to PostgreSQL.🚀 Future EnhancementsCandidate filtering and advanced skill normalization.OCR support for scanned image-based resumes.Automated email notifications for shortlisted candidates.Job recommendation engine based on applicant resumes.Skill-gap learning recommendations.👥 Team MembersThis project was developed collaboratively as an academic group project to demonstrate the practical integration of Generative AI, Vector Databases, and Web Development into a real-world workflow.Vasant KumarVinod AVinuta NaikVishalakshi N R⚖️ Disclaimer: The AI-generated match scores, recommendations, and candidate insights are intended to assist users in resume analysis and recruitment workflows. They should not be used as the sole basis for making employment decisions. Human review and judgment should always be considered.
This is now perfectly formatted with clear headers, emojis for scannability, proper code blocks for terminal commands and JSON responses, and a clean table for your tech stack. 

After pasting this, just run your three Git commands (`git add .`, `git commit -m "Update README"`, `git push`) and check out how great it looks on your GitHub page!
