import urllib

from constants import YOUTUBE_WATCH_LINK
from base import KeywordBase


class BingScrap(KeywordBase):
    WEB_LINK = "https://www.bing.com/search"
    EXTRACTED_LINKS = set()

    def get_soup_with_title(self, title):
        """
        :param title: Sample title
        :return: soup object for search result page
        """
        link = "{}?{}".format(self.WEB_LINK, urllib.parse.urlencode(
            {"q": "{} {}".format(title, "youtube")}
        ))
        return self.get_soup(link)

    def get_youtube_links(self, title):
        """
        :param title: Sample title
        :return: scrap Youtube link from search result page
        """
        soup = self.get_soup_with_title(title)
        results = soup.find("ol", {"id": "b_results"})
        links = results.findAll("li", {"class": "b_algo"})
        for link in links:
            current_link = link.find("a").attrs["href"]
            if current_link.startswith(YOUTUBE_WATCH_LINK):
                yield current_link
