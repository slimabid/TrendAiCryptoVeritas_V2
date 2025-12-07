# 🛡️ TrendAI: Veritas Protocol

## A Full-Stack Financial Intelligence Engine

**TrendAI** is a robust, AI-powered solution engineered to combat social media manipulation and quantify investment risk in real-time. This project demonstrates proficiency in asynchronous API design, supervised ML deployment, and performance-optimized React UI development.

---

## 🚀 Core Features & ML Integration

| Component | Technology | Innovation |
| :--- | :--- | :--- |
| **Sentiment Analysis** | **Logistic Regression ML Pipeline** | Replaced heuristic scoring with a **true supervised classifier** for accurate, pattern-based prediction. |
| **System Alerts** | **Dynamic Predictive Thresholding** | Alert levels (BULLISH/BEARISH) adapt automatically based on the statistical **intensity of current market volatility**. |
| **Risk Scoring** | **Composite Algorithm** | Combines ML sentiment volatility, bot detection heuristics, and news verification checks into a single **0-99 Risk Score**. |
| **Frontend** | **React / Custom CSS3** | Clean, centered "Fintech Cyberpunk" dashboard for stable, high-performance data visualization. |

---

## 🛠️ Installation & Setup

This project requires a **Python Backend** and a **React Frontend** running simultaneously in two separate terminal windows.

### 1. Backend Setup (Python)

The backend runs the core Intelligence Engine and the ML model.

1.  Open your **first terminal** and navigate to the **`backend`** folder.
2.  Install all required libraries (FastAPI, Scikit-learn, etc.):
    ```bash
    pip install -r requirements.txt
    ```
3.  **Start the Intelligence Engine:**
    ```bash
    uvicorn main:app --reload
    ```
    ⚠️ *(Keep this terminal open! The engine is running at `http://127.0.0.1:8000`)*

---

### 2. Frontend Setup (React)

The frontend runs the visualization dashboard.

1.  Open a **second terminal window** and navigate to the **`frontend`** folder.
2.  Install JavaScript dependencies (React, etc.):
    ```bash
    npm install
    ```
3.  **Launch the Dashboard:**
    ```bash
    npm run dev
    ```
    🖥️ *(The dashboard URL will open in your browser, usually `http://localhost:5173`)*

---

## 🧪 How to Use & Test the ML System

Open the Localhost URL shown in your second terminal.

* **To test ML Sentiment:** Submit a query containing terms the model was trained on (e.g., **"Bitcoin pump moon to $100k"** or **"stock market crash dump sell"**). The **Sentiment DNA** heatmap will react immediately based on the **ML prediction scores**.

* **To test Verification:** Submit a phrase like **"Apple news official"** to see the system check against authoritative domains and apply a risk penalty if unverified.

---

## 📂 Project Structure

```text
TrendAI-Veritas/
├── backend/            # Python FastAPI Server (ML Execution)
│   ├── main.py         # API Endpoints
│   ├── veritas.py      # Core Logic & ML Integration
│   ├── ml_model.py     # Logistic Regression Pipeline (The Classifier)
│   └── requirements.txt# All Python Dependencies (ML/API)
│
├── frontend/           # React Dashboard (UI)
│   ├── src/            # JavaScript Components & Custom CSS
│   └── package.json    # React Dependencies
│
└── README.md           # Documentation