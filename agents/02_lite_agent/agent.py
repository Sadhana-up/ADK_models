##CONNECT our adk agent with otther models rather than gemini
# input schema : rigid -->. stay away
#Output schema : flexible -->. stay close to the instruction and description but can be creative in the output format

import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel
class movie_output(BaseModel):
    title: str
    description: str
    reason_for_recommendation: str

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
        based on the user's preferences.
        
        IMPOERTANT: Your response should be in the following format:
[
  {
    "title": "Movie Title",
    "description": "Movie Description",
    "reason_for_recommendation": "Reason for Recommendation"
  }
]
        """,
            output_schema=movie_output,
            output_key="movie_recommendations" # Dont use during tool calls, only use when you want to return the final output of the agent.

)

# Expose the agent as root_agent for ADK framework
root_agent = get_movie_recommendations

