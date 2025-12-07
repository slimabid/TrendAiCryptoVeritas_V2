import httpx
from duckduckgo_search import DDGS
from ml_model import SENTIMENT_PREDICTOR # IMPORT THE ML MODEL

# --- 1. GET DATA (ML-Powered Sentiment) ---
async def get_reddit_data(topic: str, limit=100):
    url = f"https://www.reddit.com/search.json?q={topic}&sort=new&limit={limit}"
    headers = {"User-Agent": "Mozilla/5.0"}
    posts = []
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, headers=headers, follow_redirects=True, timeout=10.0)
            if resp.status_code == 200:
                for item in resp.json()['data']['children']:
                    p = item['data']
                    
                    # Calculate sentiment using the ML-Powered Predictor
                    title = p.get('title', '')
                    sentiment = SENTIMENT_PREDICTOR(title)
                    
                    posts.append({
                        "title": p.get('title'),
                        "author": p.get('author', 'unknown'),
                        "timestamp": p.get('created_utc'),
                        "sentiment": sentiment, # NOW uses the ML prediction
                        "url": f"https://reddit.com{p.get('permalink')}"
                    })
        except: pass
    return posts

# --- 2. GET INPUT DIRECTION (No changes) ---
def get_input_direction(text):
    text = text.lower()
    words = text.split()
    down_words = ["fall", "crash", "dump", "bear", "drop", "sell", "short", "dead", "tank"]
    up_words = ["rise", "moon", "pump", "bull", "buy", "long", "up", "high", "soar"]
    negations = ["not", "no", "won't", "never", "dont", "cant"]
    score = 0
    for i, word in enumerate(words):
        if word in down_words:
            if i > 0 and words[i-1] in negations: score += 1
            else: score -= 1
        if word in up_words:
            if i > 0 and words[i-1] in negations: score -= 1
            else: score += 1
    if score > 0: return "BULLISH"
    if score < 0: return "BEARISH"
    return "NEUTRAL"

# --- 3. GET COMMUNITY STANCE (Predictive Thresholding) ---
def get_community_stance(posts):
    if not posts: return "NEUTRAL ⚪"
    
    scores = [p['sentiment'] for p in posts]
    avg = sum(scores) / len(scores)
    
    # Calculate the AVERAGE ABSOLUTE DEVIATION (Intensity)
    intensity = sum(abs(s) for s in scores) / len(scores) 
    
    # Dynamic threshold based on current intensity
    threshold = intensity * 0.5 
    
    if avg > threshold: 
        return "BULLISH 🟢"
    
    if avg < (threshold * -1): 
        return "BEARISH 🔴"
        
    return "NEUTRAL ⚪"

# --- 4. CHECK TRUTH (No changes) ---
def check_truth(topic):
    try:
        results = DDGS().text(f"{topic} official news finance", max_results=5)
        trusted = ['bloomberg', 'reuters', 'coindesk', 'wsj', 'official', 'sec.gov']
        for r in results:
            if any(t in r['href'] for t in trusted): return "VERIFIED"
        return "UNVERIFIED"
    except: return "ERROR"

# --- 5. CHECK BOTS (No changes) ---
def is_bot_attack(posts):
    if not posts: return False
    unique = set([p['author'] for p in posts])
    if len(posts) > 15 and (len(unique) / len(posts)) < 0.5: return True
    return False

# --- 6. CALCULATE RISK (No changes) ---
def calculate_granular_risk(posts, truth_status="SKIPPED"):
    if not posts: return 0
    
    unique_count = len(set([p['author'] for p in posts]))
    ratio = unique_count / len(posts)
    bot_risk = (1.0 - ratio) * 100 
    
    scores = [abs(p['sentiment']) for p in posts]
    hype_risk = (sum(scores) / len(scores)) * 20 
    
    truth_risk = 40 if truth_status == "UNVERIFIED" else 0
    
    return int(min(bot_risk + hype_risk + truth_risk, 99))