from base import KeywordBase


class YoutubeTags(KeywordBase):

    def get_tags(self, link):
        """
        Get tags from youtube links
        :param link: https://www.youtube.com/watch?v=m49lM921
        :return: list of tags
        """
        soup = self.get_soup(link)
        tag_list = []
        try:
            tag_data = soup.get_text().split("keywords")[1].split("]")[0].replace("\\", "")[3:]\
                .replace('"', '')
            tag_list = tag_data.split(",")
        except IndexError:
            pass
        return tag_list
