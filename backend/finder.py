from google import GoogleScrap
from bing import BingScrap
from duckduckgo import DuckDuckGoScrap
from youtube import YoutubeTags


class KeywordFinder(object):

    def __init__(self):
        self.EXTRACTED_LINKS = set()
        self.TAG_LIST = set()
        self.TAG_DICT = dict()
        self.CURRENT_TRENDING = ""
        self.CURRENT_TRENDING_COUNT = 0

    def get_tags(self, link):
        """
        Get tags for youtube watch link
        :param link: https://www.youtube.com/watch?v=m49lM921
        :return:
        """
        for tag in YoutubeTags().get_tags(link):
            self.TAG_LIST.add(tag)
            if self.TAG_DICT.get(tag):
                self.TAG_DICT[tag] += 1
            else:
                self.TAG_DICT[tag] = 1
            if not self.CURRENT_TRENDING or self.CURRENT_TRENDING != tag:
                if self.TAG_DICT[tag] > self.CURRENT_TRENDING_COUNT:
                    self.CURRENT_TRENDING = tag
                    self.CURRENT_TRENDING_COUNT = self.TAG_DICT[tag]
            else:
                self.CURRENT_TRENDING = tag
                self.CURRENT_TRENDING_COUNT = self.TAG_DICT[tag]

    def get_google_links(self, title):
        """
        Updates keywords from google
        """
        for link in GoogleScrap().get_youtube_links(title):
            if link not in self.EXTRACTED_LINKS:
                self.EXTRACTED_LINKS.add(link)
                self.get_tags(link)

    def get_bing_links(self, title):
        """
        Updates keywords from Bing
        """
        for link in BingScrap().get_youtube_links(title):
            if link not in self.EXTRACTED_LINKS:
                self.EXTRACTED_LINKS.add(link)
                self.get_tags(link)

    def get_duckduckgo_links(self, title):
        """
        Updates keywords from duckduckgo
        """
        for link in DuckDuckGoScrap().get_youtube_links(title):
            if link not in self.EXTRACTED_LINKS:
                self.EXTRACTED_LINKS.add(link)
                self.get_tags(link)

    def find_links(self, title):
        """
        Get youtube links and the keywords used for given title
         by searching on different search engines
        :param title: Sample title
        :return:
        """
        self.get_google_links(title)
        self.get_bing_links(title)
        self.get_duckduckgo_links(title)
