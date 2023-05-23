from version import VERSION
from collections import namedtuple
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import argparse
from time import time


Restaurant = namedtuple("Restaurant", ["name", "url"])


urls = [
    Restaurant("Foobar", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=84"),
    Restaurant("Foodoo", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=89"),
    Restaurant("Kastari", "https://fi.jamix.cloud/apps/menu/?anro=95663&k=5&mt=2"),
    Restaurant("Kylmä", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=92"),
    Restaurant("Mara", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=111"),
    Restaurant("Napa", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=79"),
]


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

    highlight = []
    if args.allergens:
        highlight = [" " + x.upper() for x in args.allergens]
    print_menu(highlight)
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


def print_menu(highlight: list[str]):
    date = datetime.now()
    print("-" * 79)
    print("Menu for", date.strftime("%d.%m"))
    print("-" * 79)
    for res in urls:
        try:
            items = parse_soup(get_soup(res.url))
            if len(items) == 0:
                print(res.name, "\t --")
            else:
                print(res.name)
                for item in items:
                    if highlight and all(marker in item for marker in highlight):
                        print("\033[92m", "\t", item, "\033[0m")
                    else:
                        print("\t", item)
        except Exception:
            print("Couldn't fetch menu for", res.name)
