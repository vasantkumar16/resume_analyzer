
# AI Resume Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Google%20Gemini-Generative%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini">
  <img src="https://img.shields.io/badge/ChromaDB-Vector%20Database-orange?style=for-the-badge" alt="ChromaDB">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

<p align="center">
  <b>An AI-powered resume analysis and recruitment assistance platform built with Flask, Google Gemini, ChromaDB, and SQLite.</b>
</p>

<p align="center">
  Upload a resume, provide a job description, and receive an AI-generated analysis of skills, strengths, weaknesses, and job compatibility.
</p>

---

## 📌 Project Overview

The **AI Resume Analyzer** is a web-based application designed to help job seekers and recruiters evaluate resumes against job descriptions using Generative AI and semantic search.

Traditional resume screening can be time-consuming, especially when candidates need to compare their skills and projects with different job requirements.

This project addresses that challenge by combining:

- Resume text extraction
- Semantic text chunking
- AI-powered embeddings
- ChromaDB vector search
- Google Gemini-based resume analysis
- Match score generation
- Applicant analysis history
- Recruiter job posting and candidate screening

The application provides two main user roles:

1. **Applicant** – Upload a resume and analyze it against a job description.
2. **Recruiter** – Create job postings and analyze multiple candidate resumes.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To automate basic resume-to-job-description comparison.
- To identify relevant skills present in a candidate's resume.
- To identify important job requirements not supported by the resume.
- To generate an overall resume match score.
- To provide concise AI-generated resume feedback.
- To support semantic retrieval of relevant resume content.
- To maintain analysis history using a relational database.
- To provide a foundation for AI-assisted recruitment workflows.

---

## ✨ Key Features

### 👤 Applicant Features

- Applicant registration and login.
- Secure password hashing.
- Resume upload support.
- PDF and DOCX resume extraction.
- Job description input.
- AI-powered resume analysis.
- Overall match score from 0–100.
- Matching skills identification.
- Missing skills identification.
- Resume strengths and weaknesses.
- Professional AI-generated summary.
- Saved analysis history.
- Cached results for repeated resume/job combinations.

### 🏢 Recruiter Features

- Recruiter registration and login.
- Recruiter dashboard.
- Create job postings.
- Store job descriptions.
- Open and close job postings.
- Upload multiple candidate resumes.
- Analyze candidates against a job description.
- Configure a shortlist cutoff score.
- Automatically classify candidates as:
  - SHORTLISTED
  - REJECTED
- Rank candidates by match score.
- View recruitment history.
- View candidate analysis details.

### 🤖 AI & Semantic Search Features

- Google Gemini API integration.
- Gemini embedding generation.
- ChromaDB persistent vector storage.
- Semantic resume chunk retrieval.
- Section-aware resume processing.
- Structured JSON AI responses.
- Match score normalization.
- Basic Gemini quota/rate-limit retry handling.

### 🔐 Security & Data Features

- Environment-variable API key configuration.
- `.env` excluded from Git tracking.
- Password hashing using Werkzeug.
- Session-based authentication.
- Applicant/recruiter role protection.
- User-specific analysis history.
- Recruiter-specific job and recruitment history.
- File hashing for duplicate analysis detection.

---

## 🧠 How the Application Works

The application follows a Retrieval-Augmented Generation (RAG)-inspired workflow.

Instead of sending the complete extracted resume directly to the AI, the application:

1. Extracts text from the uploaded resume.
2. Divides the resume into meaningful sections.
3. Splits sections into smaller chunks.
4. Generates embeddings for the chunks.
5. Stores the embeddings in ChromaDB.
6. Uses the job description as the semantic search query.
7. Retrieves the most relevant resume chunks.
8. Sends the job description and retrieved resume evidence to Gemini.
9. Receives a structured analysis.
10. Displays and stores the result.

### 🔄 Resume Analysis Workflow

```text
                    ┌──────────────────────┐
                    │      User Uploads    │
                    │   Resume + Job JD     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Flask Web App      │
                    │   Input Validation   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Resume Extraction   │
                    │      PDF / DOCX      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Semantic Chunking   │
                    │  Section Detection   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Gemini Embeddings    │
                    │ gemini-embedding-001  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      ChromaDB        │
                    │   Vector Storage     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Semantic Retrieval   │
                    │ Relevant Resume Text │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Google Gemini     │
                    │ Resume + JD Analysis │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Structured Analysis  │
                    │ Score, Skills, etc.  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    SQLite Database   │
                    │    Saved History     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Results Dashboard  │
                    └──────────────────────┘
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Flask | Web application framework |
| Flask-SQLAlchemy | Database ORM |
| SQLite | Relational database |
| Google Gemini API | AI-powered resume analysis |
| Gemini Embeddings | Resume semantic embeddings |
| ChromaDB | Persistent vector database |
| PyMuPDF | PDF text extraction |
| python-docx | DOCX text extraction |
| LangChain Text Splitters | Resume text chunking |
| Werkzeug | Password hashing and file security |
| python-dotenv | Environment variable management |
| HTML5 | Frontend structure |
| CSS3 | Frontend styling |
| Jinja2 | Dynamic HTML templates |

---

## 🏗️ System Architecture

The application follows a modular Flask architecture.

```text
                         ┌─────────────────────┐
                         │      Frontend       │
                         │ HTML + CSS + Jinja2  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Flask App       │
                         │      app.py         │
                         └───────┬─────┬───────┘
                                 │     │
                ┌────────────────┘     └────────────────┐
                ▼                                       ▼
      ┌───────────────────┐                  ┌───────────────────┐
      │ Applicant Module  │                  │ Recruiter Module  │
      │ Resume Analysis   │                  │ Job Screening     │
      └─────────┬─────────┘                  └─────────┬─────────┘
                │                                      │
                └────────────────┬─────────────────────┘
                                 ▼
                       ┌───────────────────┐
                       │  Resume Services  │
                       │ Extraction        │
                       │ Chunking          │
                       │ Embeddings        │
                       │ Vector Retrieval  │
                       └─────────┬─────────┘
                                 │
                ┌────────────────┴────────────────┐
                ▼                                 ▼
       ┌──────────────────┐              ┌──────────────────┐
       │ Google Gemini    │              │    ChromaDB      │
       │ AI Analysis      │              │ Vector Storage   │
       └──────────────────┘              └──────────────────┘
                                 │
                                 ▼
                       ┌───────────────────┐
                       │    SQLite DB      │
                       │ Users             │
                       │ Job Postings      │
                       │ Analysis History  │
                       │ Candidate Results │
                       └───────────────────┘
```

---

## 📂 Project Structure

```text
Resume_Analyzer_Final/
│
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── job_posting.py
│   ├── analysis_history.py
│   └── recruitment_history.py
│
├── services/
│   ├── embedding_service.py
│   ├── resume_analyzer.py
│   ├── resume_extractor.py
│   ├── section_chunker.py
│   ├── vector_store.py
│   └── email_service.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── applicant_dashboard.html
│   ├── recruiter_dashboard.html
│   ├── create_job.html
│   ├── analyze_candidates.html
│   ├── results.html
│   ├── history.html
│   ├── recruiter_history.html
│   └── recruitment_details.html
│
├── static/
│   └── style.css
│
├── uploads/
│   └── .gitkeep
│
├── chroma_db/
│   └── .gitkeep
│
└── instance/
    └── .gitkeep
```

> **Note:** The structure above represents the main application modules. Your uploaded project also contains runtime-generated database files, ChromaDB files, and Python cache folders. These should remain excluded from Git.

---

## 🔍 Detailed Module Explanation

### 1. `app.py`

The main Flask application file.

Responsibilities:

- Application initialization.
- Flask configuration loading.
- Database initialization.
- User registration and login.
- Role-based access control.
- Resume upload handling.
- Applicant analysis.
- Recruiter job posting.
- Multi-resume candidate analysis.
- Recruitment history.
- Results rendering.

Important routes include:

```text
/
```

Application landing page.

```text
/register/applicant
/register/recruiter
```

Applicant and recruiter registration.

```text
/login/applicant
/login/recruiter
```

Role-specific login.

```text
/applicant/dashboard
```

Applicant resume analysis dashboard.

```text
/applicant/history
```

Applicant analysis history.

```text
/recruiter/dashboard
```

Recruiter dashboard.

```text
/recruiter/jobs/create
```

Create a job posting.

```text
/recruiter/jobs/<job_id>/analyze
```

Analyze multiple candidate resumes.

```text
/recruiter/history
```

Recruitment history.

---

### 2. `config.py`

Stores application configuration.

Current configuration includes:

- Flask secret key.
- SQLite database URI.
- SQLAlchemy tracking configuration.
- Resume upload folder.

Example:

```python
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret")
    SQLALCHEMY_DATABASE_URI = "sqlite:///resume_analyzer.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "uploads/resumes"
```

---

### 3. `database.py`

Initializes Flask-SQLAlchemy.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

The database object is imported by the model files.

---

### 4. `services/resume_extractor.py`

Extracts text from supported resume files.

Supported formats:

- PDF
- DOCX

Libraries used:

- PyMuPDF (`fitz`)
- python-docx

Example:

```python
def extract_resume_text(path):
    if path.lower().endswith(".pdf"):
        doc = fitz.open(path)
        text = "\n".join(page.get_text() for page in doc)
        doc.close()
        return text

    if path.lower().endswith(".docx"):
        doc = Document(path)
        return "\n".join(
            p.text for p in doc.paragraphs if p.text.strip()
        )

    raise ValueError("Only PDF and DOCX files are supported.")
```

---

### 5. `services/section_chunker.py`

Converts extracted resume text into semantic chunks.

The system identifies common resume sections such as:

- Summary
- Skills
- Experience
- Projects
- Education
- Certifications
- Achievements

The project uses `RecursiveCharacterTextSplitter` with:

```text
Chunk size: 800 characters
Chunk overlap: 100 characters
```

Each chunk stores:

```python
{
    "section": "skills",
    "content": "Extracted resume content..."
}
```

This helps preserve section context during semantic retrieval.

---

### 6. `services/embedding_service.py`

Generates vector embeddings for resume content using Gemini.

Configured embedding model:

```text
gemini-embedding-001
```

Example:

```python
def get_embedding(text):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values
```

Embeddings convert text into numerical vectors that can be compared for semantic similarity.

---

### 7. `services/vector_store.py`

Manages ChromaDB.

The project uses a persistent ChromaDB client:

```python
client = chromadb.PersistentClient(path="chroma_db")
```

Collection:

```text
resume_collection
```

Main operations:

#### Store resume chunks

```python
store_resume_chunks(
    resume_id,
    candidate_name,
    chunks
)
```

#### Retrieve relevant resume chunks

```python
retrieve_resume_chunks(
    resume_id,
    query,
    n_results=10
)
```

The query is the job description.

The vector store returns relevant resume content and section metadata.

---

### 8. `services/resume_analyzer.py`

This module performs the main AI analysis.

Configured generation model in the uploaded source:

```text
gemini-3.5-flash-lite
```

The analysis process:

1. Retrieve relevant resume chunks.
2. Combine them into resume evidence.
3. Build a structured analysis prompt.
4. Send the prompt to Gemini.
5. Parse the JSON response.
6. Normalize the match score.
7. Return the analysis.

Expected output:

```json
{
  "overall_score": 0,
  "matching_skills": [],
  "missing_skills": [],
  "summary": "",
  "strengths": [],
  "weaknesses": []
}
```

The prompt instructs Gemini to:

- Use only resume evidence.
- Avoid inventing qualifications.
- Compare skills, experience, projects, education, and technologies.
- Return a score from 0 to 100.
- Return valid JSON.

---

### 9. `models/user.py`

Stores registered users.

Fields:

| Field | Description |
|------|-------------|
| id | Primary key |
| username | User name |
| email | Unique email |
| password_hash | Hashed password |
| role | Applicant or recruiter |

Passwords are hashed using Werkzeug.

```python
user.set_password(password)
```

Password verification:

```python
user.check_password(password)
```

---

### 10. `models/job_posting.py`

Stores recruiter job postings.

Fields include:

- Job title
- Company
- Location
- Employment type
- Job description
- Job hash
- Job status
- Creation timestamp

Supported statuses:

```text
OPEN
CLOSED
```

---

### 11. `models/analysis_history.py`

Stores applicant resume analysis history.

Stored information includes:

- User ID
- Resume filename
- Resume hash
- Job hash
- Job description
- Match score
- Matching skills
- Missing skills
- Summary
- Strengths
- Weaknesses
- Creation timestamp

A unique constraint prevents duplicate analysis records for the same user, resume, and job description combination.

---

### 12. `models/recruitment_history.py`

Contains:

#### RecruitmentSession

Stores:

- Recruiter ID
- Job ID
- Job title
- Job description
- Job hash
- Cutoff score
- Creation time

#### CandidateResult

Stores:

- Candidate name
- Resume hash
- Job hash
- Match score
- Candidate status
- Matching skills
- Missing skills
- Summary
- Strengths
- Weaknesses

---

## 🧮 Resume Match Score

The application generates an overall match score between 0 and 100 using Gemini.

The score is normalized in the application:

```python
score = max(0.0, min(100.0, score))
```

### Score Interpretation

| Score Range | General Interpretation |
|-------------|------------------------|
| 80–100 | Strong alignment |
| 60–79 | Moderate to strong alignment |
| 40–59 | Partial alignment |
| 0–39 | Low alignment |

> These ranges are illustrative interpretations for understanding the result. They are not scientifically validated hiring thresholds.

### Recruiter Cutoff

Recruiters can configure a cutoff score.

Example:

```text
Cutoff score: 60
```

Candidates are classified as:

```text
Score >= 60 → SHORTLISTED
Score < 60  → REJECTED
```

The cutoff can be adjusted between 0 and 100.

---

## 🔐 Security Implementation

The project includes several security-related practices.

### Environment Variables

The Gemini API key is loaded using `python-dotenv`.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_secret_key
```

### Password Hashing

Passwords are not stored as plain text.

Werkzeug password hashing is used:

```python
generate_password_hash()
check_password_hash()
```

### Role-Based Authentication

Applicants and recruiters have separate protected routes.

The application checks:

- User login status.
- Session user ID.
- Session role.
- Database user validity.

### File Validation

The application allows:

```text
.pdf
.docx
```

Files are saved using secure filenames and unique generated names.

### Git Protection

Sensitive and generated files are excluded through `.gitignore`.

Excluded examples:

```text
.env
__pycache__/
*.pyc
instance/*.db
uploads/*
chroma_db/*
```

---

## ⚙️ Installation & Setup

Follow the steps below to run the project locally.

### Prerequisites

Install the following:

- Python 3.11 or newer.
- Git.
- A Google Gemini API key.
- A Windows, Linux, or macOS environment.

Python 3.11 is recommended for this project because it is a stable Python version with broad library compatibility.

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/resume_analyzer.git
```

Move into the project folder:

```bash
cd resume_analyzer
```

> Replace `YOUR_USERNAME` with your actual GitHub username.

---

### Step 2: Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt:

```cmd
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

The project dependencies include:

```text
Flask
Flask-SQLAlchemy
Werkzeug
python-dotenv
PyMuPDF
python-docx
chromadb
google-genai
langchain
langchain-core
langchain-text-splitters
pydantic
langchain-community
```

---

### Step 4: Configure Environment Variables

Create a `.env` file in the project root.

Copy the example file:

Windows:

```powershell
Copy-Item .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

Open `.env` and configure:

```env
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_secret_key
```

### Get a Gemini API Key

You can obtain a Gemini API key from Google AI Studio:

https://aistudio.google.com/

Never commit your actual API key to GitHub.

---

### Step 5: Run the Application

```bash
python app.py
```

The Flask application will start in development mode.

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🖥️ Application Usage

### Applicant Workflow

```text
1. Open the application.
2. Register as an applicant.
3. Login.
4. Upload a PDF or DOCX resume.
5. Enter the target job description.
6. Submit for analysis.
7. View the match score.
8. Review matching skills.
9. Review missing skills.
10. Read strengths and weaknesses.
11. View saved analysis history.
```

### Recruiter Workflow

```text
1. Register as a recruiter.
2. Login.
3. Open recruiter dashboard.
4. Create a job posting.
5. Enter job title and description.
6. Upload multiple candidate resumes.
7. Set a cutoff score.
8. Run candidate analysis.
9. View ranked results.
10. Review shortlisted and rejected candidates.
11. Open recruitment history.
```

---

## 📊 Example AI Analysis Output

The application returns a structured result similar to:

```json
{
  "overall_score": 82.5,
  "matching_skills": [
    "Python",
    "Flask",
    "SQL",
    "Machine Learning"
  ],
  "missing_skills": [
    "Docker",
    "AWS"
  ],
  "summary": "The candidate demonstrates good alignment with the role through relevant technical skills and project experience.",
  "strengths": [
    "Relevant programming experience",
    "Project-based technical exposure",
    "Strong alignment with required technologies"
  ],
  "weaknesses": [
    "Limited evidence of cloud deployment",
    "Some job requirements are not supported by the resume"
  ]
}
```

> The above is an illustrative example of the output structure. Actual scores and skills depend on the uploaded resume, job description, and Gemini response.

---

## 🗃️ Database Design

The application uses SQLite with Flask-SQLAlchemy.

### Main Tables

```text
User
 │
 ├── AnalysisHistory
 │
 ├── JobPosting
 │      │
 │      └── RecruitmentSession
 │              │
 │              └── CandidateResult
```

### User Table

```text
User
├── id
├── username
├── email
├── password_hash
└── role
```

### Job Posting Table

```text
JobPosting
├── id
├── recruiter_id
├── title
├── company
├── location
├── employment_type
├── job_description
├── job_hash
├── status
└── created_at
```

### Analysis History Table

```text
AnalysisHistory
├── id
├── user_id
├── resume_name
├── resume_hash
├── job_hash
├── job_description
├── match_score
├── matching_skills
├── missing_skills
├── summary
├── strengths
├── weaknesses
└── created_at
```

### Recruitment Session Table

```text
RecruitmentSession
├── id
├── recruiter_id
├── job_id
├── job_title
├── job_description
├── job_hash
├── cutoff_score
└── created_at
```

### Candidate Result Table

```text
CandidateResult
├── id
├── session_id
├── candidate_name
├── resume_hash
├── job_hash
├── match_score
├── status
├── matching_skills
├── missing_skills
├── summary
├── strengths
├── weaknesses
└── created_at
```

---

## 🔄 Duplicate Analysis Handling

The project uses hashes to identify repeated resume/job combinations.

For applicant analysis, the application calculates:

```text
Resume Hash
+
Job Description Hash
```

If the same combination has already been analyzed for the same applicant, the application retrieves the saved result from SQLite.

This helps avoid unnecessary repeated analysis requests.

For recruiter candidate analysis, existing matching results can also be reused.

---

## 📁 Data Storage

### SQLite

Stores:

- Users.
- Job postings.
- Applicant analysis history.
- Recruitment sessions.
- Candidate results.

### ChromaDB

Stores:

- Resume text chunks.
- Embeddings.
- Resume IDs.
- Candidate names.
- Resume section metadata.

### Upload Folder

Uploaded resumes are stored locally in the configured upload folder.

### Environment File

The `.env` file stores sensitive configuration such as the Gemini API key.

---

## 🚀 Future Enhancements

The current project provides a foundation for AI-assisted resume screening. Possible future improvements include:

### AI Improvements

- More advanced resume section detection.
- Better skill normalization.
- Improved job requirement extraction.
- More consistent score calibration.
- Resume recommendations and improvement suggestions.
- Support for additional AI models.
- Better handling of scanned resumes using OCR.

### Applicant Improvements

- Resume improvement suggestions.
- ATS-style keyword analysis.
- Resume version comparison.
- Export analysis reports as PDF.
- Skill-gap learning recommendations.
- Dashboard analytics.

### Recruiter Improvements

- Candidate profile management.
- Search and filter candidates.
- Export shortlisted candidates.
- Interview scheduling.
- Candidate communication management.
- Advanced recruitment analytics.
- Role-based recruiter permissions.

### Technical Improvements

- Production deployment.
- PostgreSQL support.
- Cloud file storage.
- Background task processing.
- Automated testing.
- Better error logging.
- Database migrations.
- Docker support.
- CI/CD integration.

---

## ⚠️ Limitations

- Resume extraction currently supports PDF and DOCX files.
- The application depends on the Gemini API for AI analysis and embeddings.
- API quota and rate limits may affect analysis.
- Match scores are AI-generated estimates, not validated hiring predictions.
- The current project uses SQLite for local database storage.
- Uploaded resumes are stored locally.
- The application is currently configured for development use.
- AI results may contain inaccuracies and should be reviewed.
- A high score does not guarantee interview selection or employment.

---

## 🔒 Responsible AI Disclaimer

This project is intended as an educational and recruitment-assistance tool.

AI-generated resume scores should not be treated as the sole basis for hiring decisions.

Recruiters should independently review:

- Candidate qualifications.
- Relevant experience.
- Technical skills.
- Projects.
- Communication skills.
- Job requirements.
- Candidate consent and privacy.

The system should be improved and tested for fairness before being used in real-world automated hiring decisions.

---

## 👨‍💻 Developer

**Vasant Kumar**

Computer Science and Engineering Student

Aspiring Software Developer

### Technical Interests

- Java
- Python
- Flask
- SQL
- Artificial Intelligence
- Generative AI
- Web Development
- Software Engineering

---

## 📚 Learning Outcomes

Through this project, the following concepts were explored:

- Python programming.
- Flask web development.
- REST-style application routing.
- User authentication.
- Password hashing.
- SQLAlchemy ORM.
- SQLite database management.
- Resume text extraction.
- Natural language processing concepts.
- Semantic text chunking.
- Vector embeddings.
- ChromaDB vector search.
- Google Gemini API integration.
- Retrieval-Augmented Generation concepts.
- JSON response processing.
- Git and GitHub version control.
- Environment variable security.

---

## 📌 Project Status

```text
Project Type: Academic / Personal Project
Status: Active Development
Application: Flask Web Application
AI Provider: Google Gemini API
Vector Database: ChromaDB
Relational Database: SQLite
```

---

## ⭐ Support

If you find this project useful, consider giving the repository a star ⭐

Feedback and suggestions are welcome.

---

<p align="center">
  <b>Built with Python, Flask, Google Gemini, and ChromaDB.</b>
</p>
