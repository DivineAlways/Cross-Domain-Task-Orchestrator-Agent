# Cross-Domain Task Orchestrator Agent User Guide

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DivineAlways/Cross-Domain-Task-Orchestrator-Agent.git
cd Cross-Domain-Task-Orchestrator-Agent
```

2. Install the package:
```bash
pip install -e .
```

## Usage

### Running the Agent

Basic usage:
```bash
python -m cross_domain_agent.main
```

With custom weather location:
```bash
python -m cross_domain_agent.main --location "New York,NY"
```

### Available Commands

The agent understands several types of requests:

1. Weather Queries
   - "What is the weather?" (uses default location)
   - "What's the weather in [location]?"
   
   Location formats:
   - US cities: "City, ST" (e.g., "Atlanta, GA")
   - International cities: "City, Country" (e.g., "Paris, France")
   - UK cities: "City, GB" (e.g., "London, GB")

2. Time Queries
   - "What time is it?"
   - "What is today's date?"

3. Flight Booking (Placeholder)
   - "Book a flight"

4. Alarm Setting
   - "Set an alarm for 6 AM"
   - "Wake me up at 7 tomorrow"

5. Restaurant Search
   - "Find Italian restaurants"
   - "Where can I eat sushi?"

6. Music Control
   - "Play some jazz"
   - "Play my favorite playlist"

### Configuration

The agent uses a configuration file located at `cross_domain_agent/config/config.yaml` for API keys and server settings.

Required configuration:
- `weather_api_key`: Your OpenWeatherMap API key
- `api_base_url`: Base URL for API calls
- `omniverse_server`: Omniverse server address

## Troubleshooting

Common issues:

1. "No module named 'agent'":
   - Make sure you've installed the package with `pip install -e .`

2. "Weather API key not found":
   - Check your config.yaml file has a valid API key

## Support

For issues and feature requests, please use the GitHub issue tracker.
