##CONNECT our adk agent with otther models rather than gemini 

import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

model = LiteLlm(model="groq/llama-3.3-70b-versatile",
                api_key=os.getenv("GROQ_API_KEY"))

get_movie_recommendations = Agent(
    name="get_movie_recommendations",
    model=model,
    description="Get movie recommendations based on a user's preferences.",
    instruction="""You are a movie recommendation agent.
      You will receive a user's preferences and you need to provide a list of movie recommendations
        based on those preferences. 
        The user's preferences will include 
        genres, actors, directors, and any specific themes or elements t
        hey enjoy in movies. Your response should be a list of movie titles
        along with a brief description of each movie and why it is recommended 
        based on the user's preferences.""",

)

# Expose the agent as root_agent for ADK framework
root_agent = get_movie_recommendations

