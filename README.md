# 🔐 CipherAudit — Advanced Password Strength Evaluator

**CipherAudit** is a privacy-focused, backend-powered password strength checker built using **Flask**. Unlike typical tools that rely only on regex or visual UI gimmicks, CipherAudit dives deep into **entropy**, **real-world password breaches**, and **pattern-based weaknesses** to assess how secure your password really is.

> ✅ Built for developers, security learners, and curious users who care about real password safety — not just red/green bars.

## 🌟 Key Features

- 🔢 **Entropy-Based Scoring**  
  Uses Shannon entropy to estimate how random and unpredictable the password is.

- ⚠️ **Pwned Password Check**  
  Integrates with [Have I Been Pwned](https://haveibeenpwned.com/API/v3) API to detect if your password has ever been leaked in real-world data breaches.

- 📚 **Pattern File Detection**  
  Compares passwords against multiple preloaded pattern files including:
  - Common passwords  
  - Dictionary words  
  - Keyboard sequences (e.g., `qwerty`, `12345`)  
  - Repeated characters  
  - Known weak structures  

- ⏱️ **Crack Time Estimation**  
  Predicts how long it would take to brute-force the password using current computing power.

- 🎯 **Score & Verdict**  
  Gives a final verdict with color-coded messages and score (out of 10).

- 🧠 **Clean UI with Flask + Bootstrap**  
  Easy to use, responsive UI — no JavaScript required.

## 🧰 Tools & Technologies

| Tech         | Purpose                                      |
|--------------|----------------------------------------------|
| Python 3.12+ | Core logic and backend                       |
| Flask        | Lightweight web framework                    |
| HTML/CSS     | Frontend templating via Jinja2               |
| Bootstrap    | Responsive styling                           |
| SHA-1        | Secure API query via K-Anonymity (HIBP)      |
| File I/O     | Loading and comparing pattern sets           |
| `requests`   | HTTP requests to HaveIBeenPwned API          |

## 🚀 Live Preview (Optional)

If deployed, link your site here:

> 🔗 https://cipheraudit.yourdomain.com *(Example)*


## 📦 Getting Started Locally

```bash
# 1. Clone this repo
git clone https://github.com/Laiba-muzammal/CipherAudit.git
cd CipherAudit

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python main.py

# Visit: http://127.0.0.1:5000
🛡️ How CipherAudit Stands Out
Feature	Basic Checkers ❌	CipherAudit ✅
Entropy Calculation	❌	✅
Pwned Password Check (HIBP)	❌	✅
Pattern File Matching	❌	✅
Crack Time Prediction	❌	✅
Flask Blueprint Architecture	❌	✅
Security-Oriented Design	❌	✅
Rate Limiting (Optional)	❌	✅
Ready for API Extension	❌	✅

💡 Most password checkers just show a red or green bar. CipherAudit gives a real-world risk evaluation backed by data and backend logic.

📁 Project Structure
csharp
CipherAudit/
│
├── main.py                    # Entry point
├── pass_checker/
│   ├── __init__.py            # App factory (if used)
│   ├── routes.py              # All logic & route handling
│   └── patterns/              # Pattern files (.txt)
│
├── templates/
│   ├── home.html              # Main input form
│   └── response.html          # Results page
│
├── static/
│   └── style.css              # Custom styling
│
├── requirements.txt
└── README.md

📜 License
This project is under the MIT License.

🤝 Contribute
Have an idea to improve CipherAudit? Feel free to fork the repo and submit a pull request.

🧠 Made by
Laiba Muzammal
Backend Developer | Flask Enthusiast
📬 LinkedIn • GitHub
