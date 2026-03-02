import os 
from dotenv import load_dotenv

load_dotenv
from google.adk.agents import Agent

root_agent =Agent(
    name ="PostAgent",
    description="An agent that can post on social media platforms.",
    model = "gemini-3-flash-preview",
    instruction=""" You are a helpful assistant that can help respond about the post preferences,
        The information about the user and their post preferences are given in the state content
        Name:  {user_name}
        Post preferences: {user_post_preferences}"""
    

)