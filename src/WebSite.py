import re

from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
HEADERS = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"

from .Good import Good


class WebSite:
    """Defines website, that describe real website"""

    def __init__(self, xml):
        self.rootURL=xml.rootURL.text
        self.name = xml.find("name").text
        self.goodURL = xml.catalogURL.text
        self.goodNamePath = xml.goodName.text
        self.goodPricePath = xml.goodPrice.text
        self.goodURLPath = xml.goodURL.text
        if xml.find('trash'):
            self.trash = [item.text for item in xml.trash.find_all('item')]
        else:
            self.trash=[]
        self.goods = []

    def __str__(self):
        return "Web-site '%s', base url '%s" % (self.name, self.rootURL)

    __repr__ = __str__

    def __loadAndRenderPages(self, pageLimit):
        browser = webdriver.Firefox(firefox_options=options)
        pages = []
        for i in range(1, pageLimit + 1):
            print("start render %s page %d" % (self.name, i))
            browser.get(self.goodURL % i)
            pages.append(browser.execute_script("return document.body.innerHTML"))
            print("end render %s page %d" % (self.name, i))
        browser.quit()
        return pages

    def __normalizeNames(self, names):
        normalized = []
        if (self.trash):
            for name in names:
                for regex in self.trash:
                    name = re.sub(regex, '', name)
                normalized.append(name.strip())
        else:
            normalized = [s.strip() for s in names]
        print(len(normalized))
        return normalized

    def __getGoodsUsingXpath(self, pages):
        good_names = []
        good_prices = []
        good_urls = []
        for page in pages:
            tree = html.fromstring(page)
            good_names.extend(tree.xpath(self.goodNamePath))
            good_prices.extend(tree.xpath(self.goodPricePath))
            good_urls.extend(tree.xpath(self.goodURLPath))
        good_names = self.__normalizeNames(good_names)
        for i in range(len(good_names)):
            self.goods.append(Good(good_names[i], self, good_prices[i], good_urls[i]))

    def loadGoods(self, *, pageLimit=5):
        pages = self.__loadAndRenderPages(1)
        self.__getGoodsUsingXpath(pages)
        for good in self.goods:
            print(good)
