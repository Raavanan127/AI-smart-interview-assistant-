# AI-smart-interview-assistant-
import streamlit as st
from ai_modules.speech_to_text import record_answer
from ai_modules.nlp_analysis import analyze_text
from ai_modules.emotion_detection import detect_emotion
from ai_modules.voice_analysis import voice_confidence
from ai_modules.interviewer_ai import next_question
from ui.dashboard import show_dashboard

st.title("🚀 Advanced AI Interview Assistant")

if "question" not in st.session_state:
    st.session_state.question = next_question()

st.subheader("Question:")
st.write(st.session_state.question)

if st.button("🎤 Start Answer"):
    answer = record_answer()

    result = analyze_text(answer)
    emotion = detect_emotion()
    voice_level = voice_confidence(answer)

    show_dashboard(answer, result["score"], emotion, voice_level)

    st.session_state.question = next_question()