from dataclasses import dataclass
from typing import Dict

@dataclass
class Product:
    sku: int
    title: str
    price: float
    price_in_pix: float
    installment_value: float
    quantity_installment: int
    description_technique: str

    def to_dict(self) -> Dict:
        return {
            'sku': self.sku,
            'title': self.title,
            'price': self.price,
            'price_in_pix': self.price_in_pix,
            'installment_value': self.installment_value,
            'quantity_installment': self.quantity_installment,
            'description_technique': self.description_technique
        }