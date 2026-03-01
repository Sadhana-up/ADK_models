#!/usr/bin/env python
"""Run the litellm_agent"""

from agents.simple_agent.litellm_agent.agent import root_agent

if __name__ == "__main__":
    print(f"Agent: {root_agent.name}")
    print(f"Description: {root_agent.description}")
    print(f"Instruction: {root_agent.instruction}")
    print(f"\nAgent is ready! Available methods: {[m for m in dir(root_agent) if not m.startswith('_')]}")
