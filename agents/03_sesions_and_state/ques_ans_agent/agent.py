from google.adk.agents import Agent

ques_ans_agent = Agent(
    name="QuesAnsAgent",
    model="gemini-3-flash-preview",
    description="An agent that answers questions based on user preferences and context.",
    instruction="""You are a helpful assistant that answers questions based on the user's preferences and context. 
Use the information provided in the session state to tailor your responses. If the user asks about movie recommendations, suggest sci-fi movies. If they ask about food, recommend Mexican cuisine. If they inquire about activities, suggest hiking.

Here is some information about the user: 
Name :
{user_name}
Preferences:
{user_preferences}
""",)
