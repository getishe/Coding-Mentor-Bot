# app.py
import streamlit as st
from mentor_bot import answer_query

st.set_page_config(page_title="Coding Mentor Bot", layout="centered")

st.title("👨‍💻 Coding Mentor Bot")
st.write("Ask me anything about Python!")

query = st.text_input("Your question:")

if query:
    with st.spinner("Thinking..."):
        response = answer_query(query)
    st.success("Here's what I found:")
    st.write(response)
