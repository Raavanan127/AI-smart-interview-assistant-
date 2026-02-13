import streamlit as st

def show_dashboard(answer, score, emotion, voice_level):
    st.subheader("📊 Interview Analysis Report")
    st.write("Answer:", answer)
    st.metric("AI Score", score)
    st.write("Emotion:", emotion)
    st.write("Voice Confidence:", voice_level)