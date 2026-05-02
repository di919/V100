import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="v100", page_icon="🧠")
st.title("v100 🧠 Gratis Edition")

# Groq Client - nutzt OpenAI Library aber Groq Server
client = OpenAI(
    api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

# Chat History speichern
if "messages" not in st.session_state:
    st.session_state.messages = []

# Alte Nachrichten anzeigen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Frag v100 was..."):
    # User Nachricht anzeigen
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Antwort holen
    with st.chat_message("assistant"):

              model="llama-3.1-8b-instant", model="llama3-70b-8192",  # NEU: Das aktuelle Gratis-Modell von Groq
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages
