from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-3-flash-preview",
    description="An agent that greets the user.",
    instruction="Respond to the user's greeting with a friendly message."
)
