import streamlit as st
from hf_client import get_response
from sheets_client import log_chat

st.set_page_config(page_title="HF Chat App", layout="centered")
st.title("Hugging Face Chat App")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Type your message")

if user_input:
    # Get bot reply
    bot_reply = get_response(user_input)

    # Update UI state
    st.session_state.chat.append(("User", user_input))
    st.session_state.chat.append(("Bot", bot_reply))

    # Log to Google Sheets (single source of truth)
    log_chat(user_input, bot_reply)

# Render chat history
for role, message in st.session_state.chat:
    with st.chat_message(role.lower()):
        st.write(message)
