#  ResuBot — AI Resume Chatbot for Drashti Shah

ResuBot is an **AI-powered chatbot** that interactively answers questions about **Drashti Shah’s resume**, such as her skills, projects, education, and experience.  
It uses **Python, Flask, and spaCy** to process questions and respond conversationally.

---

##  What It Does
- Answers questions like:
  - “What are Drashti’s projects?”
  - “Where does she study?”
  - “Tell me about her technical skills.”
- Uses pre-defined intent data (`intents.json`, `responses.csv`)
- Built with modular folders for **frontend**, **backend**, **NLP**, and **infrastructure**

---

##  Technologies
- **Backend:** Flask (Python)  
- **NLP / ML:** spaCy, scikit-learn, pandas  
- **Database:** MongoDB *(for future dynamic data)*  
- **Cloud (optional):** AWS SageMaker  
- **Tools:** Git, VS Code

---

## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/resubot.git
   cd resubot
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/Scripts/activate  # or venv/bin/activate for Mac/Linux
3. Install dependencies:
   pip install -r infra/requirements.txt
