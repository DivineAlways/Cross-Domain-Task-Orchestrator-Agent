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