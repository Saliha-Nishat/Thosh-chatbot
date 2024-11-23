import streamlit as st
from nltk.chat.util import Chat, reflections

# Define a set of response pairs for the chatbot
pairs = [
    ['hi|hello', ['Hello!', 'Hi there!']],
    ['how are you?', ['I am fine, thank you! How can I assist you today?']],
    ['bye', ['Goodbye! Have a great day!']],
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Streamlit app
def chatbot_app():
    st.title("Chat with My NLP Chatbot")
    st.write("Welcome! Ask me anything. Type 'bye' to end the chat.")
    
    user_input = st.text_input("You: ", "")
    
    if user_input:
        # Get the chatbot's response
        response = chatbot.respond(user_input)
        
        if response:
            st.write(f"Chatbot: {response}")
        else:
            st.write("Chatbot: I didn't understand that. Can you rephrase?")
    
    if user_input.lower() == 'bye':
        st.write("Chatbot: Goodbye! See you later.")

if __name__ == "__main__":
    chatbot_app()
