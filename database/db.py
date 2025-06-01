import sqlite3
from typing import List

from config import DB_PATH
from model.product import Product

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self._create_tables()

    def _create_tables(self):
            
            cursor = self.conn.cursor()

            cursor.execute("""

            CREATE TABLE IF NOT EXISTS products (
                sku INTEGER PRIMARY KEY,
                title TEXT,
                price REAL,
                price_in_pix REAL,
                installment_value REAL,
                quantity_installment INTEGER,
                description_technique TEXT
            );

            """)

            self.conn.commit()

    def save_products(self, products: List[Product]):
        cursor = self.conn.cursor()

        for product in products:

            cursor.execute("""

                INSERT OR REPLACE INTO products
                VALUES (:sku, :title, :price, :price_in_pix, :installment_value, :quantity_installment, :description_technique)

            """,
            product.to_dict())

        self.conn.commit()

    def close(self):
        self.conn.close()
