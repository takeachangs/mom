import cohere
import ast
from telegram.ext import ContextTypes
from utils.helpers import rel_timer, abs_timer
class CohereGenerate:
    def __init__(self):
        """
        Initialize Cohere client
        """
        self.co = cohere.Client("6yJnofp1XcVL54HTVCh19zBlXnGLuDm9GdAqyQJi")
        self.model = "command"
        self.temperature = 0
        
    async def get_delayed_response(self, message: str, chat_id: int, chat_context: ContextTypes.DEFAULT_TYPE) -> None:
        """
        Get response from Cohere API in dictionary format
        """
        print("\nCheckpoint 2\n")
        response = self.co.generate(
            model=self.model,
            prompt=f"""Imagine you are processing a prompt to be used as an input for a function. The prompt is ```
                {message}```. Return a dictionary in the following format: {"type":, "time":, "duration":, "desc":} where 
                "type"  is  only "absolute"  or "relative". If "type" is "absolute", then "duration" would be 0.  If 
                "type" is "relative", "time" would be 0; and "desc" is a string of a short response to be sent after 
                time passes. For example, if the prompt is something like " I need to be done with MAT237 work by 5 hours 
                from now", the expected dictionary would be as follows:
                    {{"type": ...
                      "relative": ...,
                      "time": (0,0,0),
                      "duration": (5,0,0),
                      "desc": "Hey, it has been 5 hours, hope you are done with MAT237!"}}
                If it was
                and if the prompt is something like "remind me to submit my MAT237 assignment at 3pm", it would be dictionary {{"type": "absolute","time": (15,0,0),"duration": (0,0,0),"desc": "It is 3pm! Have you submitted your MAT237 assignment?"}} Do not return anything other than the dictionary.""",
            temperature=self.temperature,
            stop_sequences=["}"]
        )
        dic = ast.literal_eval(response.generations[0].text)
        
        if dic["type"] == "relative":
            message = rel_timer(dic)
            print("\nCheckpoint 3\n")
            await chat_context.bot.send_message(chat_id, message)
        elif dic["type"] == "absolute":
            message = abs_timer(dic)
            print("\nCheckpoint 3\n")
            await chat_context.bot.send_message(chat_id, message)
        else:
            error_message = 'Sorry I got distracted, can you ask me again?'
            return error_message  
        
        
        
        
