import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


class BaseModel:
    def get_model(self):
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-2.5-flash")
            return model
        except Exception as e:
            print(f"Error configuring Gemini API: {e}")

class AppFeatures(BaseModel):
    def __init__(self):
        self.__database = {}
        self.first_menu()

    def first_menu(self):
        first_input = input("""
        Hi! How do you like to proceed?
            1. not a member? Sign up here!
            2. already a member? Sign in here!
            3. exit
        """)

        if first_input == "1":
            self.__sign_up()
        elif first_input == "2":
            self.__sign_in()
        elif first_input == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Please try again.")
            self.first_menu()

    def __sign_up(self):
        name = input("Enter your name: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.__database:
            print("Username already exists. Please try again.")
            self.first_menu()
        else:
            self.__database[username] = [name, password]
            print("Sign up successful! Please sign in to continue.")
            self.first_menu()

    def __sign_in(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.__database :
            if self.__database[username][1] == password:
                print("Sign in successful! Welcome back!")
                self.second_menu()
            else:
                print("Invalid password. Please try again.")
                self.__sign_in()
        else:
            print("Email not found. Please Sign up first.")
            self.first_menu()

    def second_menu(self):
        second_input = input("""
        Hi! How do you like to proceed?
            1. Sentiment Analysis
            2. Language Translation
            3. Language Detection
            4. exit
        """)
        
        if second_input == "1":
            self.sentiment_analysis()
        elif second_input == "2":
            self.language_translation()
        elif second_input == "3":
            self.language_detection()
        elif second_input == "4":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Please try again.")
            self.second_menu()

    def sentiment_analysis(self):
        user_text = input("Enter the text you want to analyze: ")
        model = self.get_model()
        response = model.generate_content(f"Analyze the sentiment of the following text: {user_text}")
        result = response.text
        print(f"Sentiment Analysis Result: {result}")
        self.second_menu()

    def language_translation(self):
        user_text = input("Enter the text you want to translate: ")
        target_language = input("Enter the target language (e.g., 'French', 'Spanish'): ")
        model = self.get_model()
        response = model.generate_content(f"Translate the following text to {target_language}: {user_text}")
        result = response.text
        print(f"Translation Result: {result}")
        self.second_menu()

    def language_detection(self):
        user_text = input("Enter the text you want to detect the language of: ")
        model = self.get_model()
        response = model.generate_content(f"Detect the language of the following text: {user_text}")
        result = response.text
        print(f"Language Detection Result: {result}")
        self.second_menu()

app = AppFeatures()