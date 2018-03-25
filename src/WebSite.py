from lxml import html
from selenium import webdriver

from .Good import Good

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
}


class WebSite:
    """Defines website, that describe real website"""

    def __init__(self, xml):
        if (xml):
            self.name = xml.find("name").text
            self.url = xml.url.text
            self.goodName = xml.goodName.text
            self.goodPrice = xml.goodPrice.text
        else:
            self.name = "No name"
            self.url = "???"
            self.goodName = "good"
            self.goodPrice = "price"
        self.goods = []

    def __str__(self):
        return "Web-site '%s', base url '%s" % (self.name, self.url)

    __repr__ = __str__

    def __loadPages(self, pageLimit, headers):
        browser = webdriver.PhantomJS()
        pages = []
        for i in range(1, pageLimit + 1):
            print("%s start loading page %d" % (self.name, i))
            browser.get(self.url % i)
            pages.append(browser.execute_script("return document.body.innerHTML"))
            # pages.append(requests.get(self.url % i, headers=headers).text)
            print("%s end loading page %d" % (self.name, i))
        browser.quit()
        return pages

    def loadGoods(self, *, pageLimit=5, headers=HEADERS):
        pages = self.__loadPages(1, headers)
        # file = open("testfile.html", "w")
        # file.write(pages[0])
        # file.close()
        for page in pages:
            tree = html.fromstring(page)
            goodNames = tree.xpath(self.goodName)
            goodPrices = tree.xpath(self.goodPrice)
            print(goodNames)
            print(goodPrices)
            print(len(goodNames))
            print(len(goodPrices))
            for i in range(len(goodNames)):
                self.goods.append(Good(goodNames[i], self, goodPrices[i], "url"))
                print(self.goods[i])
            # for good in self.goods:
