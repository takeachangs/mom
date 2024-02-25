from cohere_chat import CohereChat
from cohere_classify import CohereClassify
from cohere_generate import CohereGenerate
import threading 


def RunCohere(chat, msg):
    predict = CohereClassify.classify_message(msg)
    if predict == "not_time_task":
        chat.CohereChat.get_response(msg)
        
    elif predict == "time_task":
        immediate = threading.Thread(target = chat.CohereChat.get_response, args= (msg,))
        immediate.start()

        timer = CohereGenerate()
        delayed = threading.Thread(target = timer.get_delayed_response, args = (msg,))
        delayed.start()

