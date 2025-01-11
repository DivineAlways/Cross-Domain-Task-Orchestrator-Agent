import requests
import yaml

class ApiHandler:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        self.base_url = config['api_base_url']
        # Placeholder for authentication logic
        self.auth_token = None
        self.weather_api_key = config.get('weather_api_key')

    def authenticate(self):
        """
        Placeholder for API authentication logic.
        """
        print("Authenticating with API...")
        # Add authentication logic here
        self.auth_token = "test_token"  # Example token
        return True

    def send_request(self, endpoint, method="GET", params=None, data=None, headers=None):
        """
        Sends an API request to the specified endpoint.
        """
        url = f"{self.base_url}{endpoint}"
        if not headers:
            headers = {}
        if self.auth_token:
            headers['Authorization'] = f'Bearer {self.auth_token}'
        try:
            response = requests.request(method, url, params=params, json=data, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def get_weather(self, location):
        """
        Retrieves the current weather for a given location using OpenWeatherMap API.
        If no location is provided, defaults to Atlanta,Ga.
        """
        if not self.weather_api_key:
            print("Weather API key not found in config.")
            return None
        
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.weather_api_key}&units=metric"
        try:
            response = requests.get(weather_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Weather API request failed: {e}")
            return None

    def process_response(self, response):
        """
        Processes the API response.
        """
        if response:
            print("Processing API response...")
            return response
        else:
            print("No response to process.")
            return None
