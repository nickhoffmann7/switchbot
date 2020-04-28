import requests
from bs4 import BeautifulSoup

import utils


def check_availability(url):
    print("checking " + url)

    website = requests.get(url)
    soup = BeautifulSoup(website.content, "html.parser")
    element = soup.select_one('div[class*="availability" i]')

    if not element:
        print("availability not found")
        return

    text = utils.strip_non_alphanumeric_chars(element.text)

    if text.startswith("aufLager") or text.startswith("Lieferung"):
        print("AUF LAGER")
        return text + "\n\n" + url

    print("nicht auf lager")
