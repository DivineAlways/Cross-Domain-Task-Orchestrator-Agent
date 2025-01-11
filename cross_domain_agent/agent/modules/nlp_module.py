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
- set_alarm
- find_restaurant
- play_music
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

Input: Set an alarm for 6 AM tomorrow.
Response: set_alarm

Input: Find Italian restaurants near me.
Response: find_restaurant

Input: Play some jazz music.
Response: play_music
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()

    def extract_entities(self, user_input):
        """
        Extracts entities from the user input.
        """
        import re
        import json

        prompt = f"""
You are an entity extraction system.
Identify and extract entities from the following user input:
"{user_input}"

Extract entities for the following types:
- location
- date
- time

Respond with a JSON formatted string. For example:
Input: What's the weather in London tomorrow?
Response: {{"location": "London", "date": "tomorrow"}}

Input: Set an alarm for 7 AM.
Response: {{"time": "7 AM"}}

Input: No entities here.
Response: {{}}
"""
        response = self.model.generate_content(prompt)
        json_match = re.search(r"\{.*\}", response.text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                print("Error: Invalid JSON format in entity extraction response.")
                return {}
        else:
            print("Error: No JSON found in entity extraction response.")
            return {}
