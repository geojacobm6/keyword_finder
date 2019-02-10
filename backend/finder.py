import sys

from google import GoogleScrap
from bing import BingScrap
from youtube import YoutubeTags


class KeywordFinder(object):
    EXTRACTED_LINKS = set()
    TAG_LIST = set()
    TAG_DICT = dict()
    CURRENT_TRENDING = ""
    CURRENT_TRENDING_COUNT = 0

    def get_html(self):
        html = """
                <!DOCTYPE html>
                  <html>
                    <head>
                      <meta charset="UTF-8">
                      <title>Keyword Finder</title>
                    </head>
                    <body>
                      <h1>Results</h1>
                        {}
                    </body>
                  </html>
                """
        html_span = ''
        for tag in self.TAG_LIST:
            html_span += "<strong>{}</strong>, ".format(tag)
        print(html.format(html_span))

    def get_tags(self, link):
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

    def find_links(self, title):
        self.EXTRACTED_LINKS = set()
        self.TAG_LIST = set()
        self.TAG_DICT = dict()
        self.CURRENT_TRENDING = ""
        self.CURRENT_TRENDING_COUNT = 0
        for link in GoogleScrap().get_youtube_links(title):
            if link not in self.EXTRACTED_LINKS:
                self.EXTRACTED_LINKS.add(link)
                self.get_tags(link)

        for link in BingScrap().get_youtube_links(title):
            if link not in self.EXTRACTED_LINKS:
                self.EXTRACTED_LINKS.add(link)
                self.get_tags(link)
