from google.adk.sessions import InmemorySessionService,Session
temp_service = InmemorySessionService()
example_session = temp_service.create_session(
    app_name = "my_app",
    user_id = "user_123",
    state = {"key": "value"}
)

print(f"Examining session properties")
# print(f"Id: {example_session.id}")
# print(f"App Name: {example_session.app_name}")
# print(f"User ID: {example_session.user_id}")
print(f"State ('state')")