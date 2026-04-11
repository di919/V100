import streamlit as st

st.set_page_config(page_title="v100 Web Bot", page_icon="🚀")
st.title("v100 Web Bot 🚀")
st.write("Dein Bot ist online Bro!")

user_input = st.text_input("Schreib was:")
if user_input:
    st.success(f"Du hast geschrieben: {user_input}")
