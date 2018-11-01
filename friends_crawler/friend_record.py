from urllib.parse import urlparse
from .person import Person

class FriendRecord:
    def __init__(self, html):
        self.html = html

    def parse(self):
        link_tag = self.html.find('a')

        if link_tag and link_tag['href'] and len(link_tag['href']) > 1:
            url = urlparse(link_tag['href'])

            return Person(
                link="{}{}".format(url.netloc, url.path),
                id=self.parse_id_from_link(url.path),
                picture=self.parse_profile_picture_path(link_tag)
            )
        else:
            return None

    def parse_id_from_link(self, path):
        return path[1:]

    def parse_profile_picture_path(self, html):
        return html.find('img')['src']
