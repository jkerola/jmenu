from version import VERSION
from restaurants import RESTAURANTS, MARKINGS, API_URL, SKIPPED_ITEMS, Restaurant
from datetime import datetime
import requests
import argparse
from time import time


class ArgsNamespace:
    explain: bool
    allergens: list[str]


def main():
    args = get_args()
    if args.explain:
        print_explanations()
        exit(0)
    start = time()
    print_menu(args)
    print("Process took {:.2f} seconds.".format(time() - start))


def get_args():
    parser = argparse.ArgumentParser(
        description="Display University of Oulu restaurant menus for the day."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Display version information",
        version=VERSION,
    )
    parser.add_argument(
        "-e",
        "--explain",
        dest="explain",
        action="store_true",
        help="Display allergen and marking information",
    )

    allergens = parser.add_argument_group("highlighting allergens")
    allergens.add_argument(
        "-a",
        "--allergens",
        dest="allergens",
        action="extend",
        type=str,
        metavar=("letters", "G, VEG"),
        nargs="+",
        help='List of allergens, ex. "g veg"',
    )
    return parser.parse_args(namespace=ArgsNamespace())


def get_restaurant_menu_items(rest: Restaurant) -> list[dict]:
    today = datetime.now().strftime("%Y%m%d")
    response = requests.get(
        f"{API_URL}/{rest.client_id}/{rest.kitchen_id}?lang=fi&date={today}"
    )
    data = response.json()
    menus = get_menus(data, rest)
    if len(menus) == 0:
        return []
    items = get_menu_items(menus, rest)
    return items


def get_menu_items(menus: dict, rest: Restaurant) -> list[dict]:
    items = []
    for menu in menus:
        day = menu["days"][0]
        mealopts = day["mealoptions"]
        sorted(mealopts, key=lambda x: x["orderNumber"])
        for opt in mealopts:
            for item in opt["menuItems"]:
                if item["name"] not in SKIPPED_ITEMS:
                    items.append(item)
    return items


def get_menus(data: dict, rest: Restaurant) -> list[dict]:
    menus = []
    for kitchen in data:
        for m_type in kitchen["menuTypes"]:
            if m_type["menuTypeName"] in rest.relevant_menus:
                menus.extend(m_type["menus"])
    return menus


def print_menu(args: ArgsNamespace):
    allergens = []
    if args.allergens:
        allergens = [x.upper() for x in args.allergens]

    print_header()
    for res in RESTAURANTS:
        try:
            items = get_restaurant_menu_items(res)
            sorted(items, key=lambda x: x["orderNumber"])
            if len(items) == 0:
                print(res.name, "\t --")
            else:
                print(res.name)
                if not allergens:
                    for item in items:
                        print("\t", item["name"], item["diets"])
                else:
                    print_highlight(items, allergens)

        except Exception as e:
            print(e.with_traceback())
            print("Couldn't fetch menu for", res.name)


def print_explanations():
    for mark in MARKINGS:
        print(mark.letters, "\t", mark.explanation)


def print_highlight(items: list[str], allergens: list[str]):
    print(
        allergens,
    )
    for item in items:
        diets = item["diets"].split(",")
        diets = [marker.strip() for marker in diets]
        if all(marker in diets for marker in allergens):
            print("\033[92m", "\t", item["name"], item["diets"], "\033[0m")
        else:
            print("\t", item["name"], item["diets"])


def print_header():
    date = datetime.now()
    print("-" * 79)
    print("Menu for", date.strftime("%d.%m"))
    print("-" * 79)
