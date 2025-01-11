import requests
import yaml

class ApiHandler:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        self.base_url = config['api_base_url']
        # Placeholder for authentication logic
        self.auth_token = None

    def authenticate(self):
        """
        Placeholder for API authentication logic.
        """
        print("Authenticating with API...")
        # Add authentication logic here
        self.auth_token = "test_token" # Example token
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
