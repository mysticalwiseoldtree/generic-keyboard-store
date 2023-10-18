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
                brand TEXT,
                image TEXT,
                uniqueid TEXT
            )
            """
        )
        self.connection.commit()

    def add_entry(self, product: product.Product):
        self.cursor.execute(
            """
            INSERT INTO products (name, price, brand, image, uniqueid)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                product.name,
                product.price,
                product.brand,
                product.image,
                product.uniqueid,
            ),
        )
        self.connection.commit()

    def read_entry(self, product: product.Product):
        self.cursor.execute(
            """
            SELECT * FROM products WHERE uniqueid = ?
            """,
            (product.uniqueid,),
        )
        return self.cursor.fetchone()

    def update_entry(self, product: product.Product):
        self.cursor.execute(
            """
            UPDATE products SET name = ?, price = ?, brand = ?, image = ?
            WHERE uniqueid = ?
            """,
            (
                product.name,
                product.price,
                product.brand,
                product.image,
                product.uniqueid,
            ),
        )
        self.connection.commit()

    def remove_entry(self, product: product.Product):
        self.cursor.execute(
            """
            DELETE FROM products WHERE uniqueid = ?
            """,
            (product.uniqueid,),
        )
        self.connection.commit()
