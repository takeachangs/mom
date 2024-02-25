from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from utils.helpers import format_entry
db_name = "user_data"
collection_id = "_id"
chat_history_column = "chat_history"
user_name_column = "user_name"

# {
#  _id: "..."
#  user_name: "..."
#  chat_history: "<Cohere format>"
# }
"""Return the collection containing chat history. This is a helper
function.
"""
def _find_db(client: MongoClient) -> dict:
    db: Database = client[db_name]
    return db


"""Return true iff this user exists in the user collection
"""
def find_user(client: MongoClient,
              user_id: str) -> (dict | None):
    db: Database = _find_db(client)
    ids: Collection = db[collection_id]
    query: dict = {collection_id: user_id}

    user = ids.find_one(query)
    return user

"""Logs all users in the collection to the console"""
def print_all_users(client: MongoClient):
    db: Database = _find_db(client)
    collection: Collection = db[collection_id]

    cursor = collection.find({})

    for user in cursor:
        print(f"\n{user}\n")

"""Adds a new user to the user collection
"""
def init_user(client: MongoClient,
              user_id: str,
              user_name: str,
              greeting: dict) -> None:
    db: Database = _find_db(client)
    collection: Collection = db[collection_id]
    new_user: dict = {collection_id: user_id,
                      user_name_column: user_name,
                      chat_history_column: [format_entry("CHATBOT", greeting)]}

    collection.insert_one(new_user)

"""Return the user name of a user in the collection. Return None
 iff the user doesn't exist in the collection.
"""
def get_user_name(client: MongoClient,
                  user_id: str) -> str:
    user = find_user(client, user_id)
    if user is None:
        return None
    
    return user[user_name_column]

"""Return true iff the user in the collection has a chat history. If
the user doesn't exist, return None"""
def user_has_chat_history(client: MongoClient,
                          user_id: str) -> (bool | None):
    user: (dict | None) = find_user(client, user_id)
    if user is None:
        return None
    elif not chat_history_column in user:
        return False
    else:
        return True


"""Return the list containing the chat history of this user. Return
None if the user doesn't exist. 
"""
def get_chat_history(
        client: MongoClient,
        user_id: str) -> (list | None):
    user: (dict | None) = find_user(client, user_id)
    if user is None:
        return None
    
    return user[chat_history_column]


"""Update to the chat history of this user. Return false iff the
user doesn't exist in the collection.
"""
def record_chat_history(
        client: MongoClient,
        user_id: str,
        new_entry: dict) -> bool:
    
    database: Database = _find_db(client)
    collection: Collection = database[collection_id]

    user_name: str = get_user_name(client, user_id)
    current_chat_history: list = get_chat_history(client, user_id)
    current_chat_history.append(new_entry)

    query: dict = {collection_id: user_id}
    new_user: dict = {collection_id: user_id,
                      user_name_column: user_name,
                      chat_history_column: current_chat_history}

    collection.replace_one(query, new_user)

    return True
