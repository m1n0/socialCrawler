from bs4 import BeautifulSoup
from .friend_record import FriendRecord

class Page:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.friends_html = self.get_friends_html()
        self.friends_count = len(self.friends_html)

    def parse(self):
        return self.parse_friends_html(self.friends_html)

    def get_friends_html(self):
        friends_wrapper = self.soup.find('div', attrs={'id': 'pagelet_timeline_medley_friends'})
        friend_lists = friends_wrapper.find_all('ul', attrs={'class': 'uiList'})

        friend_lis = []
        for list in friend_lists:
            friend_lis.extend(list.find_all('div', attrs={'data-testid': 'friend_list_item'}))

        return friend_lis

    def parse_friends_html(self):
        list = []
        for friend_li in self.friends_html:
            person = FriendRecord(friend_li).parse()
            list.append(person) if person is not None else None

        return list
