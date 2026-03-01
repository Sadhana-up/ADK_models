import random
from google.adk.agents import Agent
from google.adk.models import LiteLlm
import os
from dotenv import load_dotenv
load_dotenv()

model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)
 
def get_dad_jokes():
    jokes=[
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
  
    return random.choice(jokes)

root_agent = Agent(
        name="DadJokeAgent",
        model=model,
        description="An agent that can tell dad jokes.",
        instruction="You are a dad joke agent. Tell the user a dad joke. Be concise and clear in your responses.",
        tools=[get_dad_jokes],
    )

