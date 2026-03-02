import uuid
import asyncio
import os
from dotenv import load_dotenv

from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Load environment variables from .env file
load_dotenv()


async def main():
    session_service = InMemorySessionService()
    state_context = {
        "user_name": "John Doe",
        "user_post_preferences": "John prefers to post about technology and programming on Twitter and LinkedIn."

    }

    SESSION_ID = str(uuid.uuid4())
    USER_ID = "user_123"
    APP_NAME = "social_media_manager"

    session = await session_service.create_session(
        session_id=SESSION_ID,
        user_id=USER_ID,
        app_name=APP_NAME,
        state=state_context
    )

    print("Session created with ID:", session.id)

    runner = Runner(agent=root_agent, session_service=session_service, app_name=APP_NAME)

    user_query = types.Content(
        role = "user",
        parts=[
            types.Part(
                text="What should I post about today?"
            )
        ]

    )
    for event in runner.run(
        user_id=USER_ID,    
        session_id=SESSION_ID, 
        new_message=user_query

    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print("Agent response:", event.content.parts[0].text)

    session = await session_service.get_session(
        app_name=APP_NAME,
        session_id=SESSION_ID,
        user_id=USER_ID
    )

    print("SESSION STATE:", session.state)

    for key, value in session.state.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())
