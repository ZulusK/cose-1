from queue import Queue

from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from sty import fg

from .Good import Good

options = Options()
options.add_argument("--headless")
HEADERS = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) "
"Gecko/20100101 Firefox/10.0"


class WebSite:
    def __init__(self, xml):
        self.root_url = xml.rootURL.text
        self.name = xml.find("name").text
        self.good_url = xml.catalogURL.text
        xml_item = xml.find("good-item")
        self.item_path = xml_item.path.text
        self.good_name_path = xml_item.title.text
        self.good_price_path = xml_item.price.text
        self.good_url_path = xml_item.url.text
        if xml.find('trash'):
            self.trash = [item.text for item in xml.trash.find_all('item')]
        else:
            self.trash = []
        self.goods = []

    def __str__(self):
        return "Web-site '{2}{0!s}{4}', url: '{3}{1!s}{4}'" \
            .format(self.name, self.root_url, fg.blue, fg.green, fg.rs)

    __repr__ = __str__

    def __load_page(self, browser, url):
        print("{4}start{5} fetching '{2}{0!s}{3}' page: {1!s}"
              .format(self.name, url, fg.blue, fg.rs, fg.yellow, fg.rs))
        browser.get(url)
        page = browser.execute_script("return document.body.innerHTML")
        print("{4}end{5} fetching '{2}{0!s}{3}' page: {1!s}"
              .format(self.name, url, fg.blue, fg.rs, fg.green, fg.rs))
        return page

    def __good_tile_2_good(self, tile):
        name = tile.xpath(self.good_name_path)[0]
        price = tile.xpath(self.good_price_path)[0]
        url = tile.xpath(self.good_url_path)[0]
        return Good(self, name, price, url)

    def __get_goods_tiles(self, page):
        tree = html.fromstring(page)
        tiles = tree.xpath(self.item_path)
        print(len(tiles))
        return tiles

    def __load_goods_from_page(self, browser, url, queue):
        page = self.__load_page(browser, url)
        good_tails = self.__get_goods_tiles(page)
        for tile in good_tails:
            try:
                queue.put(self.__good_tile_2_good(tile))
            except Exception as err:
                # print(err)
                pass

    def load_goods(self, *, pageLimit=5):
        browser = webdriver.Firefox(firefox_options=options)
        queue = Queue()
        for i in range(1, pageLimit + 1):
            self.__load_goods_from_page(browser, self.good_url % i, queue)
        browser.quit()
        while not queue.empty():
            self.goods.append(queue.get())
            print(self.goods[-1])
            # print(self.goods[-1])
