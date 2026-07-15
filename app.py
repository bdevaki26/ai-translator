import streamlit as st
from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

st.title("🌍 AI Translator")
st.write("Translate any text and keep the tone")

text = st.text_area("Enter text to translate:", height=150)

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", ["Auto Detect", "English", "Hindi", "Telugu", "Tamil"])
with col2:
    target_lang = st.selectbox("Target Language", ["Hindi", "English", "Telugu", "Tamil", "Spanish"])

tone = st.selectbox("Tone", ["Neutral", "Formal", "Casual", "Professional"])

if st.button("Translate"):
    if text:
        prompt = f"Translate this from {source_lang} to {target_lang} in a {tone.lower()} tone. Only give translation.\n\nText: {text}"
        response = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.1-8b-instant")
        st.subheader("Translated Text:")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter text first")