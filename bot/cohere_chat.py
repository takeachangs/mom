import cohere
import bot.db_handler as db
from utils.constants import PREAMBLE
from utils.helpers import greet_user, format_entry
from database.mongo_client import start_database
# If the user doesn't exist in the database, we create it

class CohereChat: 
    def __init__(self, temperature,user_id, user_name):
        """
        Initialize Cohere client with API key
        """
        self.co = cohere.Client("6yJnofp1XcVL54HTVCh19zBlXnGLuDm9GdAqyQJi")
        self.model = "command"
        self.temperature = temperature
        self.user_id = user_id
        self.user_name = user_name
        self.mongo_client = start_database()

        user: dict = db.find_user(self.mongo_client, self.user_id)
        if user is None:
            greeting = greet_user(self.user_name)
            db.init_user(self.mongo_client, self.user_id, self.user_name, greeting)

    def get_response(self, message, documents =[]):
        """
        Get response from Cohere API
        """
        # Fetch history from database
        chat_history: list = db.get_chat_history(self.mongo_client, self.user_id)
        if chat_history is None:
            exit(404)

        print(f"\n\n{chat_history}\n\n")

        response = self.co.chat(
            chat_history=chat_history,
            preamble_override=PREAMBLE,
            message=message,
            temperature=self.temperature,
            documents=documents
        )

        user_entry: dict = format_entry("USER", message)
        bot_entry: dict = format_entry("CHATBOT", response.text)

        # Update history on database
        db.record_chat_history(self.mongo_client, self.user_id, user_entry)
        db.record_chat_history(self.mongo_client, self.user_id, bot_entry)

        return response.text