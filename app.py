import streamlit as st
import asyncio
from google import genai
from google.genai import types
import edge_tts
import os

# Ρύθμιση σελίδας
st.set_page_config(page_title="Ο Τάκης AI", page_icon="🤖")

st.title("🤖 Τάκης - Web Edition")

# Το API Key σου
API_KEY = "AQ.Ab8RN6IWzf1ZUaUqq2mIZTvil9ii8SlDu-9ersvDZ3IJpNsMJA"
client = genai.Client(api_key=API_KEY)

# Chat setup
if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="Είσαι ο Τάκης, ένας μάγκας AI βοηθός. Απαντάς σύντομα στα ελληνικά."
        )
    )

# Πεδίο κειμένου
user_input = st.text_input("Γράψε στον Τάκη:")

if user_input:
    with st.spinner("Ο Τάκης σκέφτεται..."):
        # Απάντηση από Gemini
        response = st.session_state.chat.send_message(user_input)
        reply = response.text
        
        st.write(f"**Τάκης:** {reply}")
        
        # Δημιουργία ήχου
        audio_file = "takis_reply.mp3"
        communicate = edge_tts.Communicate(reply, "el-GR-NestorasNeural")
        asyncio.run(communicate.save(audio_file))
        
        # Αναπαραγωγή
        audio_file = open(audio_file, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)

st.info("Τώρα ο Τάκης τρέχει στον server και τον ανοίγεις από το κινητό!")
