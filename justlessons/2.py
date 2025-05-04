import requests
import time

# Параметры поиска
MIN_DISCOUNT = 20  # Минимальная скидка %
MAX_PRICE = 100    # Максимальная цена в $
CHECK_INTERVAL = 60  # Проверка каждые 60 сек

def get_steam_market_items(game="csgo", currency=1):
    url = f"https://steamcommunity.com/market/search/render/?query=&start=0&count=100&search_descriptions=0&sort_column=price&sort_dir=asc&appid=730&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    return []

def check_discount(item):
    original_price = item.get("original_price", 0) or 0
    if isinstance(original_price, str):
        original_price = float(original_price.strip('$'))
    current_price = float(item["sell_price_text"].strip('$'))
    if original_price > 0:
        discount = ((original_price - current_price) / original_price) * 100
        return discount >= MIN_DISCOUNT and current_price <= MAX_PRICE
    return False

def main():
    print("Мониторинг Steam Market...")
    while True:
        items = get_steam_market_items()
        for item in items:
            if check_discount(item):
                print(f"🔥 Найдена выгодная вещь: {item['name']}")
                print(f"💰 Цена: ${item['sell_price_text']}")
                print(f"🔗 Ссылка: https://steamcommunity.com/market/listings/730/{item['hash_name']}")
                print("-" * 50)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()