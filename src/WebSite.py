import requests

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

    def __repr___(self):
        return "Web-site '%(name)', base url '%{url}" % self

    def loadGoods(self, *, pageLimit=10, headers=defaultHeaders):
        for i in range(1, pageLimit + 1):
            page = requests.get(self.url % i, headers=headers)
            print("%s load page %d", self, i)
            with open('output/test-%s-%d.html' % (self.name, i), 'w') as output_file:
                output_file.write(page.text)
