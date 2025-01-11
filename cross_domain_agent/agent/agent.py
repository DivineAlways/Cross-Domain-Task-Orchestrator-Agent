from agent.modules import TaskPlanner, ApiHandler, OmniverseInterface, GeminiModule
import time

class Agent:
    def __init__(self):
        self.nlp_module = GeminiModule()
        self.task_planner = TaskPlanner()
        self.api_handler = ApiHandler()
        self.omniverse_interface = OmniverseInterface()
        self.omniverse_address = self.omniverse_interface.server_address

    def run(self):
        print("Agent is running...")
        self.omniverse_interface.connect(self.omniverse_address)
        while True:
            user_input = input("Enter your request: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            # 1. Process user input with NLP
            intent = self.nlp_module.recognize_intent(user_input)
            print(f"Intent: {intent}")
            entities = self.nlp_module.extract_entities(user_input)
            print(f"Entities: {entities}")

            # 2. Create a task plan
            plan = self.task_planner.create_plan(user_input)
            print(f"Task Plan: {plan}")

            # 3. Execute the plan
            self.execute_plan(plan)

            # 4. Provide feedback
            print("Task completed.")

    def execute_plan(self, plan):
        for step in plan:
            action = step['action']
            params = step['params']
            print(f"Executing step: {action} with params: {params}")

            if action == "identify_object":
                # Example: Interact with Omniverse to identify an object
                response = self.omniverse_interface.send_command("identify object")
                print(f"Omniverse response: {response}")
            elif action == "calculate_path":
                # Example: Interact with Omniverse to calculate a path
                response = self.omniverse_interface.send_command("calculate path")
                print(f"Omniverse response: {response}")
            elif action == "move_object":
                # Example: Interact with Omniverse to move an object
                response = self.omniverse_interface.send_command("move object")
                print(f"Omniverse response: {response}")
            elif action == "get_text":
                # Example: Get text from user or a file
                print("Getting text...")
                time.sleep(1)
            elif action == "summarize_text":
                # Example: Summarize text using NLP module
                response = self.nlp_module.generate_response("Summarize this text")
                print(f"NLP response: {response}")
            elif action == "prepare_api_request":
                # Example: Prepare API request
                print("Preparing API request...")
                time.sleep(1)
            elif action == "call_api":
                # Example: Call API using API handler
                api_response = self.api_handler.send_request("/users", method="GET", params={"id": 123})
                print(f"API response: {api_response}")
            elif action == "process_api_response":
                # Example: Process API response
                print("Processing API response...")
                time.sleep(1)
            elif action == "unknown_task":
                print("Unknown task.")
            else:
                print(f"Unknown action: {action}")
            time.sleep(1)
