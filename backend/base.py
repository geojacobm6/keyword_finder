import requests

from bs4 import BeautifulSoup

from constants import YOUTUBE_WATCH_LINK, HEADERS


class KeywordBase(object):

    @staticmethod
    def get_headers():
        return HEADERS

    def get_soup(self, link):
        source = requests.get(link, headers=self.get_headers()).text
        soup = BeautifulSoup(source, "html.parser")
        return soup