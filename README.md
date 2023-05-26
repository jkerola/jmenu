# jmenu

## About

Python app to scrape University of Oulu restaurant menus from Jamix.

Works by rendering the pages with selenium, then scraping the HTML with BeautifulSoup4

# Usage

Simply run the binary

```shell
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
