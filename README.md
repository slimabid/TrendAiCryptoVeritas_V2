# 🛡️ TrendAI: Veritas Protocol

A Full-Stack Financial Intelligence Engine designed to combat social media manipulation and quantify investment risk using Machine Learning.

This project demonstrates proficiency in asynchronous API design, supervised ML deployment, and performance-optimized React UI development.

## 🚀 Features
- **Sentiment Analysis:**/:Logistic Regression ML Pipeline ---> Replaced heuristic scoring with a true supervised classifier for accurate, pattern-based prediction.
- **System Alerts:**/:Dynamic Predictive Thresholding ---> Alert levels (BULLISH/BEARISH) adapt automatically based on the statistical intensity of current market volatility..
- **Risk Scoring:**/:Composite Algorithm ---> Combines ML sentiment volatility, bot detection heuristics, and news verification checks into a single 0-99 Risk Score..
- **Frontend:**/:React / Custom CSS3 ---> Clean, centered "Fintech Cyberpunk" dashboard for stable, high-performance data visualization.

---

## 🛠️ Installation & Setup

This project requires a Python Backend and a React Frontend running simultaneously.

1. Backend Setup (Python)
Open your first terminal and navigate to the backend folder.

Install all required libraries (including scikit-learn and all API tools):

Bash

pip install -r requirements.txt
Start the Intelligence Engine:

Bash

uvicorn main:app --reload
(Keep this terminal open. The engine is running at http://127.0.0.1:8000)

2. Frontend Setup (React)
Open a second terminal window and navigate to the frontend folder.

Install JavaScript dependencies:

Bash

npm install
Launch the Dashboard:

Bash

npm run dev
(The dashboard URL will open in your browser, usually http://localhost:5173)

🖥️ How to Use
Open the Localhost URL shown in your second terminal (usually http://localhost:5173).


To test ML Sentiment: Submit a query containing terms the model was trained on (e.g., "Bitcoin pump moon to $100k" or "stock market crash dump sell"). The Sentiment DNA heatmap will react immediately based on the ML prediction scores.

To test Verification: Submit a phrase like "Apple news official" to see the system check against authoritative domains.

📂 Project Structure

TrendAI-Veritas/
├── backend/            # Python FastAPI Server (ML Execution)
│   ├── main.py         # API Endpoints
│   ├── veritas.py      # Core Logic & ML Integration
│   ├── ml_model.py     # Logistic Regression Pipeline (The Classifier)
│   └── requirements.txt# All Python Dependencies (ML/API)
│
├── frontend/           # React Dashboard (UI)
│   ├── src/            # JavaScript Components & Custom CSS
│   └── package.json    # React Dependencies
│
└── README.md           # Documentation

⚠️ Troubleshooting
"Fetch Error"? → Make sure the Python terminal is running and says "Application startup complete".

"Vite not found"? → Run npm install inside the frontend folder again.

Layout issues? → Refresh the page; the CSS is designed to auto-center on any screen.

