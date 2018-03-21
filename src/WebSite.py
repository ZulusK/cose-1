import requests
from .Good import Good
defaultHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}


class WebSite:
    """Defines website, that describe real website"""

    def __init__(self, xml):
        self.name = xml.find("name").text
        self.url = xml.url.text
        self.goodName = xml.goodName.text
        self.goodPrice = xml.goodPrice.text
        self.goods = []

    def __str__(self):
        return "Web-site '%s', base url '%s" % (self.name, self.url)

    def loadPages(self, pageLimit, headers):
        pages = []
        for i in range(1, pageLimit + 1):
            pages.append(requests.get(self.url % i, headers=headers))
            print("%s load page %d" % (self.name, i))
        return pages

    def loadGoods(self, *, pageLimit=10, headers=defaultHeaders):
        pages = self.__loadPages(pageLimit=pageLimit, headers=headers)
        self.goods=[Good]
