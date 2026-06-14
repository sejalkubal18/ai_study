import streamlit as st
import google.generativeai as genai

st.title("AI Study Assistant Chatbot 🤖")
st.caption("Aligned with UN SDG 4: Quality Education")

# Configure API Key (Input box for user or set as secret)
api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input("Ask an academic question..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        
        # System instructions embedded in the prompt to enforce SDG 4 behavior
        prompt = f"You are an expert AI Study Assistant acting as a tutor. Help the student understand this concept: {user_input}"
        response = model.generate_content(prompt)
        
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.chat_message("assistant").write(response.text)
      
