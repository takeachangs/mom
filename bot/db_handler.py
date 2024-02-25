from pymongo.mongo_client import MongoClient

db_name = "user_data"
col_name = "chat_history"


"""Return the collection containing chat history. This is a helper
function.
"""
def find_db(client: MongoClient, user: str) -> dict:
    db = client[db_name]
    return db[col_name]


"""Return true iff this user already has a document in the chat history
collection.
"""
def find_chat_history(client: MongoClient, user: str) -> bool:
    col = find_db(client, user)
    return col.find_one({"user": user}) != None


"""Create a new document for this user in the chat history collection.
Do nothing and return false iff this user already has a document.
"""
def init_chat_history(client: MongoClient, user: str) -> bool:
    if find_chat_history(client, user) == True:
        return False

    col = find_db(client, user)
    new_doc = {"user": user, col_name: []}
    col.insert_one(new_doc)

    return True


"""Return the list containing the chat history of this user. Return
an empty list iff this user does not have a document in the chat
history collection.
"""
def get_chat_history(client: MongoClient, user: str) -> list:
    if find_chat_history(client, user) == False:
        return []

    col = find_db(client, user)
    doc = col.find_one({"user": user})
    return doc[col_name]


"""Add to the chat history of this user. Return false iff this user
does not have a document in the chat history collection.
"""
def record_chat_history(client: MongoClient, user: str, chat_history: \
                        list) -> bool:
    if find_chat_history(client, user) == True:
        return False
    
    query = {"user": user}

    db = client[db_name]
    col = db[col_name]
    doc = col.find_one(query)

    new_history = doc[col_name]
    new_history.extend(chat_history)

    col.update_one(query, {col_name: new_history})

    return True


"""Clear the chat history of this user. Return false iff this user
does not have a document in the chat history collection.
"""
def clear_chat_history(client: MongoClient, user: str) -> bool:
    if find_chat_history(client, user) == True:
        return False

    query = {"user": user}

    db = client[db_name]
    col = db[col_name]

    col.update_one(query, {col_name: []})

    return True