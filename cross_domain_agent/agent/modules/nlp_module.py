import google.generativeai as genai
import os

class GeminiModule:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Gemini API key not found. Please set the GEMINI_API_KEY environment variable or pass the key as an argument.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

    def recognize_intent(self, user_input):
        """
        Recognizes the intent of the user input.
        """
        prompt = f"""
You are an intent recognition system.
Identify the intent of the following user input:
"{user_input}"

Possible intents are:
- get_weather
- book_flight
- get_time
- general_query
- unknown

Respond with the intent only, no other text. For example:
Input: What's the weather in London?
Response: get_weather

Input: Book me a flight to New York tomorrow.
Response: book_flight

Input: Hi, how are you?
Response: general_query

Input: What's the current time?
Response: get_time
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()

    def extract_entities(self, user_input):
        """
        Extracts entities from the user input.
        """
        print(f"Extracting entities for: {user_input}")
        # Placeholder for entity extraction logic
        return {"example_entity": "example_value"}
