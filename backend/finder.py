import sys

from google import GoogleScrap
from youtube import YoutubeTags


class KeywordFinder(object):
    EXTRACTED_LINKS = set()
    TAG_LIST = set()

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

    def find_links(self, title):
        for link in GoogleScrap().get_youtube_links(title):
            if link not in self.EXTRACTED_LINKS:
                self.EXTRACTED_LINKS.add(link)
                self.get_tags(link)



# if __name__ == '__main__':
#     keyword_object = KeywordFinder()
#     keyword_object.find_links(sys.argv[1])
#     keyword_object.get_html()
#     sys.stdout.flush()