from scraper.scraper import MaetoScraper
from database.db import Database

def main():
    print("Buscador de Produtos Loja Maeto")
    while True:
        search_term = input("Digite o produto de busca: ").strip()
    
        if not search_term:
            print("A busca não pode ser vazio.")
            return
        
        db = Database()
        scraper = MaetoScraper(db)
        
        try:
            
            products = scraper.search_products(search_term)
            if products:
                db.save_products(products)
            else:
                print("Nenhum produto encontrado.")
        finally:
            db.close()

if __name__ == "__main__":
    main()