import streamlit as st
import google.generativeai as genai
import edge_tts
import asyncio
import os

# Ρύθμιση σελίδας
st.set_page_config(page_title="Ο Τάκης AI", page_icon="🤖")
st.title("🤖 Τάκης - Web Edition")

# Το κλειδί μας απευθείας στον κώδικα
API_KEY = "AQ.Ab8RN6IWzf1ZUaUqq2mIZTvil9ii8SlDu-9ersvDZ3IJpNsMJA"

# Ρύθμιση του Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Πεδίο κειμένου
user_input = st.text_input("Γράψε στον Τάκη:")

if user_input:
    with st.spinner("Ο Τάκης σκέφτεται..."):
        try:
            # Απάντηση από Gemini
            response = st.session_state.chat.send_message(user_input)
            reply = response.text
            
            st.write(f"**Τάκης:** {reply}")
            
            # Δημιουργία ήχου
            audio_file = "takis_reply.mp3"
            communicate = edge_tts.Communicate(reply, "el-GR-NestorasNeural")
            asyncio.run(communicate.save(audio_file))
            
            # Αναπαραγωγή
            st.audio(audio_file, format="audio/mp3")
        except Exception as e:
            st.error(f"Κάτι πήγε στραβά: {e}")
