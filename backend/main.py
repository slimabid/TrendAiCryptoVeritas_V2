from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from veritas import get_reddit_data, get_community_stance, get_input_direction, check_truth, is_bot_attack, calculate_granular_risk

app = FastAPI(title="TrendAI Final")

# Enable CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_input(query: str):
    # 1. Fetch
    posts = await get_reddit_data(query, limit=100)
    if not posts: return {"error": "No data found"}
    
    # 2. Analyze
    input_dir = get_input_direction(query)
    comm_side = get_community_stance(posts)
    is_bot = is_bot_attack(posts)
    
    # 3. Truth Check
    truth_status = "SKIPPED"
    if any(w in query.lower() for w in ["apple", "amazon", "official", "news"]):
        truth_status = check_truth(query)
    
    # 4. Calc Score
    final_score = calculate_granular_risk(posts, truth_status)
    
    # 5. Result String
    comm_clean = comm_side.replace(" 🟢", "").replace(" 🔴", "").replace(" ⚪", "")
    result = "Neutral Market"
    if input_dir == "NEUTRAL": result = f"Market Sentiment is {comm_clean}"
    elif input_dir == comm_clean: result = f"✅ MARKET CONSENSUS"
    else: result = f"⚠️ MARKET DIVERGENCE"

    # 6. Verdict
    verdict = "SAFE / ORGANIC"
    if is_bot: 
        verdict = "🚨 CRITICAL: BOT ATTACK"
        final_score = 99
    elif truth_status == "UNVERIFIED":
        verdict = "⚠️ SUSPICIOUS: UNVERIFIED RUMOR"
    elif final_score > 65:
        verdict = "⚠️ HIGH VOLATILITY / HYPE"
    elif input_dir == "BEARISH":
        verdict = "📉 BEARISH PREDICTION"
    elif input_dir == "BULLISH":
        verdict = "📈 BULLISH PREDICTION"

    return {
        "verdict": verdict,
        "risk_score": final_score,
        "community_stance": comm_side,
        "result": result,
        "posts": posts[:50]
    }