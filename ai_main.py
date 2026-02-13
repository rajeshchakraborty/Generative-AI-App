import os

import google.genai as genai

class researchModel:
    MODEL_NAME = "gemini-3-flash-preview"

    def get_client(self):
        GEMINI_API_KEY = "AIrajeshFhOzzf6G1JyrRP3NjE7H0OEIwo1pg" # Replace with your actual API key or set it in the environment variable
        try:
            api_key = os.environ.get("GEMINI_API_KEY", GEMINI_API_KEY)
            if not api_key:
                raise RuntimeError("Set GEMINI_API_KEY in your environment.")
            return genai.Client(api_key=api_key)
        except Exception as e:
            print(f"Error initializing the client: {e}")
            return None
        

class ResearchApp(researchModel):
    def __init__(self):
        self.__database = {}
        self.first_manu()

    def first_manu(self):
        while True:
            first_input = input("""
        Hi, How do you want to precess?
        1. Not a mumber ? Register here
        2. Already a member ? Login here
        3. Exit
        """).strip()

            if first_input == "1":
                self.__register()
            elif first_input == "2":
                self.__login()
            elif first_input == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    def second_menu(self):
        second_input = input("""
        What do you want to do next?
        1. Sentiment analysis
        2. Language translation
        3. Language detection
        4. Exit
        """)

        if second_input == "1":
            self.sentiment_analysis()
        elif second_input == "2":
            self.language_translation()
        elif second_input == "3":
            self.language_detection()
        elif second_input == "4":
            exit()

    def __register(self):
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip().lower()
        password = input("Enter your password: ").strip()
        self.__database[email] = {"name": name, "password": password}
        print("Registration successful!")

    def __login(self):
        while True:
            email = input("Enter your email: ").strip().lower()
            password = input("Enter your password: ").strip()
            if email in self.__database and self.__database[email]["password"] == password:
                print(f"Welcome back, {self.__database[email]['name']}!")
                self.second_menu()
                return
            print("Invalid email or password.")

    def sentiment_analysis(self):
        text = input("Enter the text for sentiment analysis: ")
        client = super().get_client()
        if not client:
            return
        response = client.models.generate_content(
            model=self.MODEL_NAME,
            contents=f"Perform sentiment analysis on the following text: {text}",
        )
        print(f"Sentiment Analysis Result: {response.text}")
        self.second_menu()
        
    def language_translation(self):
        text = input("Enter the text to translate: ")
        client = super().get_client()
        if not client:
            return
        target_language = input("Enter the target language (e.g., 'French', 'Spanish'): ")
        response = client.models.generate_content(
            model=self.MODEL_NAME,
            contents=f"Translate the following text to {target_language}: {text}",
        )
        print(f"Translation Result: {response.text}")
        self.second_menu()   

    def language_detection(self):
        text = input("Enter the text for language detection: ")
        client = super().get_client()
        if not client:
            return
        response = client.models.generate_content(
            model=self.MODEL_NAME,
            contents=f"Detect the language of the following text: {text}",
        )
        print(f"Language Detection Result: {response.text}")
        self.second_menu()

if __name__ == "__main__":
    app = ResearchApp()
