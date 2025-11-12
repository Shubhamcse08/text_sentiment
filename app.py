import streamlit as st
from utils import analyze_sentiment

st.title("Sentiment Analysis App")
st.write("Enter text below to analyze its sentiment:")

user_input = st.text_area("Enter Text", "")

if st.button("Analyze"):
    if user_input.strip():
        result = analyze_sentiment(user_input)
        st.markdown(f"""
        <p><b>Sentiment:</b> {result['sentiment']}</p>
        <p><b>Compound:</b> {result['compound']}</p>
        <p><b>Positive:</b> {result['pos']}</p>
        <p><b>Neutral:</b> {result['neu']}</p>
        <p><b>Negative:</b> {result['neg']}</p>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please enter some text to analyze.")
