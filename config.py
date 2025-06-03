class Settings:
    BASE_URL = "https://www.lojamaeto.com"
    SEARCH_URL = f"{BASE_URL}/search/?q="
    TIMEOUT = 15
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    DB_NAME = "products.db"