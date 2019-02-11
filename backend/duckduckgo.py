import urllib
import requests

from bs4 import BeautifulSoup

from constants import YOUTUBE_WATCH_LINK
from base import KeywordBase


class DuckDuckGoScrap(KeywordBase):
    BING_LINK = "https://duckduckgo.com/html/"
    EXTRACTED_LINKS = set()

    def get_soup_with_title(self, title):
        link = "{}?{}".format(self.BING_LINK, urllib.parse.urlencode(
            {"q": "{} {}".format(title, "youtube")}
        ))
        return self.get_soup(link)

    def get_youtube_links(self, title):
        soup = self.get_soup_with_title(title)
        results = soup.find("div", {"id": "links"})
        links = results.findAll("div", {"class": "results_links"})
        for link in links:
            current_link = link.find("a").attrs["href"]
            if current_link.startswith(YOUTUBE_WATCH_LINK):
                yield current_link