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

from typing import NamedTuple


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
    diets: [str]

    def diets_to_string(self) -> str:
        """Returns the diets associated with this MenuItem as spaced string."""
        return " ".join(self.diets)


class Restaurant(NamedTuple):
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

    name: str
    client_id: int
    kitchen_id: int
    menu_type: int
    relevant_menus: [str]


class Marker(NamedTuple):
    """Dataclass for allergen information markings

    Attributes:
        letters (str):
            allergen markings
        explanation (str):
            extended information about the marker
    """

    letters: str
    explanation: str


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
    Restaurant("Foobar", 93077, 49, 84, ["Foobar Salad and soup", "Foobar Rohee"]),
    Restaurant("Foodoo", 93077, 48, 89, ["Foodoo Salad and soup", "Foodoo Reilu"]),
    Restaurant("Kastari", 95663, 5, 2, ["Ruokalista"]),
    Restaurant("Kylymä", 93077, 48, 92, ["Kylymä Rohee"]),
    Restaurant("Mara", 93077, 49, 111, ["Salad and soup", "Ravintola Mara"]),
    Restaurant("Napa", 93077, 48, 79, ["Napa Rohee"]),
]

MARKERS = [
    Marker("G", "Gluteeniton"),
    Marker("M", "Maidoton"),
    Marker("L", "Laktoositon"),
    Marker("SO", "Sisältää soijaa"),
    Marker("SE", "Sisältää selleriä"),
    Marker("MU", "Munaton"),
    Marker("[S], *", "Kelan korkeakouluruokailunsuosituksen mukainen"),
    Marker("SIN", "Sisältää sinappia"),
    Marker("<3", "Sydänmerkki"),
    Marker("VEG", "Vegaani"),
]
