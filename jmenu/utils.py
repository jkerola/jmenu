from version import VERSION
from restaurants import RESTAURANTS
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import argparse
from time import time


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
        "--hide",
        action="store_true",
        help="Hide bad results instead of highlighting good ones",
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
    parser.add_argument_group
    return parser.parse_args()


def main():
    args = get_args()
    start = time()

    allergens = []
    if args.allergens:
        allergens = [" " + x.upper() for x in args.allergens]
    print_menu(allergens, args.hide)
    print("Process took {:.2f} seconds.".format(time() - start))


def get_selenium_opts() -> Options:
    opts = Options()
    opts.add_argument("--headless")
    return opts


def get_soup(url: str) -> BeautifulSoup:
    try:
        driver = webdriver.Chrome(options=get_selenium_opts())
        driver.get(url)
        cond = expected_conditions.presence_of_element_located(
            (
                By.CLASS_NAME,
                "v-customlayout-header",
            )
        )
        WebDriverWait(driver, 5).until(cond)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        return soup
    except Exception:
        pass


def parse_soup(soup: BeautifulSoup) -> list[str]:
    results = soup.find_all("div", attrs={"class": "menu-sub-view"})
    if len(results) == 0:
        return []
    results = soup.find_all("span", attrs={"class": "menu-item"})
    menu = []
    for result in results:
        menu.append(result.text)
    return menu


def print_menu(allergens: list[str], hide: bool = False):
    date = datetime.now()
    print("-" * 79)
    print("Menu for", date.strftime("%d.%m"))
    print("-" * 79)
    for res in RESTAURANTS:
        try:
            items = parse_soup(get_soup(res.url))
            if len(items) == 0:
                print(res.name, "\t --")
            else:
                print(res.name)
                if not allergens:
                    for item in items:
                        print("\t", item)
                else:
                    if not hide:
                        print_highlight(items, allergens)
                    else:
                        print_hide(items, allergens)

        except Exception:
            print("Couldn't fetch menu for", res.name)


def print_hide(items: list[str], allergens: list[str]):
    for item in items:
        if any(marker in item for marker in allergens):
            print("\t", item)


def print_highlight(items: list[str], allergens: list[str]):
    for item in items:
        if any(marker in item for marker in allergens):
            print("\033[92m", "\t", item, "\033[0m")
        else:
            print("\t", item)
