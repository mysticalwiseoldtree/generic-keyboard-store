import pymongo

import dns
import modules.product as product

"""
Database management system for management of products.
Database is connected when the class is initialized,
and disconnected when class is no longer in use.
"""


class ProductDatabase:
    def __init__(self):
        # Connect to MongoDB
        self.client = pymongo.MongoClient("127.0.0.1", 27017)
        self.db = self.client["KayBee"]
        self.collection = self.db["products"]

    def add_entry(self, product: product.Product):
        # Insert a new document into the collection
        self.collection.insert_one(
            {
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "category": product.category,
                "image": product.image,
                "unique_product_id": product.unique_product_id,
            }
        )

    def read_entry(self, product: product.Product):
        # Find a document in the collection by unique_product_id
        return self.collection.find_one(
            {"unique_product_id": product.unique_product_id}
        )

    def update_entry(self, product: product.Product):
        # Update a document in the collection by unique_product_id
        self.collection.update_one(
            {"unique_product_id": product.unique_product_id},
            {
                "$set": {
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "category": product.category,
                    "image": product.image,
                }
            },
        )

    def remove_entry(self, product: product.Product):
        # Remove a document from the collection by unique_product_id
        self.collection.delete_one({"unique_product_id": product.unique_product_id})
