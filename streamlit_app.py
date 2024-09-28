
import streamlit as st
import google.generativeai as genai

st.title("✈️ Your Personal AI Travel Planner")
st.subheader("Plan your next adventure with AI")
st.markdown("Made by Mr.Tripop Netpu 6610422011")

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")

# Initialize the Gemini Model
if gemini_api_key:
    try:
        # Configure Gemini with the provided API Key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize with an empty list

# Display previous chat history using st.chat_message (if available)
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

# Capture user input and generate bot response
if user_input := st.chat_input("Tell me about your trip requirements..."):
    # Store and display user message
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    # Use Gemini AI to generate a bot response
    if gemini_api_key and model:
        try:
            # Generate a response tailored to travel planning
            prompt = f"Act as a travel planner and friendly assistant. {user_input}. Provide a detailed travel plan including activities, places to visit, estimated budget, and famous local restuarant."
            response = model.generate_content(prompt)
            bot_response = response.text
            
            # Store and display bot response
            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)
        except Exception as e:
            st.error(f"An error occurred while generating a response: {e}")
