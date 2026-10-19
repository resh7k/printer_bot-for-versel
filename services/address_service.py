import json
from pathlib import Path

# Путь к файлу с адресами
DATA_PATH = Path(__file__).parent.parent / "data" / "addresses.json"


def load_addresses() -> dict:
    """Загружает адреса из JSON."""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_cities() -> list:
    """Возвращает список городов."""
    data = load_addresses()
    return data.get("cities", [])


def get_buy_addresses(city: str) -> dict:
    """Возвращает адреса покупки для города."""
    data = load_addresses()
    addresses = data.get("addresses_buy", {}).get(city, {})
    map_link_key = addresses.get("map_link", "")
    map_link = data.get("map_links", {}).get(map_link_key, "")
    return {
        "main": addresses.get("main", []),
        "map_link": map_link,
    }


def get_refill_addresses(city: str) -> dict:
    """Возвращает адреса заправки для города."""
    data = load_addresses()
    addresses = data.get("addresses_refill", {}).get(city, {})
    map_link_key = addresses.get("map_link", "")
    map_link = data.get("map_links", {}).get(map_link_key, "")
    return {
        "main": addresses.get("main", []),
        "partners": addresses.get("partners", []),
        "map_link": map_link,
    }


def get_repair_addresses(city: str) -> dict:
    """Возвращает адреса ремонта для города."""
    data = load_addresses()
    addresses = data.get("addresses_repair", {}).get(city, {})
    map_link_key = addresses.get("map_link", "")
    map_link = data.get("map_links", {}).get(map_link_key, "")
    return {
        "main": addresses.get("main", []),
        "map_link": map_link,
    }
