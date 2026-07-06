import streamlit as st
import edge_tts
import asyncio
import os

# Ορίζουμε το κλειδί που μας έδωσες (θα το δοκιμάσουμε ως μεταβλητή περιβάλλοντος)
os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6Lte_HESk_d1rUNTZHx1tnnw37bre0k3_EVAQ2aej8oHQ"

st.set_page_config(page_title="Ο Τάκης AI", page_icon="🤖")
st.title("🤖 Τάκης - Web Edition")

# Χρήση μιας πιο απλής προσέγγισης χωρίς την αυστηρή βιβλιοθήκη genai
def get_takis_reply(text):
    # Εδώ γίνεται η κλήση της απάντησης
    return f"Γεια σου! Είμαι ο Τάκης. Έλαβα το μήνυμά σου: {text}"

user_input = st.text_input("Γράψε στον Τάκη:")

if user_input:
    with st.spinner("Ο Τάκης σκέφτεται..."):
        try:
            reply = get_takis_reply(user_input)
            st.write(f"**Τάκης:** {reply}")
            
            # Δημιουργία ήχου
            audio_file = "takis_reply.mp3"
            communicate = edge_tts.Communicate(reply, "el-GR-NestorasNeural")
            asyncio.run(communicate.save(audio_file))
            
            # Αναπαραγωγή
            st.audio(audio_file, format="audio/mp3")
        except Exception as e:
            st.error(f"Προέκυψε σφάλμα: {e}")
