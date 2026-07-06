import streamlit as st
import google.generativeai as genai
import edge_tts
import asyncio
import os

st.set_page_config(page_title="Ο Τάκης AI", page_icon="🤖")
st.title("🤖 Τάκης - Web Edition")

# Εδώ δεν θα βάλουμε API_KEY
# Θα δοκιμάσουμε να τρέξουμε το μοντέλο μέσω της δωρεάν πρόσβασης του Streamlit
# Αν σου βγάλει σφάλμα, σημαίνει ότι το Streamlit δεν επιτρέπει δωρεάν κλήσεις χωρίς κλειδί.

try:
    # Δοκιμή χωρίς key
    model = genai.GenerativeModel("gemini-1.5-flash")
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])

    user_input = st.text_input("Γράψε στον Τάκη:")

    if user_input:
        with st.spinner("Ο Τάκης σκέφτεται..."):
            response = st.session_state.chat.send_message(user_input)
            st.write(f"**Τάκης:** {response.text}")
            
            audio_file = "takis_reply.mp3"
            communicate = edge_tts.Communicate(response.text, "el-GR-NestorasNeural")
            asyncio.run(communicate.save(audio_file))
            st.audio(audio_file, format="audio/mp3")
except Exception as e:
    st.write("Συγνώμη, το Google Gemini απαιτεί κλειδί AIza για να λειτουργήσει.")
    st.write("Αν δεν μπορείς να βγάλεις AIza κλειδί, η μόνη άλλη λύση είναι να χρησιμοποιήσουμε άλλο μοντέλο (π.χ. OpenAI ή HuggingFace).")
