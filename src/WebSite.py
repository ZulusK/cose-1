import threading
from queue import Queue

from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from sty import fg, bg

options = Options()
options.add_argument("--headless")
HEADERS = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"

from .Good import Good


class WebSite:
    """Defines website, that describe real website"""

    def __init__(self, xml):
        self.rootURL = xml.rootURL.text
        self.name = xml.find("name").text
        self.goodURL = xml.catalogURL.text
        self.goodNamePath = xml.goodName.text
        self.goodPricePath = xml.goodPrice.text
        self.goodURLPath = xml.goodURL.text
        if xml.find('trash'):
            self.trash = [item.text for item in xml.trash.find_all('item')]
        else:
            self.trash = []
        self.goods = []

    def __str__(self):
        return "Web-site '{2}{0!s}{4}', url: '{3}{1!s}{4}'".format(self.name, self.rootURL, fg.blue, fg.green, fg.rs)

    __repr__ = __str__

    def __loadPage(self, url):
        browser = webdriver.Firefox(firefox_options=options)
        print("{4}start{5} render '{2}{0!s}{3}' page: {1!s}".format(self.name, url, fg.blue, fg.rs, bg.yellow, bg.rs))
        browser.get(url)
        page = browser.execute_script("return document.body.innerHTML")
        print("{4}end{5} render '{2}{0!s}{3}' page: {1!s}".format(self.name, url, fg.blue, fg.rs, bg.green, bg.rs))
        browser.quit()
        return page

    def __getGoodAttrsFromPage(self, page):
        tree = html.fromstring(page)
        names = tree.xpath(self.goodNamePath)
        prices = tree.xpath(self.goodPricePath)
        urls = tree.xpath(self.goodURLPath)
        return (names, prices, urls)

    def __loadGoodsFromPage(self, url,queue):
        page = self.__loadPage(url)
        good_names, good_prices, good_urls = self.__getGoodAttrsFromPage(page)
        for i in range(len(good_names)):
            queue.put(Good(self, good_names[i], good_prices[i], good_urls[i]))

    def loadGoods(self, *, pageLimit=5):
        queue = Queue();
        threads = []
        for i in range(1, pageLimit+1):
            threads.append(threading.Thread(target=self.__loadGoodsFromPage, args=(self.goodURL % i, queue)))
            threads[-1].start()
        for thread in threads:
            thread.join()
        while not queue.empty():
            self.goods.append(queue.get())
            print(self.goods[-1])
