# Resume Ranker App (GenAI-Powered)

**Resume Ranker App** is a user-friendly Streamlit application that leverages Azure OpenAI to evaluate and rank multiple resumes based on a provided job description. With this tool, recruiters and HR professionals can streamline their candidate screening process using AI-driven insights.

---

##  Features

- **Easy Upload**: Upload a job description PDF and up to 10 candidate resumes (PDF format).
- **AI-Powered Scoring**: Uses Azure OpenAI (GPT) to analyze and score each resume against the job description.
- **Automated Ranking**: Instantly ranks resumes from best to least match.
- **Secure & Private**: All processing happens within your environment; no data is stored.

##  How It Works

1. **Upload**  
   - Upload the job description as a PDF.
   - Upload up to 10 candidate resumes in PDF format.

2. **Processing**  
   - The app extracts text from each PDF.
   - For each resume, it uses Azure OpenAI to compare with the job description and assigns a match score (0-100).

3. **Results**  
   - Resumes are listed and ranked by their AI-generated match score.

---

##  Required Libraries

Install all dependencies using the requirements file:

```bash
pip install -r requirements.txt
```

**Main libraries used:**
- `streamlit`
- `os`
- `PyPDF2`
- `python-dotenv`
- `langchain`
- `openai`
- `azure-ai-ml` (if needed for Azure integration)

---

##  How to Run

1. **Clone the repository**
    ```bash
    git clone https://github.com/dharm1123/Resume_Ranker_App_GenAI-App.git
    cd Resume_Ranker_App_GenAI-App
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**

    - Create a `.env` file in the root directory with the following content:
        ```
        AZURE_OPENAI_API_BASE=your_azure_openai_endpoint
        AZURE_OPENAI_API_VERSION=your_api_version
        AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
        AZURE_OPENAI_API_KEY=your_api_key
        ```

4. **Run the app**
    ```bash
    streamlit run app.py
    ```

5. **Open in Browser**

    - After running, Streamlit will provide a local URL (usually http://localhost:8501/). Open this in your browser to use the app.

---

## File Structure

```
Resume_Ranker_App_GenAI-App/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── ...
```

---

## Author

**DHARM DUDHAGARA**  
[GitHub Profile](https://github.com/dharm1123)

---

## Contributors

- [DHARM DUDHAGARA](https://github.com/dharm1123)
- [Devangi Shingala](https://github.com/devangishingala)

---
## Contact

For suggestions, issues, or feature requests, please use the [GitHub Issues](https://github.com/dharm1123/Resume_Ranker_App_GenAI-App/issues) page.

---
