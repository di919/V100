import streamlit as st
import openai
import os

# --- GROQ API EINRICHTUNG ---
# Holt den API-Schlüssel sicher aus den Streamlit Secrets
try:
    client = openai.OpenAI(
        api_key=st.secrets["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1"
    )
except Exception:
    st.error("Fehler: GROQ_API_KEY nicht in den Secrets gefunden!")
    st.stop()


# --- CHATBOT LOGIK ---
st.title("v100 🧠")
st.caption("Dein eigener Chatbot, angetrieben von Groq")

# Initialisiert den Chat-Verlauf
if "messages" not in st.session_state:
    st.session_state.messages = []

# Zeigt alte Nachrichten an
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Nimmt neue Eingabe entgegen
if prompt := st.chat_input("Was geht?"):
    # Fügt User-Nachricht hinzu
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Holt Antwort von Groq
    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # AKTUELLES GRATIS-MODELL VON GROQ
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        except openai.APIError as e:
            st.error(f"Groq API Fehler: {e}")
            response = "Sorry, da lief was schief bei Groq."
        except Exception as e:
            st.error(f"Ein Fehler ist aufgetreten: {e}")
            response = "Sorry, da lief was schief."

    # Fügt Bot-Antwort zum Verlauf hinzu
    st.session_state.messages.append({"role": "assistant", "content": response})
