import sqlite3
import backend.modules.product as product

"""
Database management system for management of products.
Database is connected when the class is initialized,
and disconnected when class is no longer in use.
"""


class ProductDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("products_database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                name TEXT,
                price REAL,
                category TEXT,
                image TEXT,
                unique_product_id TEXT
            )
            """
        )
        self.connection.commit()

    def add_entry(self, product: product.Product):
        self.cursor.execute(
            """
            INSERT INTO products (name, price, category, image, unique_product_id)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                product.name,
                product.price,
                product.category,
                product.image,
                product.unique_product_id,
            ),
        )
        self.connection.commit()

    def read_entry(self, product: product.Product):
        self.cursor.execute(
            """
            SELECT * FROM products WHERE unique_product_id = ?
            """,
            (product.unique_product_id,),
        )
        return self.cursor.fetchone()

    def update_entry(self, product: product.Product):
        self.cursor.execute(
            """
            UPDATE products SET name = ?, price = ?, category = ?, image = ?
            WHERE unique_product_id = ?
            """,
            (
                product.name,
                product.price,
                product.category,
                product.image,
                product.unique_product_id,
            ),
        )
        self.connection.commit()

    def remove_entry(self, product: product.Product):
        self.cursor.execute(
            """
            DELETE FROM products WHERE unique_product_id = ?
            """,
            (product.unique_product_id,),
        )
        self.connection.commit()
