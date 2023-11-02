from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/Infy' 
mongo = PyMongo(app)
mycol = mongo.db["restaurants"]

@app.route('/')
def index():
    if mongo.db is not None:
        return "Connected to MongoDB!"
    else:
        return "Failed to connect to the database."

# Create (Insert) Operation
@app.route('/create', methods=['POST'])
def create_document():
    data = request.get_json()
    mycol.insert_one(data)
    return jsonify({"message": "Document inserted successfully!"})

# Read (Select) Operation
@app.route('/read', methods=['GET'])
def read_documents():
    documents = mycol.find()
    data_list = [doc for doc in documents]
    return jsonify(data_list)

# Update Operation
@app.route('/update', methods=['PUT'])
def update_document():
    query = request.get_json()['query']
    new_data = request.get_json()['new_data']
    mycol.update_one(query, {"$set": new_data})
    return jsonify({"message": "Document updated successfully!"})

# Delete Operation
@app.route('/delete', methods=['DELETE'])
def delete_document():
    query = request.get_json()
    mycol.delete_one(query)
    return jsonify({"message": "Document deleted successfully!"})

if __name__ == '__main__':
    app.run()
