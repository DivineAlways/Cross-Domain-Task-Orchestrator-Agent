import requests

class ApiModule:
    def __init__(self):
        self.base_urls = {}  # Dictionary to store base URLs for different APIs

    def add_api_base_url(self, api_name, base_url):
        self.base_urls[api_name] = base_url

    def make_request(self, api_name, endpoint, method="GET", headers=None, params=None, data=None):
        if api_name not in self.base_urls:
            raise ValueError(f"API '{api_name}' not configured.")

        base_url = self.base_urls[api_name]
        url = f"{base_url}{endpoint}"

        try:
            if method == "GET":
                response = requests.get(url, headers=headers, params=params)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError(f"Invalid HTTP method: {method}")

            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            return None

class Agent:
    # ...
    def run(self):
        print("Agent is running...")
        print("Connecting to Omniverse...")
        self.omniverse_interface.connect()

        while True:
            user_input = input("Enter your request: ")
            intent = self.nlp_module.recognize_intent(user_input)
            entities = self.nlp_module.extract_entities(user_input)
            print(f"Intent: {intent}")
            print(f"Entities: {entities}")

            plan = self.task_planner.create_plan(intent, entities)

            for step in plan:
                result = self.execute_step(step)
                if result:
                    print(result) # Print the result of the step or do something else

    def execute_step(self, step):
        action = step['action']
        params = step['params']
        print(f"Executing step: {action} with params: {params}")

        if action == 'get_weather_data':
            return self.api_module.get_weather_data(params.get('location'))
        else:
            print("Unknown task.")
            return "Unknown task."