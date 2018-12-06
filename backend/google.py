import urllib
import requests

from bs4 import BeautifulSoup

from constants import YOUTUBE_WATCH_LINK
from base import KeywordBase


class GoogleScrap(KeywordBase):
    GOOGLE_LINK = "https://www.google.com/search"
    EXTRACTED_LINKS = set()

    def get_soup_with_title(self, title):
        link = "{}?{}".format(self.GOOGLE_LINK, urllib.parse.urlencode(
            {"q": "{}+youtube".format(title)}
        ))
        return self.get_soup(link)

    def get_youtube_links(self, title):
        soup = self.get_soup_with_title(title)
        links = soup.find_all('div', class_='r')
        for link in links:
            current_link = link.a.get("href")
            if current_link.startswith(YOUTUBE_WATCH_LINK):
                yield current_link