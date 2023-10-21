import pymongo
import base64


class WindyDatabase:
    """
    Database management system.
    Database is connected when the class is initialized,
    and disconnected when class is no longer in use.
    """

    def __init__(self, database: str):
        # Connect to MongoDB
        self.client = pymongo.MongoClient(
            base64.b64decode(
                "bW9uZ29kYitzcnY6Ly93aW5kbnlwOmNoaWNrZW5yaWNlNDIwQHdpbmR5Y2x1c3Rlci56ZXlvZjNtLm1vbmdvZGIubmV0Lz9yZXRyeVdyaXRlcz10cnVlJnc9bWFqb3JpdHk="
            ).decode("utf-8")
        )
        try:
            self.client.admin.command("ping")
            print("MongoDB Atlas connection successful.")
        except Exception as e:
            print(e)
        self.db = self.client["KayBee"]
        self.collection = self.db[database]

    def get_all_entries(self):
        """Get all documents from the collection"""
        return list(self.collection.find())

    def add_entry(self, data: dict):
        """Insert a new document into the collection"""
        self.collection.insert_one(data)

    def read_entry(self, uuid: str):
        """Find a document in the collection by unique_id"""
        return self.collection.find_one({"unique_id": uuid})

    def update_entry(self, uuid: str, data: dict):
        """Update a document in the collection by unique_id"""
        self.collection.update_one({"unique_id": uuid}, {"$set": data})

    def remove_entry(self, uuid: str):
        """Remove a document from the collection by unique_id"""
        self.collection.delete_one({"unique_id": uuid})
