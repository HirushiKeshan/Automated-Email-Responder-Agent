# 📬 Automated Email Responder Agent 🤖

An intelligent email-processing agent that reads unread Gmail messages, classifies them into relevant categories using a Gemini LLM, drafts appropriate and professional replies, and allows refinement of those replies based on user feedback — all automated with clean, scalable Python code.

---

## 🚀 Features

✅ Reads unread emails from Gmail (via Gmail API)  
✅ Classifies emails into categories like `Job Inquiry`, `Meeting Request`, `Support Query`, `Spam`, etc.  
✅ Generates polite, context-aware replies using Gemini Pro/Flash  
✅ Accepts user feedback to improve and refine replies  
✅ Modular and scalable design with best practices  
✅ Environment variable management using `.env`  
✅ Clear CLI interaction with error handling  

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Google Gemini Pro / Gemini Flash**
- **LangChain**
- **Gmail API** via `google-api-python-client`
- **OAuth2** for Gmail Authentication
- **dotenv** for environment management

---


## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/HirushiKeshan/Automated-email-Responder-Agent.git
cd Automated-email-Responder-Agent
```
### 2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4.Set up environment variables
Create a .env file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key
EMAIL_ID=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password

```
### 5.Gmail API Setup Guide
```
1.Go to the Google Cloud Console.

2.Create a new project or select an existing one.

3.Enable Gmail API for the project.

4.Go to Credentials, click Create Credentials → OAuth Client ID

5.Download the credentials.json and place it in the root directory.

6.When you run the app, it will prompt to authenticate and save a token.json.
```
### 6.Running the Agent
```
python main.py

