from jmenu.api import parse_items, fetch_restaurant
from jmenu.classes import RESTAURANTS
from conftest import get_json, mock_fetch_restaurant
from unittest.mock import patch
from datetime import datetime


@patch("jmenu.api.requests.get", side_effect=mock_fetch_restaurant)
def test_fetch_restaurant(self):
    rest = list(filter(lambda x: x.name == "Mara", RESTAURANTS)).pop()
    assert fetch_restaurant(rest, datetime.now(), lang_code="fi") == get_json()


def test_parsing_with_defaults():
    items = parse_items(get_json())
    assert items[0].name is not None
    assert len(items) == 20  # base menu contains 20 items


def test_parsing_with_rest_values():
    rest = list(filter(lambda x: x.name == "Mara", RESTAURANTS)).pop()
    assert rest is not None
    items = parse_items(get_json(), rest.relevant_menus)
    assert len(items) == 6  # Mara relevant menu should result in 6 items
