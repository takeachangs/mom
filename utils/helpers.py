
"""Returns the greeting message for the user"""
def greet_user(user_name: str) -> str:
    return f"Hi {user_name}, how has your day been?"

"""Returns an entry to the chat history written <role>"""
def format_entry(role: str, message: str) -> dict:
    return {"role": role, "message": message}