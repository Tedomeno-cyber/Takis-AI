import streamlit as st
import google.generativeai as genai
import edge_tts
import asyncio
import os

# Ρύθμιση σελίδας
st.set_page_config(page_title="Ο Τάκης AI", page_icon="🤖")
st.title("🤖 Τάκης - Web Edition")

# Το κλειδί μας
API_KEY = "AQ.Ab8RN6LHFJgvc-sJQwqVB6ZllKX8EL-HhRuH5xkp-rsNCFXi2g"

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
            
            # Αναπαραγωγή ήχου
            st.audio(audio_file, format="audio/mp3")
            
        except Exception as e:
            st.error(f"Κάτι πήγε στραβά με το κλειδί ή τη σύνδεση: {e}")
            st.write("Σημείωση: Αν το σφάλμα επιμένει, ίσως το κλειδί χρειάζεται ανανέωση από το Google AI Studio.")
