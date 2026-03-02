from google.adk.sessions import InMemorySessionService
from google.genai import types 
from dotenv import load_dotenv
from google.adk.runners import Runner
from ques_ans_agent.agent import ques_ans_agent

load_dotenv()



sessions_service = InMemorySessionService()

initial_state = {
    "user_name": "Alice",
    "user_preferences" : "likes sci-fi movies, fav food is mexican, enjoys hiking" 
}

#CREATING A NEW SESSION 
APP_NAME = 'alice sanu'
USER_ID = 'alice123'
SESSION_ID = 'session_001'

stateful_session = sessions_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state
)
print("Session created with ID:", stateful_session.session_id)


runner = Runner(
    agent=ques_ans_agent,
    app_name=APP_NAME,
    session_service=sessions_service,
)

new_message = types.Content(
    role="user",
    parts=[types.Part(text="What movie should I watch tonight?")],
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,    
): 
    if event.is_final_response():
        print("Agent's response:", event.response.parts[0].text)  

print("Session Event Exploration")
session = sessions_service_stateful.get_session(APP_NAME, USER_ID, SESSION_ID)

print("final session state")

for key,value in session.state.items():
    print(f"{key}: {value}")
