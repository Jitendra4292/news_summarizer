import streamlit as st
from newspaper import Article
from textblob import TextBlob
from transformers import pipeline
import re

st.title("📰 Personal News Summarizer & Sentiment Tracker")

# Function to clean article text
def clean_text(text):
    # Replace multiple spaces/newlines with single space
    text = re.sub(r'\s+', ' ', text)
    # Strip leading/trailing spaces
    return text.strip()

# Input the news article URL
url = st.text_input("Enter a news article URL:")

@st.cache_resource(show_spinner=True)
def load_summarizer():
    # Use distilbart model for faster load and lighter computation
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return summarizer

summarizer = load_summarizer()

if url:
    article = Article(url)
    try:
        article.download()
        article.parse()
        title = article.title
        raw_text = article.text

        # Clean article text for better summaries
        text = clean_text(raw_text)

        st.subheader(title)
        st.write(text)

        # Summarize the article (limit input length for model constraints)
        max_input_length = 1000
        if len(text) > max_input_length:
            input_text = text[:max_input_length]
        else:
            input_text = text

        summary_result = summarizer(
            input_text, max_length=180, min_length=80, do_sample=False
        )
        summary_text = summary_result[0]['summary_text']

        st.markdown("### Summary:")
        st.write(summary_text)

        # Sentiment analysis
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            st.success(f"Sentiment: Positive (score = {polarity:.2f})")
        elif polarity == 0:
            st.info(f"Sentiment: Neutral (score = {polarity:.2f})")
        else:
            st.error(f"Sentiment: Negative (score = {polarity:.2f})")

    except Exception as e:
        st.error(f"Error fetching or parsing the article: {e}")
