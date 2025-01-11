
class TaskPlanner:
    def __init__(self):
        print("Task planner initialized")

    def create_plan(self, parsed_request):
        """
        Generates a sequence of steps to achieve the goal based on the parsed request.
        For now, this is a simplified example.
        """
        print(f"Creating plan for request: {parsed_request}")
        intent = parsed_request.get("intent")
        entities = parsed_request.get("entities", {})

        if intent == "book_flight":
            plan = [{"action": "book_flight", "params": {
                "destination": entities.get("location"),
                "date": entities.get("date")
            }}]
        elif intent == "get_time":
            plan = [{"action": "get_current_time", "params": {}}]
        elif intent == "general_query":
            plan = [{"action": "respond_to_query", "params": {}}]
        elif "move object" in parsed_request.lower():
            plan = [
                {"action": "identify_object", "params": {}},
                {"action": "calculate_path", "params": {}},
                {"action": "move_object", "params": {}}
            ]
        elif "summarize" in parsed_request.lower():
            plan = [
                {"action": "get_text", "params": {}},
                {"action": "summarize_text", "params": {}}
            ]
        elif "call api" in parsed_request.lower():
            plan = [
                {"action": "prepare_api_request", "params": {}},
                {"action": "call_api", "params": {}},
                {"action": "process_api_response", "params": {}}
            ]
        elif "what is the weather" in parsed_request.lower():
            plan = [
                {"action": "get_weather", "params": {}}
            ]
        else:
            plan = [{"action": "unknown_task", "params": {}}]
        return plan
