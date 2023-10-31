import pymongo

url = "mongodb://localhost:27017"

client = pymongo.MongoClient(url)

db = client.Infy

collection = db.Employee

if db is not None:
    print("connected")

new_data = {
    "employee_id": 10,
    "first_name": "Gayatri",
    "last_name": "Dunakhe",
    "email": "gayatri@gmail.com",
    "phone": "1234567890",
    "department": "CME",
    "position":"ASE",
    "salary":60000
}

# res = collection.insert_one(new_data)

# query = {"employee_id": 10}

# delete_res = collection.delete_one(query)

# if delete_res.deleted_count > 0:
#     print("Document deleted")

cursor = collection.find()

qury = {"employee_id": 10}

update = {"$set": {"phone": "1213141516"}}

update_res = collection.update_one(qury, update)

if update_res.modified_count > 0:
    print("Document updated")

for data in cursor:
    print(data)

client.close()
