import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import random

# --- SIMULATED TRAINED MODEL ---
# Since we cannot train a model right now, we use a simple, pre-defined TF-IDF 
# vectorizer and a Logistic Regression pipeline for demonstration.

# 1. SIMULATED VOCABULARY: The model needs to know the words it learned.
# In a real project, this would be saved after training.
SIMULATED_VOCAB = [
    "pump", "moon", "bullish", "buy", "long", "good", "great", "win", 
    "bearish", "dump", "crash", "sell", "short", "bad", "scam", "down", 
    "neutral", "hold", "wait", "stable"
]

# 2. SIMULATED PREPROCESSOR: Prepares text for the model.
def clean_text(text):
    text = text.lower()
    # Remove special characters and clean up
    text = re.sub(r'[^a-z\s]', '', text) 
    return text.strip()

# 3. SIMULATED MODEL LOAD: Creates a simple TF-IDF pipeline.
# We are demonstrating the pipeline structure, which is the core ML concept here.
def load_sentiment_pipeline():
    # A real model would be loaded from a serialized file (e.g., pickle file)
    
    # Create a vectorizer (the feature extractor) trained on the simulated vocab
    vectorizer = TfidfVectorizer(vocabulary=SIMULATED_VOCAB)
    
    # Create a simple Logistic Regression model (the classifier)
    # This is the actual machine learning algorithm used for prediction
    classifier = LogisticRegression(random_state=42)
    
    # Combine feature extraction and classification into a pipeline
    model_pipeline = Pipeline([
        ('vectorizer', vectorizer),
        ('classifier', classifier)
    ])
    
    # Simulate a prediction function
    def predict_sentiment(text):
        cleaned_text = clean_text(text)
        
        # --- ML Classification Simulation ---
        # The following logic simulates a prediction from the trained model.
        # In a real scenario, we'd use model_pipeline.predict()
        if "pump" in cleaned_text or "moon" in cleaned_text or "buy" in cleaned_text:
            return random.uniform(0.6, 0.95) # Strongly positive prediction
        if "crash" in cleaned_text or "dump" in cleaned_text or "sell" in cleaned_text:
            return random.uniform(-0.95, -0.6) # Strongly negative prediction
        return random.uniform(-0.1, 0.1) # Neutral prediction
        
    return predict_sentiment

# Load the function once
SENTIMENT_PREDICTOR = load_sentiment_pipeline()