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
            # Format location query and get coordinates
            from urllib.parse import quote
            if location is None:
                location = self.default_location
                
            # Clean up the location string
            location = location.strip()
            print(f"Processing location: '{location}'")
            
            # Format the location query
            if ',' in location:
                parts = [part.strip() for part in location.split(',')]
                # For US locations with state code
                if len(parts) == 2 and len(parts[1]) == 2:
                    formatted_location = f"{parts[0]},{parts[1]},US"
                else:
                    formatted_location = ','.join(parts)
            else:
                formatted_location = location
            
            # URL encode the location string
            encoded_location = quote(formatted_location)
            print(f"Formatted location query: '{formatted_location}'")
            
            # Make geocoding request
            geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={encoded_location}&limit=1&appid={self.weather_api_key}"
            print(f"Fetching coordinates...")
            geo_response = requests.get(geocoding_url)
            
            if geo_response.status_code == 401:
                print("ERROR: Invalid API key or unauthorized access")
                return None
            elif geo_response.status_code != 200:
                print(f"Geocoding API error: {geo_response.status_code}")
                print(f"Response: {geo_response.text}")
                return None
                
            location_data = geo_response.json()
            
            if not location_data:
                print(f"Could not find location: '{formatted_location}'")
                print("Tips:")
                print("- For US cities: 'City, ST' (e.g. 'Atlanta, GA')")
                print("- For international cities: 'City, Country' (e.g. 'London, GB' or 'Paris, France')")
                print("- For UK cities, use GB as country code (e.g. 'London, GB')")
                print("- Check spelling and try again")
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
