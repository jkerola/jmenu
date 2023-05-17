from version import VERSION
from sys import argv, exit
from collections import namedtuple
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

Restaurant = namedtuple("Restaurant", ["name", "url"])

urls = [
    Restaurant("Kastari", "https://fi.jamix.cloud/apps/menu/?anro=95663&k=5&mt=2"),
    Restaurant("Foodoo", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=89"),
    Restaurant("Foobar", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=84"),
    Restaurant("Napa", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=79"),
    Restaurant("Kylmä", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=92"),
]


def parse_args(args: argv):
    if "--help" in args:
        print_usage()
        exit(0)
    elif "--version" in args:
        print(VERSION)
        exit(0)
    elif len(args) >= 2:
        print("Error: Unrecognized command")
        exit(1)


def get_selenium_opts() -> Options:
    opts = Options()
    opts.add_argument("--headless")
    return opts


def print_usage():
    print(
        f"""Juvenes menu fetcher {VERSION}
Flags:
    --help          # Print this usage information
    --version       # Print version information
""",
    )


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


def print_menu():
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
                    print("\t", item)
        except Exception:
            print("Couldn't fetch menu for", res.name)
