from pymongo import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://chlid:childofmother@mother.gntx7mg.mongodb.net/?retryWrites=true&w=majority&appName=Mother"

# create a new client and connect to the server
def start_database():
    client = MongoClient('localhost')
    
    # send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        # print("Pinged your deployment. You successfully connected to MongoDB!")
        # print(client.list_database_names())
        return client
    except Exception as e:
        print(e)
        return None