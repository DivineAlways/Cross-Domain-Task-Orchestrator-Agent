from cross_domain_agent.agent.agent import Agent
import argparse

def main():
    parser = argparse.ArgumentParser(description='Cross Domain Agent')
    parser.add_argument('--location', type=str, default='Atlanta,GA',
                       help='Location for weather queries (default: Atlanta,GA). Use quotes for cities with spaces.')
    args = parser.parse_args()
    
    agent = Agent(default_location=args.location)
    agent.run()

if __name__ == "__main__":
    main()
