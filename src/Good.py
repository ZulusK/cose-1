import re

from sty import fg




class Good:

    def __normalizeName(self, name):
        if (self.website.trash):
            for regex in self.website.trash:
                name = re.sub(regex, '', name)
        return name.strip()

    def __normalizeURL(self, url):
        if url.startswith("/"):
            return self.website.rootURL + url
        else:
            return url

    def __normalizePrice(self, price):
        return int("".join(price.split()))

    def __init__(self, website, name, price, url):
        self.website = website
        self.name = self.__normalizeName(name)
        self.price = self.__normalizePrice(price)
        self.url = self.__normalizeURL(url)

    def __str__(self):
        return "Good '{2}{0!s}{4}', price: {3}${1!s}{4}".format(self.name, self.price, fg.blue, fg.green, fg.rs)

    __repr__ = __str__
