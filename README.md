# Cross-Domain Agent

This project implements a cross-domain agent capable of understanding user requests, creating task plans, and interacting with various services, including APIs and Omniverse.

## Overview

The agent is designed to be modular and extensible, allowing for easy integration of new capabilities. It consists of the following main components:

*   **Agent**: The main class that orchestrates the entire process.
*   **NLP Module**: Handles natural language processing, including intent recognition and entity extraction.
*   **Task Planner**: Creates a plan of action based on the user's request.
*   **API Handler**: Manages communication with external APIs.
*   **Omniverse Interface**: Connects and interacts with an Omniverse instance.

## Setup

### Prerequisites

*   Python 3.6+
*   pip
*   A Gemini API key (set as an environment variable `GEMINI_API_KEY`)
*   An Omniverse instance (optional)

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd cross_domain_agent
    ```
2.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```
3.  Set the `GEMINI_API_KEY` environment variable:

    ```bash
    export GEMINI_API_KEY="your_gemini_api_key"
    ```

### Configuration

The project uses a `config/config.yaml` file for configuration. Here's an example:

```yaml
api_base_url: "https://api.example.com"
omniverse_server: "localhost:8080"
weather_api_key: "your_weather_api_key"
```

*   `api_base_url`: The base URL for your API.
*   `omniverse_server`: The address of your Omniverse server.
*   `weather_api_key`: Your OpenWeatherMap API key.

## Usage

To run the agent, execute the following command:

```bash
python cross_domain_agent/main.py
```

The agent will prompt you to enter your request. Type your request and press Enter. The agent will process your request, create a task plan, and execute it.

## Modules

### NLP Module (`agent/modules/nlp_module.py`)

The NLP module uses the Gemini API to process natural language. It includes the following methods:

*   `recognize_intent(user_input)`: Recognizes the intent of the user input.
*   `extract_entities(user_input)`: Extracts entities from the user input.
*   `generate_response(text)`: Generates a response based on the given text.

### Task Planner (`agent/modules/task_planner.py`)

The task planner creates a plan of action based on the user's request. It includes the following method:

*   `create_plan(parsed_request)`: Generates a sequence of steps to achieve the goal.

### API Handler (`agent/modules/api_handler.py`)

The API handler manages communication with external APIs. It includes the following methods:

*   `send_request(endpoint, method, params, data, headers)`: Sends an API request to the specified endpoint.
*   `get_weather(location)`: Retrieves the current weather for a given location using OpenWeatherMap API.
*   `process_response(response)`: Processes the API response.

### Omniverse Interface (`agent/modules/omniverse_interface.py`)

The Omniverse interface connects and interacts with an Omniverse instance. It includes the following methods:

*   `connect(address)`: Establishes a connection to an Omniverse instance.
*   `send_command(command)`: Sends commands to the Omniverse environment.
*   `receive_data()`: Receives data from the Omniverse environment.

### Omniverse Module (`agent/modules/omniverse_module.py`)

The Omniverse module provides a basic interface for connecting to and interacting with Omniverse. It includes the following methods:

*   `connect()`: Connects to the Omniverse instance.
*   `disconnect()`: Disconnects from the Omniverse instance.
*   `execute_command(command)`: Executes a command in the Omniverse environment.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License.
