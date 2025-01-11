import requests
import yaml

class ApiHandler:
    def __init__(self, config_path=None, default_location='Atlanta,GA'):
        if config_path is None:
            import os.path
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config', 'config.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        self.base_url = config['api_base_url']
        # Placeholder for authentication logic
        self.auth_token = None
        self.weather_api_key = config.get('weather_api_key')
        self.default_location = default_location

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

    def get_weather(self, location=None):
        """
        Retrieves the current weather for a given location using OpenWeatherMap API.
        If no location is provided, uses the default location.
        """
        if location is None:
            location = self.default_location
        if not self.weather_api_key:
            print("ERROR: Weather API key not configured!")
            print("Please follow these steps:")
            print("1. Sign up at https://openweathermap.org/api")
            print("2. Get your API key from your account")
            print("3. Add it to cross_domain_agent/config/config.yaml")
            print("   weather_api_key: \"your-api-key-here\"")
            return None
        
        try:
            # First get coordinates for the location
            geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={self.weather_api_key}"
            geo_response = requests.get(geocoding_url)
            geo_response.raise_for_status()
            location_data = geo_response.json()
            
            if not location_data:
                print(f"Location not found: {location}")
                return None
                
            lat = location_data[0]['lat']
            lon = location_data[0]['lon']
            
            # Now get weather using coordinates
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.weather_api_key}&units=metric"
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
