# jmenu

## About

Python app to fetch University of Oulu restaurant menus from Jamix API.

Versions below 1.3 work by rendering the pages with selenium, then scraping the HTML with BeautifulSoup4.

Versions 1.3 and above use the API at [https://fi.jamix.cloud/apps/menuservice/rest](https://fi.jamix.cloud/apps/menuservice/rest)

# Installing

Jmenu is available for install on the [Python package index.](https://pypi.org/project/jmenu/)

Install it with pip:

```shell
pip install jmenu
```

#

| Argument        | Example | Description                             |
| :-------------- | :------ | :-------------------------------------- |
| -a, --allergens | g veg   | Highlights appropriately marked results |

| Flag           | Description                     |
| :------------- | :------------------------------ |
| -t, --tomorrow | Fetch menu results for tomorrow |
| -h, --help     | Display usage information       |
| -v, --version  | Display version information     |

# Contributing

**Requirements**

- Python 3.7+
- Virtualenv

Setup the development environment with

```shell
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Build and install the package with

```
python3 -m build
pip install dist/<package_name>.whl
```
