"""
Contains dataclasses jmenu uses to manage data.
This file can be imported and exposes the following classes:

    * MenuItem
    * Restaurant
    * Marker

The following collections are use-case specific to the University of Oulu:

    * MARKERS
    * RESTAURANTS
    * SKIPPED_ITEMS
"""

from collections.abc import Iterable, Mapping
from datetime import datetime
from typing import NamedTuple

import requests


class MenuItem(NamedTuple):
    """Dataclass for single menu items and their properties

    Attributes:
        name (str):
            name of the dish
        diets ([str]):
            list of allergen markers

    Methods:
        diets_to_string: returns the list of diets as a joined string.
    """

    name: str
    diets: Iterable[str]

    def diets_to_string(self) -> str:
        """Returns the diets associated with this MenuItem as spaced string."""
        return " ".join(self.diets)


class Restaurant:
    name: str

    def __init__(self, name: str):
        self.name = name


class MealdooRestaurant(Restaurant):
    menu_name: str

    def __init__(self, name: str, menu_name: str):
        self.menu_name = menu_name
        Restaurant.__init__(self, name)


class JamixRestaurant(Restaurant):
    """Dataclass for relevant restaurant information

    Attributes:
        name (str):
            name of the restaurant
        client_id (int):
            internal jamix identifier used for restaurant providers
        kitchen_id (int):
            internal jamix identifier used to assign menu content
        menu_type (int):
            internal jamix identifier used to classify menus based on content
        relevant_menus ([str]):
            menu names used for filtering out desserts etc.
    """

    client_id: int
    kitchen_id: int
    menu_type: int
    relevant_menus: Iterable[str]

    def __init__(self, name, client_id, kitchen_id, menu_type, relevant_menus):
        Restaurant.__init__(self, name)
        self.client_id = client_id
        self.menu_type = menu_type
        self.kitchen_id = kitchen_id
        self.relevant_menus = relevant_menus


class Marker(NamedTuple):
    """Dataclass for allergen information markings

    Attributes:
        letters (str):
            allergen markings
        explanation (dict):
            extended information about the marker, in lang_code: explanation pairs.


    Methods:
        get_explanation(lang: str): returns the explanation string for this Marker. Defaults to english.
    """

    letters: str
    explanation: Mapping

    def get_explanation(self, lang_code: str = "en"):
        "Returns the explanation in the language specified by lang_code. Defaults to english."
        exp = self.explanation.get(lang_code)
        return exp if exp is not None else f"No explanation available for '{lang_code}'"


# TODO: Remove extra space when the API response is fixed
SKIPPED_ITEMS = [
    "proteiinilisäke",
    "Täysjyväriisi",
    "Lämmin kasvislisäke",
    "Höyryperunat",
    "Tumma pasta",
    "Meillä tehty perunamuusi",
    "Mashed Potatoes",
    "Dark Pasta",
    "Whole Grain Rice",
    "Hot Vegetable  Side",  # note the extra space
]

RESTAURANTS = [
    JamixRestaurant("Foobar", 93077, 69, 84, ["Foobar Salad and soup", "Foobar Rohee"]),
    JamixRestaurant("Foodoo", 93077, 48, 89, ["Foodoo Salad and soup", "Foodoo Reilu"]),
    # JamixRestaurant("Kastari", 95663, 5, 2, ["Ruokalista"]),
    JamixRestaurant("Kylymä", 93077, 48, 92, ["Kylymä Rohee"]),
    MealdooRestaurant("Julinia", "ravintolajulinia"),
    JamixRestaurant("Mara", 93077, 49, 111, ["Salad and soup", "Ravintola Mara"]),
    JamixRestaurant("Napa", 93077, 48, 79, ["Napa Rohee"]),
]

MARKERS = [
    Marker("G", {"fi": "Gluteeniton", "en": "Gluten-free"}),
    Marker("M", {"fi": "Maidoton", "en": "Milk-free"}),
    Marker("L", {"fi": "Laktoositon", "en": "Lactose-free"}),
    Marker("SO", {"fi": "Sisältää soijaa", "en": "Contains soy"}),
    Marker("SE", {"fi": "Sisältää selleriä", "en": "Includes cellery"}),
    Marker("MU", {"fi": "Munaton", "en": "Egg-free"}),
    Marker(
        "[S], *",
        {
            "fi": "Kelan korkeakouluruokailunsuosituksen mukainen",
            "en": "Matches recommendation standards provided by KELA",
        },
    ),
    Marker("SIN", {"fi": "Sisältää sinappia", "en": "Contains mustard"}),
    Marker("<3", {"fi": "Sydänmerkki", "en": "Better choice indicator"}),
    Marker("VEG", {"fi": "Vegaani", "en": "Vegan"}),
]


class ApiEndpoint:
    baseUrl: str

    def create_url_for_restaurant(restaurant: Restaurant):
        pass

    def parse_items() -> list[MenuItem]:
        pass


class MealdooApi(ApiEndpoint):
    baseUrl = "https://api.fi.poweresta.com/publicmenu/dates/uniresta"

    def create_url_for_restaurant(
        self, restaurant: MealdooRestaurant, date: datetime
    ) -> str:
        return f"{self.baseUrl}/{restaurant.name.lower()}/?menu={restaurant.menu_name}&dates={date.strftime('%Y-%m-%d')}"

    def parse_items(self, data: list[dict], lang_code: str) -> list[MenuItem]:
        items = []
        for result in data:
            try:
                options = result["data"]["mealOptions"]
                for opt in options:
                    for row in opt["rows"]:
                        title = "???"
                        diets = []
                        for name in row["names"]:
                            if name["language"] == lang_code and name["name"]:
                                title, *extra_diets = name["name"].split(",")
                                diets.extend(extra_diets)

                        for diet in row["diets"]:
                            if diet["language"] == lang_code and diet["dietShorts"]:
                                diets.extend(diet["dietShorts"])

                        items.append(MenuItem(title, set(diets)))
            except Exception:
                pass

        return items


class JamixApi(ApiEndpoint):
    baseUrl = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu"

    def create_url_for_restaurant(
        self,
        restaurant: JamixRestaurant,
        date: datetime,
        lang_code="en",
    ) -> str:
        return f"{self.baseUrl}/{restaurant.client_id}/{restaurant.kitchen_id}?lang={lang_code}&date={date.strftime('%Y%m%d')}"

    def parse_items(
        self, data: list[dict], relevant_menus: list[str]
    ) -> list[MenuItem]:
        """Returns a list of [MenuItems] parsed from JSON data

        Parameters:
            data (list[dict]):
                parsed JSON response from the jamix API, see api._fetch_restaurant
            relevant_menus (list[str]):
                list of menu names to filter when parsing
                defaults to all menus

        Returns:
            (list[MenuItem]):
                list of restaurant menu items
        """
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
                    if item["name"] not in SKIPPED_ITEMS and len(item["name"]) > 0:
                        items.append(MenuItem(item["name"], item["diets"].split(",")))
        return items


class MenuItemFactory:
    jamix = JamixApi()
    mealdoo = MealdooApi()

    def get_menu_items(
        self,
        restaurant: JamixRestaurant | MealdooRestaurant,
        date: datetime,
        lang_code="en",
    ) -> list[MenuItem]:
        if type(restaurant) is JamixRestaurant:
            url = self.jamix.create_url_for_restaurant(restaurant, date, lang_code)
            data = requests.get(url, timeout=5).json()
            return self.jamix.parse_items(data, restaurant.relevant_menus)

        elif isinstance(restaurant, MealdooRestaurant):
            url = self.mealdoo.create_url_for_restaurant(restaurant, date)
            data = requests.get(url, timeout=5).json()
            return self.mealdoo.parse_items(data, lang_code)
