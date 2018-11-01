from chromote import Chromote
from time import sleep
from .profiles_db import ProfilesDb
from .page import Page

class FriendsCrawler:
    def __init__(self):
        self.chrome = Chromote()
        self.tab = self.chrome.add_tab()
        self.profiles = {}
        self.db = ProfilesDb()

    def crawl(self, url):
        self.goto_url(url)
        sleep(3)
        page = Page(self.tab.html)
        count = page.friends_count

        while True:
            print(count)
            self.scroll()
            sleep(1)
            page = Page(self.tab.html)
            new_count = page.friends_count

            if (new_count == count):
                break
            else:
                count = new_count

        friends = page.parse_friends_html()

        for friend in friends:
            print(friend)

    def scroll(self):
        self.tab.synthesize_scroll_gesture(x=0, y=0, x_distance=0, y_distance=-1500, speed=12000)

    def goto_url(self, url):
        self.tab.set_url(url)
