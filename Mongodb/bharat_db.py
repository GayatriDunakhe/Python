import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db_name = 'bharat'
collection_name = 'banglore'

db = client[db_name]
collection = db[collection_name]

# Getting db details----------------------------
# document_count = collection.count_documents({})
# storage_size_bytes = db.command('collstats', collection_name)['storageSize']

# print(f"Number of Documents in {collection_name}: {document_count}")
# print(f"Storage Size of {collection_name} (Bytes): {storage_size_bytes}")

# Updating data in collection --------------------------------
# filter_criteria = {"name": "John Doe"}

# update_operation = {"$set": {"name": "Ram"}}

# result = collection.update_one(filter_criteria, update_operation)

# Updating specifice data in collection ------------------------------
data = {"name": "Ram"}

update_phno = {"$set":{"phone": "1234567890"}}

# result = collection.update_one(data, update_phno)

# if result.modified_count > 0:
#     print("Document updated successfully.")
# else:
#     print("No document found with the name 'John'.")


# Inserting new data in collection-----------------------------
new_data ={
    "name":"Gayatri",
    "age":23,
    "city":"Hyderabad",
    "phone": 1234567890
}

# insert_res = collection.insert_one(new_data)

record = [
    {
        "name":"Alice",
        "age":45,
        "city":"Pune",
        "phone": 22334455667
    },
    {
        "name":"Bob",
        "age":34,
        "city":"Banglore",
        "phone": 189094083
    },
]

# insert_res = collection.insert_many(record)

# if insert_res.inserted_id:
#     print("Data Inserted")
# else:
#     print("Data is not inserted")

# Deleting data in collection-------------------------------------
# delete_res = collection.delete_one({"name": "Ram"})

# delete_res = collection.delete_many({"name": {"Ganesh", "Tom"}})

# if delete_res.deleted_count > 0:
#     print("Document deleted")
# else:
#     print("Document is not deleted")

# Fetch data form collection -----------------------------------
# cursor = collection.find()
# print(cursor)

# Find documents where the "name" field is "Tom"-----------------------
# query = {"name":"Tom"}
# cursor = collection.find(query)

# Find documents where the "age" field is greater than or equal to 25 --------------------
# query = {"age": {"$gte": 25}}
# projection = {"name": 1, "age": 1}
# cursor = collection.find(query, projection)

# Sort documents by "age" in ascending order-----------------------------------
# cursor = collection.find().sort("age", pymongo.ASCENDING)

# Retrieve 5 documents, skipping the first 2-----------------------------
# cursor = collection.find().limit(5).skip(2)

# Find documents where "name" is "Alice" or "Bob"---------------------------
# query = {"$or": [{"name": "Alice"}, {"name": "Bob"}]}
# cursor = collection.find(query)

# Find documents where "name" starts with 'A'-------------------
# import re
# query = {"name": {"$regex": re.compile("^A")}}
# cursor = collection.find(query)

# Find documents where age is 25+ and city include "Pune" ------------------------
query = {"$and": [{"age": {"$gte": 25}}, {"city": "Pune"}]}  
cursor = collection.find(query)
print(cursor)

for data in cursor:
    print(data)

# Creating new collection in db---------------------------------
# new_collection = "Hyderabad"
# collection = db[new_collection]

# db.create_collection(new_collection)

# all_collection = db.list_collection_names()
    
# if new_collection in all_collection:
#     print("Collection is created")
# else:
#     print("Collection is not created")

client.close()