import sqlite3
from typing import List
from model.product import Product
from config import Settings

class Database:
    def __init__(self, db_name=Settings.DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self._init_db()
    
    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            sku TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            price_in_pix REAL NOT NULL,
            installment_value REAL NOT NULL,
            quantity_installment INTEGER NOT NULL,
            description_technique TEXT,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        self.conn.commit()
    
    def save_products(self, products: List[Product]):
        cursor = self.conn.cursor()
        
        for product in products:
            cursor.execute('''
            INSERT OR REPLACE INTO products(sku, title, price, price_in_pix, installment_value, quantity_installment, description_technique)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',
                (
                    product.sku,
                    product.title,
                    product.price,
                    product.price_in_pix,
                    product.installment_value,
                    product.quantity_installment,
                    product.description_technique
                )
            )

        self.conn.commit()
        print(f"{len(products)} produtos salvos/atualizado.")
    
    def close(self):
        self.conn.close()