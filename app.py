import streamlit as st
from transformers import pipeline

st.title("My First AI App")
text = st.text_input("Type something:")
if text:
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)[0]
    st.write(f"Sentiment: {result['label']}, Score: {result['score']:.2f}")