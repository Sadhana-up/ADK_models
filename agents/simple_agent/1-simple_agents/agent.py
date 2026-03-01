from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
import os       
from dotenv import load_dotenv
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

groq_model= LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    api_key=groq_api_key,
)


# root_agent = LlmAgent(
#     name="OpenRouter_DeepSeek_Agent",
#     model=groq_model,
#     description="A DeepSeek agent that can answer questions and perform tasks.",
#     instruction="You are a DeepSeek agent. Help the user with their programming tasks by providing code snippets, explanations, and debugging assistance. Be concise and clear in your responses.",
# )
# from google.adk.agents import Agent
# from dotenv import load_dotenv
# from google.adk.tools import google_search
# load_dotenv()

# root_agent = Agent(
#     name="SimpleAgent",
#     model="gemini-3-flash-preview",
#     description="A simple agent that can answer questions and perform tasks.",
#     instruction="You are a simple agent. Help the user with their programming tasks by providing code snippets, explanations, and debugging assistance. Be concise and clear in your responses.",
    
# )

##Simple tool agent : 

# def get_current_weather(location) -> dict:
#     '''Get the current weather for a given location.'''
#     return{
#         "location": location,
#         "weather": "sunny",
#         "temperature": 25
#     }

#     # This is a mock function to simulate getting the current weather for a location.
#     # In a real implementation, this would call a weather API.
#     return f"The current weather in {location} is sunny with a temperature of 25°C."
# root_agent = Agent(
#     name="search_agent",
#     model="gemini-2.5-flash",
#     description="tool agent that can search the web for information.",
#     instruction="You are a search agent. Use the google  search tool to find information on the web. Be concise and clear in your responses.",
#     # tools=[google_search, get_current_weather] ##--> one tool at a time # no built in with default tools 
#     tools=[google_search],
#     # tools=[get_current_weather],
    
#     )






