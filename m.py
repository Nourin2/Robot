import streamlit as st

# Define your data as a dictionary
data = {
    "What is your name?": "My name is Bard, a large language model from Google AI.",
    "What can you do?": "I can answer your questions in an informative way, generate different kinds of creative content, and translate languages.",
    "How are you doing today?": "I'm doing well, thank you for asking!",
}

# Initialize state variable to store conversation history
if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

# Display title and conversation history
st.title("Robot")
for message in st.session_state["conversation"]:
    st.write(f"{message['role']}: {message['content']}")

# User input field and button
user_input = st.text_input("Ask me something:")
if st.button("Send"):

    # Check if user input matches a preset question
    if user_input in data:
        response = data[user_input]
    else:
        response = "Sorry, I don't have a preset answer for that question. However, I can try to answer it in a more general way."

    # Add user input and response to conversation history
    st.session_state["conversation"].append({"role": "User", "content": user_input})
    st.session_state["conversation"].append({"role": "Chatbot", "content": response})