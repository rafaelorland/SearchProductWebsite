import sqlite3

from config import DB_PATH
from model.product import Product

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH['database'])
        self._create_tables()

    def create_table(self):
            
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
            

    # def get_product(db_path,product: Product):
