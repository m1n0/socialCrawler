import sys
from friends_crawler.crawler import FriendsCrawler

if __name__ == '__main__':
    starting_id = sys.argv[1]
    crawler = FriendsCrawler().crawl(f'https://www.facebook.com/{starting_id}/friends')
