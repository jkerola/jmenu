# jmenu

## About

Python app to display University of Oulu restaurant menus from Jamix API.

Versions below 1.3 work by rendering the pages with selenium, then scraping the HTML with BeautifulSoup4.

Versions 1.3 and above use the API at [https://fi.jamix.cloud/apps/menuservice/rest](https://fi.jamix.cloud/apps/menuservice/rest)

# Usage

Simply run the binary

```shell
chmod +x jmenu
./jmenu
```

to print restaurant menus in the terminal.

| Argument              | Example | Description                           |
| :-------------------- | :------ | :------------------------------------ |
| --allergens, <br/> -a | G VEG   | Highlights results with the allergen. |

| Flag      | Description                                        |
| :-------- | :------------------------------------------------- |
| --hide    | Hide bad results instead of highlighting good ones |
| --help    | Display usage information                          |
| --version | Display version information                        |

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
