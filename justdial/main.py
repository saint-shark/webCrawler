
import requests
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
})
# print (headers)
url = input("input url")
# print (url)
for pageNum in range(1,25):

        comp_url = url + "/page-" + str(pageNum)
        # print (comp_url)
        r = requests.get(comp_url ,headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        searchResult = []
        article_desc = {}
        for i in range (0,50):
            try:
                article_desc['Name'] = soup.select('.jcn')[i].get_text()
                article_desc['telephone'] = soup.select('.contact-info span a')[i].get_text()
                article_desc['address'] = soup.select('.mrehover')[i].get_text()
                article_desc = {}
                searchResult.append(article_desc)

            except:
                pass
        if (len(searchResult) == 0):
            break
        print (searchResult)
