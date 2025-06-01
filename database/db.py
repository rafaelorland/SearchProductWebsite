import sqlite3

from model.product import Product

def create_table(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

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

        conn.commit()
        conn.close()

# def get_product(db_path,product: Product):
