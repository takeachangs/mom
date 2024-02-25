from pymongo.mongo_client import MongoClient

def get_chat_history(client: MongoClient, user: str) -> list:
    query = {"user": user}

    db = client["user_data"]
    col = db["chat_history"]
    doc = col.find_one(query)

    return doc["chat_history"]


def record_chat_history(client: MongoClient, user: str, chat_history: list):
    query = {"user": user}

    db = client["user_data"]
    col = db["chat_history"]
    doc = col.find_one(query)

    new_history = doc["chat_history"]
    new_history.extend(chat_history)

    col.update_one(query, {"chat_history": new_history})