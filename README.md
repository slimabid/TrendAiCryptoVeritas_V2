# 🛡️ TrendAI: Veritas Protocol

**A Real-Time Market Surveillance & Narrative Verification Engine.**

TrendAI is a full-stack intelligence dashboard that detects crypto bot attacks, quantifies "hype," and verifies market rumors against trusted news sources in real-time.

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Tech Stack](https://img.shields.io/badge/Stack-FastAPI%20%7C%20React-blue)

## 🚀 Features
- **Bot Attack Detection:** Analyzes author-to-post ratios to flag coordinated manipulation.
- **Narrative Verification:** Cross-references social claims with trusted financial news (Bloomberg, SEC, Reuters).
- **Sentiment DNA:** Visualizes the "mood" of the market using a 100-post heat map.
- **Risk Scoring:** Assigns a 0-100 risk score based on hype, bot activity, and news verification.

---

## 🛠️ Installation & Setup

This project uses a **Python Backend** and a **React Frontend**. You need to run both simultaneously.

### 1. Backend Setup (Python)
Open your **first terminal** and run:

```bash
# Go to the backend folder
cd backend

# Install the AI & API libraries
pip install fastapi uvicorn textblob httpx duckduckgo-search

# Start the Intelligence Engine
uvicorn main:app --reload
> The backend is now running on http://127.0.0.1:8000

2. Frontend Setup (React)
Open a second terminal (keep the first one running!) and run:

Bash

# Go to the frontend folder
cd frontend

# Install dependencies (only needs to be done once)
npm install

# Launch the Dashboard
npm run dev
> The dashboard is now accessible at http://localhost:5173

🖥️ How to Use
Open the Localhost URL shown in your second terminal (usually http://localhost:5173).

Type a coin or topic in the search bar (e.g., "Bitcoin", "PEPE", "ETF Approval").

Hit Enter or click SCAN.

View the Risk Score, Verdict, and Live Feed instantly.

📂 Project Structure
Plaintext

TrendAI-Veritas/
├── backend/            # Python FastAPI Server
│   ├── main.py         # API Endpoints
│   └── veritas.py      # Logic (Sentiment, Bots, Search)
│
├── frontend/           # React Dashboard
│   ├── src/
│   │   ├── App.jsx     # Main UI Logic
│   │   └── App.css     # Cyberpunk Styling
│   └── package.json    # React Dependencies
│
└── README.md           # Documentation
⚠️ Troubleshooting
"Fetch Error"? → Make sure the Python terminal is running and says "Application startup complete".

"Vite not found"? → Run npm install inside the frontend folder again.

Layout issues? → Refresh the page; the CSS is designed to auto-center on any screen.


### **How to Upload This:**
1.  Save the file as **`README.md`**.
2.  Run: `git add README.md`
3.  Run: `git commit -m "Add professional documentation"`
4.  Run: `git push origin main`

Now check your GitHub repo—it will look like a serious open-source tool!