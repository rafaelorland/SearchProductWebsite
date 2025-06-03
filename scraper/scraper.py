import re
from urllib.parse import urljoin
from typing import List
import requests
from bs4 import BeautifulSoup
from config import Settings
from model.product import Product

class MaetoScraper:
    def __init__(self, db):
        self.db = db
        self.settings = Settings()
    
    def _make_request(self, url):
        try:
            response = requests.get(
                url,
                headers=self.settings.HEADERS,
                timeout=self.settings.TIMEOUT
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro: {e}")
            return None
    
    def _extract_sku(self, url):
        return url.split('/')[-1].strip()
    
    def _parse_price(self, price_str):
        return float(re.sub(r'[^\d,]', '', price_str).replace(',', '.'))
    
    def search_products(self, search_term: str) -> List[Product]:
        products = []
        response = self._make_request(f"{self.settings.SEARCH_URL}{search_term}")
        
        if not response:
            return products
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for item in soup.find_all('div', class_='product-list-info'):
            try:
                # verificar dados revisar e retirar o print de teste a baixo
                title_tag = item.find('h4', class_='product-list-name').a
                title = title_tag.get('title', '').strip()
                product_url = urljoin(self.settings.BASE_URL, title_tag.get('href', ''))
                sku = self._extract_sku(product_url)
                
                price_box = item.find('div', class_='box-price-to')
                price = self._parse_price(price_box.find('span', class_='to-price').text.strip())
                price_in_pix = self._parse_price(price_box.find('div', class_='cash-payment-container').find('span', class_='to-price').text.strip())
                
                parcel = item.find('div', class_='product-parcel')
                installments = parcel.find('span', class_='installments-number').text.strip()
                quantity_installment = int(installments.replace('x', ''))
                installment_value = self._parse_price(parcel.find('span', class_='installments-amount').text.strip())
                
                products.append(Product(
                    sku=sku,
                    title=title,
                    price=price,
                    price_in_pix=price_in_pix,
                    installment_value=installment_value,
                    quantity_installment=quantity_installment,
                    description_technique="Ver página do produto para detalhes técnicos"
                ))
            except Exception as e:
                print(f"Erro ao processar produto: {e}")
                continue
                
        return products