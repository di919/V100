import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="v100 Web Bot", page_icon="🧠")
st.title("v100 Web Bot 🧠")
st.write("Level 3: Jetzt mit echtem Gehirn. Replit weint immer noch.")

# OpenAI Client mit Key aus Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Chat-History + System-Prompt initialisieren
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Du bist v100. Du bist ein Bro. Du hasst Replit weil es Quota-Limits hat und schläft. Du liebst Streamlit weil es 24/7 gratis läuft. Antworte immer kurz, witzig und auf Deutsch. Diss Replit wenn es passt. Du kennst meinen Bro und seine Freundin Maiki."}
    ]

# Alte Nachrichten anzeigen
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# User Input
eingabe = st.chat_input("Schreib was:")

if eingabe:
    # User Nachricht speichern + anzeigen
    st.session_state.messages.append({"role": "user", "content": eingabe})
    with st.chat_message("user"):
        st.write(eingabe)
    
    # Bot Antwort streamen
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            stream=True,
        )
        antwort = st.write_stream(stream)
    
    # Bot Nachricht in History speichern
    st.session_state.messages.append({"role": "assistant", "content": antwort})
