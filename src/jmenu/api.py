"""api.py

Contains functions used to wrangle the JAMIX API.
This file can be imported and exposes the following functions:

    * fetch_restaurant
    * parse_items
    * get_menu_items

The following constants are also exposed:
    
    * API_URL
"""


import requests
from datetime import datetime
from .classes import Restaurant, MenuItem, SKIPPED_ITEMS

API_URL = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu"


def fetch_restaurant(rest: Restaurant, fetch_date: datetime) -> list[dict]:
    """Return the JSON response containing all menu information for [Restaurant]

    Parameters
    ----------
    rest : Restaurant
        dataclass containing relevant restaurant information, see classes.RESTAURANTS
    fetch_date : datetime
        datetime object used to fetch the date specified menu

    Returns
    -------
    list[dict]
        parsed response json
    """
    response = requests.get(
        f"{API_URL}/{rest.client_id}/{rest.kitchen_id}?lang=fi&date={fetch_date.strftime('%Y%m%d')}",
        timeout=5,
    )
    return response.json()


def get_menu_items(rest: Restaurant, fetch_date: datetime) -> list[MenuItem]:
    """Returns a list of restaurant [MenuItems]

    Parameters
    ----------
    rest : Restaurant
        dataclass containing relevant restaurant information, see classes.RESTAURANTS
    fetch_date : datetime
        datetime object used to fetch the date specified menu

    Returns
    -------
    list[MenuItem]
        list of restaurant menu items, see classes.MenuItem
    """
    data = fetch_restaurant(rest, fetch_date)
    items = parse_items(data, rest.relevant_menus)
    return items


def parse_items(data: list[dict], relevant_menus: list[str] = []) -> list[MenuItem]:
    """Returns a list of [MenuItems] parsed from JSON data

    Parameters
    ----------
    data : list[dict]
        parsed JSON response from the jamix API, see api._fetch_restaurant
    relevant_menus : list[str]
        list of menu names to consider when parsing
        defaults to empty list

    Returns
    -------
    list[MenuItem]
        list of restaurant menu items, see classes.MenuItem"""
    menus = []
    for kitchen in data:
        for m_type in kitchen["menuTypes"]:
            if len(relevant_menus) == 0 or m_type["menuTypeName"] in relevant_menus:
                menus.extend(m_type["menus"])
    if len(menus) == 0:
        return []
    items = []
    for menu in menus:
        day = menu["days"][0]
        mealopts = day["mealoptions"]
        sorted(mealopts, key=lambda x: x["orderNumber"])
        for opt in mealopts:
            for item in opt["menuItems"]:
                if item["name"] not in SKIPPED_ITEMS:
                    items.append(MenuItem(item["name"], item["diets"]))
    return items
