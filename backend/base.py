import requests

from bs4 import BeautifulSoup

from constants import HEADERS


class KeywordBase(object):

    @staticmethod
    def get_headers():
        return HEADERS

    def get_soup(self, link):
        """
        Get soup for youtube watch link
        :param link: https://www.youtube.com/watch?v=m49lM921
        :return: soup object
        """
        source = requests.get(link, headers=self.get_headers()).text
        soup = BeautifulSoup(source, "html.parser")
        return soup
