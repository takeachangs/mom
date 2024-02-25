import cohere

class CohereChat: 
    def __init__(self, temperature, user):
        """
        Initialize Cohere client with API key
        """
        self.co = cohere.Client("6yJnofp1XcVL54HTVCh19zBlXnGLuDm9GdAqyQJi")
        self.model = "command"
        self.temperature = temperature
        self.chat_history = []
        self.user = user

    def get_response(self, message, documents =[]):
        """
        Get response from Cohere API
        """
        response = self.co.chat(
            chat_history=self.chat_history,
            message=message,
            temperature=self.temperature,
            documents=documents
        )
        user_message = {"user_name": self.user, "text": message}
        bot_message = {"user_name": "CHATBOT", "text": response.text}
        
        self.chat_history.append(user_message)
        self.chat_history.append(bot_message)

        return response
