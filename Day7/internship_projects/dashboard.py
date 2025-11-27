import streamlit as st
import google.generativeai as genai

key = "AIzaSyCKbLmhn_jMaRP84A924nG8NRJKkw32nYc"

genai.configure(api_key = key)
model = genai.GenerativeModel("gemini-2.5-flash")


# st.sidebar.page_link("page1.py", label="Home")
st.sidebar.text("Home")
st.sidebar.text("About")
st.sidebar.text("Contects")
st.sidebar.text("Hero section")
st.sidebar.text("New Chats")
st.sidebar.text("Search box")
st.sidebar.text("History")

prompt = st.chat_input("Ask me anything...", accept_file=True)

if prompt:
    user_text = prompt["text"]
    user_files = prompt["files"]

    container = []

    if user_text:
        container.append({"text": user_text})
        st.write("You: "+user_text)
        

    response = model.generate_content({"parts": container})
    st.write("Bot: "+response.text)
