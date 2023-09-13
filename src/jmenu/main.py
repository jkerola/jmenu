"""main.py

This file contains the logic for executing jmenu from the command line.
This file can be imported and exposes the following functions:
    * main
"""

from .version import VERSION
from .classes import RESTAURANTS, MARKERS, MenuItem
from .api import get_menu_items
from datetime import datetime, timedelta
import argparse
from time import time


class _ArgsNamespace:
    """Dataclass for managing command line arguments

    Attributes
    ---
    explain : bool
        print allergen marker info
    allergens : list[str]
        highlight the provided allergen markers
    tomorrow: bool
        fetch the menus for tomorrow
    """

    explain: bool
    allergens: list[str]
    tomorrow: bool


def main():
    """Fetch and print restaurant menus"""
    args = _get_args()
    if args.explain:
        _print_explanations()
        exit(0)
    start = time()
    _print_menu(args)
    print("Process took {:.2f} seconds.".format(time() - start))


def _get_args():
    parser = argparse.ArgumentParser(
        description="Display University of Oulu restaurant menus for the day"
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="display version information",
        version=VERSION,
    )
    parser.add_argument(
        "-e",
        "--explain",
        dest="explain",
        action="store_true",
        help="display allergen marking information",
    )
    parser.add_argument(
        "-t",
        "--tomorrow",
        dest="tomorrow",
        action="store_true",
        help="display menus for tomorrow",
    )
    allergens = parser.add_argument_group("allergens")
    allergens.add_argument(
        "-a",
        "--allergens",
        dest="allergens",
        action="extend",
        type=str,
        metavar=("markers", "G, VEG"),
        nargs="+",
        help='list of allergens, for ex. "g veg"',
    )
    return parser.parse_args(namespace=_ArgsNamespace())


def _print_menu(args: _ArgsNamespace):
    fetch_date = datetime.now()
    if args.tomorrow:
        fetch_date += timedelta(days=1)

    allergens = []
    if args.allergens:
        allergens = [x.lower() for x in args.allergens]

    _print_header(fetch_date)
    for res in RESTAURANTS:
        try:
            items = get_menu_items(res, fetch_date)
            if len(items) == 0:
                print(res.name.ljust(8), "--")
            else:
                print(res.name)
                if not allergens:
                    print(*[f"\t {item.name} {item.diets}" for item in items], sep="\n")
                else:
                    _print_highlight(items, allergens)

        except Exception:
            print("Couldn't fetch menu for", res.name)


def _print_explanations():
    for mark in MARKERS:
        print(mark.letters, "\t", mark.explanation)


def _print_highlight(items: list[MenuItem], allergens: list[str]):
    for item in items:
        diets = [diets.strip().lower() for diets in item.diets.split(",")]
        if all(marker in diets for marker in allergens):
            print("\033[92m", "\t", item.name, item.diets, "\033[0m")
        else:
            print("\t", item.name, item.diets)


def _print_header(fetch_date: datetime):
    print("-" * 79)
    print("Menu for", fetch_date.strftime("%d.%m"))
    print("-" * 79)


if __name__ == "__main__":
    main()
