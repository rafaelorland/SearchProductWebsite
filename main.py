from scraper.scraper import MaetoScraper
from database.db import Database

def main():
    print(("="*6)+" Buscador de Produtos - Loja Maeto "+("="*6))
    
    while True:
        search_term = input("Digite o nome do produto para buscar ou digite (sair) para encerrar: ").strip()

        if search_term.lower() == 'sair':
            print(("="*6)+" Encerrando o buscador "+("="*6))
            break

        if not search_term:
            print("O termo de busca não pode estar vazio.")
            continue
        
        db = Database()
        scraper = MaetoScraper(db)
        
        try:
            products = scraper.search_products(search_term)
            if products:
                db.save_products(products)
            else:
                print("Nenhum produto encontrado para essa busca.")
        finally:
            db.close()

if __name__ == "__main__":
    main()
