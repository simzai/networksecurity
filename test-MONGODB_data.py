import collections.abc
import collections
collections.MutableMapping = collections.abc.MutableMapping


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://ksimranjuneja19:anhad22@cluster0.yckidvn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)