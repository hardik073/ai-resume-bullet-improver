# AI Resume Bullet Improver

A simple Python CLI tool that uses OpenAI's LLM to rewrite resume bullet points into strong, achievement-oriented statements.

## 🚀 Features

- Rewrites resume bullet points
- Makes them impact-focused
- Uses measurable language when possible
- Clean CLI interface
- Secure API key handling via environment variables

---

## 🛠 Tech Stack

- Python 3.9+
- OpenAI API
- Virtual Environment (venv)

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
https://github.com/hardik073/ai-resume-bullet-improver.git
cd ai-resume-bullet-improver
```
### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate #Windows
```

### Set Environment Variable
```bash
Mac/Linux:
export OPENAI_API_KEY="your-api-key-here"

Windows (PowerShell):
setx OPENAI_API_KEY "your-api-key-here"
```

⚠️ Never hardcode your API key in the source code.

### ▶️ Run the App
```
python main.py
```
