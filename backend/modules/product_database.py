import sqlite3
import modules.keyboards as keyboards

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
            CREATE TABLE IF NOT EXISTS keyboards (
                name TEXT,
                price REAL,
                brand TEXT,
                image TEXT,
                switch_type TEXT,
                uniqueid TEXT
            )
            """
        )
        self.connection.commit()

    def add_entry(self, product: keyboards.Keyboard):
        self.cursor.execute(
            """
            INSERT INTO keyboards (name, price, brand, image, switch_type, uniqueid)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                product.name,
                product.price,
                product.brand,
                product.image,
                product.switch_type,
                product.uniqueid,
            ),
        )
        self.connection.commit()

    def read_entry(self, product: keyboards.Keyboard):
        self.cursor.execute(
            """
            SELECT * FROM keyboards WHERE uniqueid = ?
            """,
            (product.uniqueid,),
        )
        return self.cursor.fetchone()

    def update_entry(self, product: keyboards.Keyboard):
        self.cursor.execute(
            """
            UPDATE keyboards SET name = ?, price = ?, brand = ?, image = ?, switch_type = ?
            WHERE uniqueid = ?
            """,
            (
                product.name,
                product.price,
                product.brand,
                product.image,
                product.switch_type,
                product.uniqueid,
            ),
        )
        self.connection.commit()

    def remove_entry(self, product: keyboards.Keyboard):
        self.cursor.execute(
            """
            DELETE FROM keyboards WHERE uniqueid = ?
            """,
            (product.uniqueid,),
        )
        self.connection.commit()
