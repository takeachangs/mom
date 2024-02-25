from bot.cohere_chat import CohereChat
from bot.cohere_classify import CohereClassify
from bot.cohere_generate import CohereGenerate
from telegram.ext import ContextTypes
import threading
import asyncio

def _between_response(response_callback, args: tuple) -> None:
    print("\nCheckpoint 1\n")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    msg, chat_id, context = args
    loop.run_until_complete(response_callback(msg, chat_id, context))
    loop.close()

def RunCohere(chat: CohereChat, msg: str, chat_id: int, context: ContextTypes.DEFAULT_TYPE) -> str:
    classifier = CohereClassify()
    predict = classifier.classify_message(msg)
    print(predict)
    if predict == "time_task":
        timer = CohereGenerate()
        delayed = threading.Thread(target = _between_response, args = (timer.get_delayed_response, (msg, chat_id, context)))
        delayed.start()
    
    return chat.get_response(msg)

