## Gayatri Dunakhe
## Wavw2-B1-Python
## MongoDB with Python:

1. What is MongoDB, and why is it called a NoSQL database?
- MongoDB is a popular NoSQL database management system that is designed to store and manage large volumes of unstructured or semi-structured data. 
- It is called a NoSQL database because it does not rely on a traditional relational database management system (RDBMS) structure with tables and rows. 
- Instead, MongoDB stores data in a flexible and schema-less format using collections and documents. 
- NoSQL databases like MongoDB are often chosen for their scalability, flexibility, and ability to handle diverse data types efficiently.

2. How can you install PyMongo, the Python driver for MongoDB?
- To install PyMongo, the Python driver for MongoDB, we can use the Python package manager pip. 
- Steps - 
    - Open a terminal or command prompt
    - Then run - 
    ```pip install pymongo```

3. What is a document in MongoDB, and how is it different from a row in a relational database?
- In MongoDB, a document is a basic unit of data storage, and it is analogous to a row in a relational database table. 
- However, documents in MongoDB are stored in a JSON-like format called BSON (Binary JSON), which allows for flexible and nested data structures. 
- Unlike rows in a relational database, documents in MongoDB can have different fields and structures within the same collection, making MongoDB a schema-less database.

4. How do you create a new database in MongoDB using PyMongo?
- To create a new database in MongoDB using PyMongo, we don't need to explicitly create one. 
- MongoDB creates a new database when we first insert data into it. 
- We can specify the database name when connecting to MongoDB using the MongoClient constructor. 
- For example:
```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["mydatabase"] 

```

5. What is a collection in MongoDB, and how can you create one using PyMongo?
- In MongoDB, a collection is a group of MongoDB documents, similar to a table in a relational database. 
- Collections do not require a predefined schema, and documents within a collection can have different fields. 
- We can create a new collection using PyMongo by simply inserting documents into it. 
- When we insert data into a collection that doesn't exist, MongoDB creates the collection automatically.

6. How do you insert a single document into a MongoDB collection using PyMongo?
- To insert a single document into a MongoDB collection using PyMongo, ywe can use the `insert_one()` method. 
- For example:
```python

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

res = collection.insert_one(new_data)
```

7. How can you find and retrieve documents from a MongoDB collection using PyMongo?
- You can find and retrieve documents from a MongoDB collection using PyMongo's `find()` method.
- The find() method allows you to specify query criteria to filter the results. 
- For example:
```python
cursor = collection.find()

for data in cursor:
    print(data)

client.close()

```

8. What is the `_id` field in MongoDB, and why is it important?
- The `_id `field in MongoDB is a unique identifier automatically assigned to each document in a collection. 
- It serves as the primary key for the document and ensures its uniqueness within the collection. 
- We can provide own `_id` value when inserting a document, or MongoDB will generate one for us if it's not provided. 
- The `_id` field is important because it enables efficient retrieval and updates of specific documents.

9. How do you update a specific document in a MongoDB collection using PyMongo?
- To update a specific document in a MongoDB collection using PyMongo, we can use the `update_one()` method. 
-For example:
```python
qury = {"employee_id": 10}

update = {"$set": {"phone": "1213141516"}}

update_res = collection.update_one(qury, update)
```

10. What is the purpose of indexing in MongoDB, and how can you create an index using PyMongo?
- Indexing in MongoDB improves query performance by allowing MongoDB to efficiently look up documents based on specific fields. 
- We can create an index using PyMongo's `create_index()` method on a collection. 
- For example:
```python
collection.create_index([("name", pymongo.ASCENDING)])
```

11. How can you delete a document from a MongoDB collection using PyMongo?
- To delete a document from a MongoDB collection using PyMongo, you can use the `delete_one()` method to delete a single document or the `delete_many()` method to delete multiple documents that match specific criteria. 
- For example:
```python
query = {"employee_id": 10}

result = collection.delete_one(query)
```

12. What is aggregation in MongoDB, and what kind of operations can you perform using it in PyMongo?
- Aggregation in MongoDB allows us to perform complex data transformations and computations on data stored in collections. 
- We can use aggregation pipelines to combine multiple stages, including filtering, grouping, sorting, and more, to process and analyze data. 
- PyMongo provides methods like `aggregate()` to perform aggregation operations.

13. How do you count the number of documents in a MongoDB collection using PyMongo?
- To count the number of documents in a MongoDB collection using PyMongo, we can use the `count_documents()` method.
- For example:
```python
count = collection.count_documents({})
print(count)
``` 

14. What are some common data types used in MongoDB documents?
- Common data types used in MongoDB documents include strings, numbers, arrays, nested documents, dates, and object IDs. 
- MongoDB's BSON format supports a wide range of data types, making it flexible for different data structures.

15. How can you sort the results of a query in MongoDB using PyMongo?
- We can sort the results of a query in MongoDB using PyMongo's `sort()` method. 
- For example:
```python
cursor = collection.find().sort("age", pymongo.ASCENDING)
```