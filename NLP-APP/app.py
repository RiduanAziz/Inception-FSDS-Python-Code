import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="NLP App", 
    page_icon="🤖",
    layout="wide")

class BaseModel:
    def get_model(self):
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-2.5-flash")
            return model
        except Exception as e:
            print(f"Error configuring Gemini API: {e}")
            return None
        
def main():
    st.title("Welcome to the NLP App!")
    st.write("Please sign in to continue.")
    
    #Initialize Session State
    if "database" not in st.session_state:
        st.session_state.database = {}  # Format: email: {'name': name, 'password': password}
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "current_user" not in st.session_state:
        st.session_state.current_user = None
    
    #Sidebar for Navigation / Auth
    with st.sidebar:
        st.header("Navigation")
        if not st.session_state.logged_in:
            option = st.radio("Choose Option", ["Login", "Register"])
        else:
            st.success(f"Welcome, {st.session_state.database[st.session_state.current_user]['name']}!")
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.current_user = None
                st.rerun()
    
    if not st.session_state.logged_in:
        if option == "Login":
             login()
        elif option == "Register":
            register()
    else:
        feature()
        
    
def feature():
    st.subheader("NLP Features")
    features = st.selectbox(
        "Select a feature to explore:",
            ["Sentiment Analysis", "Language Translation", "Language Detection"])
    
    nlp = BaseModel()
    model = nlp.get_model()
    
    if features == "Sentiment Analysis":
        st.info("Analyze the sentiment of a sentence!")
        user_text = st.text_area("Enter text for sentiment analysis:")
        if st.button("Analyze Sentiment"):
            if user_text:
                with st.spinner("Analyzing..."):
                    response = model.generate_content(f"Give the sentiment of the following text: '{user_text}'")
                    st.write("### Sentiment Analysis Result:")
                    st.write(response.text)
            else:
                st.warning("Please enter some text to analyze.")
                
    elif features == "Language Translation":
        st.info("Translate text to another language!")
        user_text = st.text_area("Enter text for translation:")
        target_language = st.text_input("Enter target language (e.g., 'French', 'Spanish'):")
        if st.button("Translate"):
            if user_text and target_language:
                with st.spinner("Translating..."):
                    response = model.generate_content(f"Translate the following text to {target_language}: '{user_text}'")
                    st.write("### Translation Result:")
                    st.write(response.text)
            else:
                st.warning("Please enter both text and target language for translation.")
    
    elif features == "Language Detection":
        st.info("Detect the language of a sentence!")
        user_text = st.text_area("Enter text for language detection:")
        if st.button("Detect Language"):
            if user_text:
                with st.spinner("Detecting..."):
                    response = model.generate_content(f"Detect the language of the following text: '{user_text}'")
                    st.write("### Language Detection Result:")
                    st.write(response.text)
            else:
                st.warning("Please enter some text to detect the language.")
    
def register():
    st.subheader("Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Register"):
        if email in st.session_state.database:
            st.error("Email already registered. Please log in.")
        else:
            st.session_state.database[email] = {'name': name, 'password': password}
            st.success("Registration successful! Please log in.")
            st.rerun()
    else:
        st.info("Please fill in the details to register.")
            
def login():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if email in st.session_state.database and st.session_state.database[email]['password'] == password:
            st.session_state.logged_in = True
            st.session_state.current_user = email
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid email or password.")
    else:
        st.info("Please enter your email and password to log in.")
            


if __name__ == "__main__":
    main()

