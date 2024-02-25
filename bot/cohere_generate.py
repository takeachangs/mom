import cohere
import ast
from utils.helpers import rel_timer, abs_timer
class CohereGenerate:
    def __init__(self):
        """
        Initialize Cohere client
        """
        self.co = cohere.Client("6yJnofp1XcVL54HTVCh19zBlXnGLuDm9GdAqyQJi")
        self.model = "command"
        self.temperature = 0
        
        def get_delayed_response(self, message):
            """
            Get response from Cohere API in dictionary format
            """
            response = self.co.generate(
                model=self.model,
                prompt=message,
                temperature=self.temperature,
                stop_sequences=["}"]
            )
            dic = ast.literal_eval(response.generations[0].text)
            
            if dic["type"] == "relative":
                rel_timer(dic)
            elif dic["type"] == "absolute":
                abs_timer(dic)
            else:
                error_message = "Sorry I got distracted, can you ask me again?"
                return error_message  
        
        
        
        
