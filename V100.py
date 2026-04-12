import streamlit as st
import random

st.set_page_config(page_title="v100 Web Bot", page_icon="🚀")
st.title("v100 Web Bot 🚀")
st.write("Dein Bot ist online Bro!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

eingabe = st.chat_input("Schreib was:")

if eingabe:
    st.session_state.messages.append({"role": "user", "content": eingabe})
    with st.chat_message("user"):
        st.write(eingabe)
    
    antworten = [
        f"Yo Leo! Du hast '{eingabe}' gesagt. Replit kann das nicht 😂",
        f"'{eingabe}'? Bro ich bin v100. Ich laufe 24/7 gratis während Replit pennt.",
        f"Verstanden: {eingabe}. Was noch? Ich hab unlimited Energie.",
        f"Nice! '{eingabe}' notiert. Quota-Hölle? Kenn ich nicht mehr.",
        f"v100 hier. '{eingabe}' empfangen. Streamlit Cloud > Replit Quota 💯"
    ]
    
    antwort = random.choice(antworten)
    st.session_state.messages.append({"role": "assistant", "content": antwort})
    with st.chat_message("assistant"):
        st.write(antwort)
