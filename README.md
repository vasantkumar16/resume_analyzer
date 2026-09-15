# AI Resume Analyzer

An AI-powered web application that analyzes resumes against job descriptions using Retrieval-Augmented Generation (RAG), semantic embeddings, and Google Gemini.

The system helps applicants understand how well their resume matches a job description and helps recruiters analyze and compare multiple candidates for a job role.

## 📌 Project Overview

The AI Resume Analyzer is a Flask-based web application designed to simplify the resume screening and job-matching process. Instead of relying only on traditional keyword matching, the application uses semantic search and RAG to understand the meaning and context of information present in resumes and job descriptions.

The application supports two types of users:
* 👤 **Applicant**
* 🧑‍💼 **Recruiter**

## ✨ Features

### 👤 Applicant Features
* **Applicant registration and login:** Secure password-based authentication.
* **Upload resume:** Supports PDF or DOCX formats.
* **Enter a job description:** For targeted analysis.
* **AI-powered resume analysis:**
  * Resume-to-job match score
  * Matching skills identification
  * Missing skills identification
  * Strengths and weaknesses analysis
  * AI-generated resume summary
* **Analysis history:** Previous analysis retrieval and duplicate analysis detection.

### 🧑‍💼 Recruiter Features
* **Recruiter registration and login:** Secure access to the recruiter workspace.
* **Recruiter dashboard:** Centralized hub for hiring.
* **Create job postings:** Add job title, company, location, employment type, and job description.
* **Upload multiple candidate resumes:** Batch processing support.
* **Analyze multiple candidates against a job:**
  * Generate AI-based candidate match scores
  * Identify matching and missing skills
  * View candidate strengths, weaknesses, and summaries
* **Set a cutoff score:** Review candidates based on the cutoff.
* **Maintain recruitment history:** View previous recruitment sessions.

## 🤖 AI and RAG Features

The application uses a Retrieval-Augmented Generation (RAG) approach for resume analysis. The basic workflow is:

```text
Resume
   ↓
Text Extraction
   ↓
Section Detection
   ↓
Semantic Chunking
   ↓
Gemini Embeddings
   ↓
ChromaDB
   ↓
Semantic Retrieval
   ↓
Relevant Resume Chunks
   ↓
Google Gemini
   ↓
Resume Analysis
The system retrieves the most relevant parts of the resume before sending the information to the AI model. This allows the model to focus on the sections of the resume that are most relevant to the job description.🧠 Why RAG?Traditional resume screening systems often depend heavily on exact keyword matching.For example:Job Description: Experience in developing predictive models.Resume: Developed machine learning models for classification and prediction.A simple keyword-based system may not fully understand that these two statements are related. With semantic embeddings, the application can identify content based on meaning and context, not just exact words.RAG helps the system:Retrieve relevant resume informationReduce unnecessary information sent to the AI modelImprove contextual understandingProvide analysis based on actual resume contentCompare resumes and job descriptions more intelligently🛠️ Technology StackCategoryTechnologyProgramming LanguagePythonBackendFlaskFrontendHTML, CSS, Jinja2DatabaseSQLiteORMFlask-SQLAlchemyAI ModelGoogle GeminiEmbeddingsGemini EmbeddingsVector DatabaseChromaDBText ProcessingLangChainPDF ProcessingPyMuPDFDOCX Processingpython-docxAuthenticationFlask SessionsPassword SecurityWerkzeugEnvironment Variablespython-dotenv📂 Project StructurePlaintextAI-Resume-Analyzer/
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
├── utils/
│   ├── hash_utils.py
│   └── timezone.py
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
│   └── resumes/
│
├── chroma_db/
│
└── instance/
    └── resume_analyzer.db
🔄 Application WorkflowApplicant WorkflowApplicant Registration ➔ Applicant Login ➔ Upload Resume ➔ Enter Job Description ➔ Extract Resume Text ➔ Create Resume Chunks ➔ Generate Embeddings ➔ Store in ChromaDB ➔ Retrieve Relevant Chunks ➔ Google Gemini Analysis ➔ Display Results ➔ Save Analysis HistoryRecruiter WorkflowRecruiter Registration ➔ Recruiter Login ➔ Create Job Posting ➔ Enter Job Description ➔ Upload Multiple Resumes ➔ Process Candidate Resumes ➔ Generate Embeddings ➔ Semantic Retrieval ➔ Google Gemini Analysis ➔ Generate Candidate Scores ➔ Apply Cutoff Score ➔ Review Candidate Results ➔ Save Recruitment History📄 Resume ProcessingThe application supports the following resume formats:PDF: Text is extracted using PyMuPDF.DOCX: Text is extracted using python-docx.After extracting the text, the application processes the content and identifies different resume sections. Common sections include: Summary, Profile, Objective, Skills, Technical Skills, Experience, Internship, Projects, Education, Certifications, and Achievements.✂️ Semantic ChunkingLarge resume text is divided into smaller chunks before generating embeddings. The application uses a recursive text splitter.chunk_size = 800chunk_overlap = 100Why chunking?A complete resume can contain a large amount of information. Instead of embedding the entire resume as one large piece, it is divided into smaller meaningful sections. Each chunk can then be searched independently.Chunk Metadata:Each chunk can contain information such as resume_id, candidate_name, section, content, and embedding. This allows the application to identify where retrieved information came from.🔎 Semantic SearchAfter resume chunks are stored in ChromaDB, the application performs semantic retrieval. The job description is used to identify the most relevant resume chunks.For example, if a job requires: Python + Machine Learning + SQL, the system searches the vector database for resume sections that are semantically related to these requirements. The retrieved chunks are then provided to the Gemini model for analysis.🗄️ ChromaDBThe application uses ChromaDB as the local vector database, stored in the chroma_db/ folder.ChromaDB stores:Resume chunksEmbeddingsResume IDsCandidate informationSection metadata🤖 AI AnalysisGoogle Gemini is used to analyze the retrieved resume content against the job description. The analysis includes the overall match score, matching skills, missing skills, strengths, weaknesses, and a summary.Example response:JSON{
    "overall_score": 82.5,
    "matching_skills": ["Python", "Machine Learning", "SQL"],
    "missing_skills": ["Docker", "AWS"],
    "summary": "The candidate has a strong foundation in Python and machine learning and matches several core requirements of the role.",
    "strengths": ["Strong Python knowledge", "Relevant machine learning projects"],
    "weaknesses": ["Limited cloud experience"]
}
🔐 AuthenticationThe application provides separate authentication for Applicants and Recruiters. User passwords are not stored directly; they are securely hashed using Werkzeug password hashing. The application also uses Flask sessions to maintain logged-in users. Role-based access prevents applicants from accessing recruiter-specific functionality.♻️ Duplicate Analysis DetectionThe application uses hashing to avoid unnecessary repeated AI analysis. Hashes are generated for the Resume and the Job Description. The application checks whether the same resume has already been analyzed for the same job description to reduce unnecessary API requests and save processing time.🗃️ Database ModelsThe application uses SQLite with Flask-SQLAlchemy.User: Stores User ID, Name, Email, Password hash, and Role.JobPosting: Stores Job ID, Recruiter ID, Job title, Company, Location, Employment type, Job description, Job hash, and Job status.AnalysisHistory: Stores applicant resume analysis information including match score, skills, strengths/weaknesses, summary, and timestamp.RecruitmentSession: Stores information about a recruiter's candidate analysis session and cutoff scores.CandidateResult: Stores individual candidate results for a recruitment session including selection status.⚙️ Installation1. Clone the RepositoryBashgit clone [https://github.com/vasantkumar16/resume_analyzer.git](https://github.com/vasantkumar16/resume_analyzer.git)
cd resume_analyzer
2. Create a Virtual EnvironmentBash# For Windows:
python -m venv venv
venv\Scripts\activate

# For PowerShell:
.\venv\Scripts\Activate.ps1
3. Install DependenciesBashpip install -r requirements.txt
🔑 Environment VariablesCreate a .env file in the root directory.Code snippetGEMINI_API_KEY=your_gemini_api_key
SECRET_KEY=your_secure_secret_key
GEMINI_API_KEY: The API key used to access Google Gemini services.SECRET_KEY: The Flask secret key used for securely signing session-related data.Note: Do not publish your actual API key or secret key on GitHub. Make sure .env is inside your .gitignore file.▶️ Running the ApplicationAfter activating the virtual environment, run:Bashpython app.py
The Flask application will normally be available at http://127.0.0.1:5000. Open the address in your browser.📊 Example MatchingSuppose a job description requires: Python, Machine Learning, SQL, Flask, Git.A candidate's resume contains: Python, Machine Learning, SQL, Flask.The system may identify:Matching Skills: Python, Machine Learning, SQL, FlaskMissing Skills: GitThe final score is generated by the AI based on the retrieved resume information and job requirements.🔒 Security ConsiderationsThe project includes basic security practices such as password hashing, session-based authentication, role-based access, secure filename handling, and environment variables for API keys.For production deployment, additional security improvements are recommended: CSRF protection, HTTPS, file-size restrictions, File-content validation, a production database (like PostgreSQL), and rate limiting.⚠️ Important NotesGemini API: The application depends on Google Gemini APIs. API model availability, quotas, rate limits, and pricing may change.Resume Privacy: Uploaded resumes may contain personal information. Do not upload real candidate resumes to a public GitHub repository. The uploads/, chroma_db/, and instance/ folders should generally not contain publicly committed personal data.🚀 Future EnhancementsPossible improvements include:Candidate rankingAdvanced skill normalizationOCR support for scanned resumesApplicant AI doubt assistantAutomated Email notificationsProduction PostgreSQL database & Cloud deployment👥 Team MembersThis project was developed collaboratively as a group project to demonstrate the practical implementation of AI-powered application development.Vasant Kumar - GitHubVinod AVinuta Naik - GitHubVishalakshi N R🎓 Project PurposeThis project was developed as an academic/group project to demonstrate the practical application of Python, Flask, Machine Learning concepts, Generative AI, RAG, Semantic Search, Vector Databases, Embeddings, Natural Language Processing, and Web Application Development. The project demonstrates how AI can be integrated into a real-world recruitment and resume-screening workflow.⚖️ DisclaimerThe AI-generated match scores, recommendations, and candidate insights are intended to assist users in resume analysis and recruitment workflows. They should not be used as the sole basis for making employment decisions. Human review and judgment should always be considered.
