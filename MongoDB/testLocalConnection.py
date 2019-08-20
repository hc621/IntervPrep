from pymongo import MongoClient
import pprint


MONGO_HOST = "54.85.175.129"
MONGO_PORT = 27017
MONGO_DB = "scar"
MONGO_USER = "hchen"
MONGO_PASS = "Heron7056"

client = MongoClient(MONGO_HOST,MONGO_PORT)
db=client[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

collection=db.test_collection
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"]}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print()
db.list_collection_names()
pprint.pprint(posts.find_one())
'''

''''''

client = MongoClient('mongodb://hchen:Heron7056@54.85.175.129/scar')

'''