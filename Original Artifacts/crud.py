from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    
    def __init__(self, username, password, HOST, PORT, DB, COL):
        # Use provided parameters instead of hardcoding
        self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]
        
    # Insert a new animal document into MongoDB
    def create(self, data):
        try:
            if isinstance(data, dict) and data:  # Ensure data is a non-empty dictionary
                result = self.collection.insert_one(data)
                return result.inserted_id  # Return the inserted document ID
            else:
                raise ValueError("Data must be a non-empty dictionary")
        except Exception as e:
            print("Error:", e)
            return None
                
    # Read documents based on the query
    def read(self, query={}):  # Default to empty dictionary instead of None
        try:
            return list(self.collection.find(query))
        except Exception as e:
            print("Error:", e)
            return []
        
    # Update documents based on query
    def update(self, query, new_data, multiple=False):
        try:
            if not query or not new_data:
                raise ValueError("Query and new data must be provided for an update operation.")
                
            update_data = {"$set": new_data}
            
            if multiple:
                result = self.collection.update_many(query, update_data)
            else:
                result = self.collection.update_one(query, update_data)
                
            return result.modified_count  # Return the number of modified documents
        
        except Exception as e:
            print("Error:", e)
            return 0
           
    # Delete documents based on query
    def delete(self, query, multiple=False):
        try:
            if not query:
                raise ValueError("Query must be provided for a delete operation.")
            
            if multiple:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
                
            return result.deleted_count  # Return the number of deleted documents
        
        except Exception as e:
            print("Error:", e)
            return 0
