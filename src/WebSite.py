from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")

from .Good import Good


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

    def __loadPages(self, pageLimit):
        browser = webdriver.Firefox(firefox_options=options)
        pages = []
        for i in range(1, pageLimit + 1):
            print("%s start loading page %d" % (self.name, i))
            browser.get(self.url % i)
            pages.append(browser.execute_script("return document.body.innerHTML"))
            print("%s end loading page %d" % (self.name, i))
        browser.quit()
        return pages

    def loadGoods(self, *, pageLimit=5):
        pages = self.__loadPages(1)
        for page in pages:
            tree = html.fromstring(page)
            goodNames = tree.xpath(self.goodName)
            goodPrices = tree.xpath(self.goodPrice)
            goodNames = [name[:name.find(' + ')] for name in goodNames]

            for i in range(len(goodNames)):
                self.goods.append(Good(goodNames[i], self, goodPrices[i], "url"))
                print(self.goods[i])
            # for good in self.goods:
