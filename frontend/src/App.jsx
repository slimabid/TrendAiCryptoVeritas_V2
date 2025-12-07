import React, { useState } from 'react';
import './App.css'; // Make sure this import is here!

export default function App() {
  const [query, setQuery] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const analyze = async () => {
    if(!query) return;
    setLoading(true);
    setError(null);
    setData(null);

    try {
      const res = await fetch(`http://127.0.0.1:8000/analyze?query=${query}`, {
        method: "POST"
      });
      const result = await res.json();
      if(result.error) throw new Error(result.error);
      setData(result);
    } catch (e) {
      setError("Cannot connect to Backend (Port 8000)");
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      
      {/* 1. HEADER */}
      <div className="header">
        <h1 className="logo">Trend<span>AI</span></h1>
        <p className="subtitle">Veritas Protocol Online</p>
      </div>

      {/* 2. SEARCH */}
      <div className="search-box-wrapper">
        <input 
          className="search-input"
          placeholder="Analyze a narrative..." 
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && analyze()}
        />
        <button className="search-btn" onClick={analyze} disabled={loading}>
          {loading ? "..." : "SCAN"}
        </button>
      </div>

      {error && <p style={{color: '#ef4444', marginTop: '20px'}}>{error}</p>}

      {/* 3. DASHBOARD */}
      {data && (
        <div className="dashboard-grid">
          
          {/* Verdict */}
          <div className="card highlight">
            <div className="card-title">Verdict</div>
            <div className="big-text" style={{color: data.risk_score > 50 ? '#ef4444' : '#10b981'}}>
              {data.verdict}
            </div>
            <p style={{color: '#cbd5e1', marginTop: '10px'}}>{data.result}</p>
          </div>

          {/* Risk Score */}
          <div className="card">
            <div className="card-title">Risk Score</div>
            <div className="big-text" style={{color: 'white'}}>
              {data.risk_score}
            </div>
          </div>

          {/* Sentiment */}
          <div className="card">
            <div className="card-title">Sentiment</div>
            <div className="big-text">
               {data.community_stance.includes("BULL") ? "🚀" : data.community_stance.includes("BEAR") ? "📉" : "⚖️"}
            </div>
            <div style={{color: '#cbd5e1', fontWeight: 'bold', marginTop: '5px'}}>
              {data.community_stance.replace(/🟢|🔴|⚪/g, "")}
            </div>
          </div>

          {/* Heatmap (Full Width) */}
          <div className="full-width-card">
            <div className="card-title" style={{textAlign: 'left'}}>Sentiment DNA (100 Posts)</div>
            <div className="heatmap">
               {data.posts.map((post, i) => {
                 const height = Math.max(15, Math.abs(post.sentiment || 0) * 100);
                 const color = (post.sentiment || 0) > 0 ? '#10b981' : (post.sentiment || 0) < 0 ? '#ef4444' : '#475569';
                 return (
                   <div 
                    key={i} 
                    className="heat-bar" 
                    style={{ height: `${height}%`, backgroundColor: color }}
                    title={post.title}
                   ></div>
                 )
               }).reverse()}
            </div>
          </div>

        </div>
      )}
    </div>
  );
}