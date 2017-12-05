# Regular Expressions
import re
# Requests
import requests
# BS4 for scraping
from bs4 import BeautifulSoup
# For pretty printing data
import pprint as pp
import sys
import cymysql

sys.setrecursionlimit(1500)
# Pages
visited_pages = []
visited_articles = []

# Database connection
#conn = cymysql.connect(host='127.0.0.1', user='root', passwd='', db='crawlers', charset='utf8')
#cur = conn.cursor()


def make_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def get_all_articles(url, news_type, offset):
    complete_url = url + "/" + "?" + news_type + "&" "paged=" + str(offset)
    try:
        soup = make_soup(complete_url)
        articles = soup.select('.post-title')
        all_articles = []

        for article in articles:
            all_articles.append(article.select('a')[0].get('href'))

        return all_articles, len(all_articles)
    except:
         print("Error in making soup. Please try again later.")
         return False, False


                # def insert_article_in_database(article):
                #     try:
                #         query = 'INSERT into `aaj_tak` (`id`, `body`, `image_url`, `category`, `title`, `url`, `news_time`) VALUES (NULL, %s, %s, %s, %s, %s, %s)'
                #         cur.execute(query, (
                #         str(article['body']), str(article['image_url']), str(article['category']), str(article['title']), str(article['url']), str(article['news_time'])))
                #         conn.commit()
                #         print("Saved successfully -->" + article['title'])
                #     except cymysql.err.IntegrityError:
                #         print("Already present --> " + article['title'])
                #     except:
                #         print("There was an Error for --> " + article['title'])

def get_article(url):
     article_desc = {}
     soup = make_soup(url)
     article_desc['title'] = soup.select('.post-inner h1')[0].contents[0].contents[0]
     try:
         article_desc['image_url'] = soup.select('.single-post-thumb img')[0].get('src')
     except:
         pass
     article_desc['news_time'] = soup.select('.tie-date')[0].contents[0]
     try:
         article_desc['body'] = soup.select('.entry')[0].get_text()
     except:
         pass
     print (article_desc)
     return article_desc


def main():

     types = ['cat=11', 'cat=2', 'cat=8', 'cat=7', 'cat=39']

     for link_type in types:
            offset = 1

            while offset < 20:


                article_urls, length = get_all_articles("http://gnanews.in", link_type, offset)


                offset = length + offset

                for article_url in article_urls:

                    print (article_url)
                    article_desc = get_article(article_url)
                    #article_desc['category'] = link_type
                    article_desc['url'] = article_url
                                    #                insert_article_in_database(article_desc)

                                    # get_article("http://aajtak.intoday.in/story/evm-hacking-hackathon-election-commission-1-929419.html")


if __name__ == '__main__':
    main()
