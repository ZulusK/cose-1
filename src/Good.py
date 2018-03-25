import re
import xml.etree.ElementTree as ET

from sty import fg


class Good:
    def to_XML(self):
        root = ET.Element('good')
        ET.SubElement(root, 'name').text = self.name
        ET.SubElement(root, 'price').text = str(self.price)
        ET.SubElement(root, 'url').text = self.url
        ET.SubElement(root, 'store').text = self.website.name
        return root

    def __normalize_name(self, name):
        if (self.website.trash):
            for regex in self.website.trash:
                name = re.sub(regex, '', name)
        return name.strip()

    def __normalize_URL(self, url):
        if url.startswith("/"):
            return self.website.rootURL + url
        else:
            return url

    def __normalize_price(self, price):
        return int("".join(price.split()))

    def __init__(self, website, name, price, url):
        self.website = website
        self.name = self.__normalize_name(name)
        self.price = self.__normalize_price(price)
        self.url = self.__normalize_URL(url)

    def __str__(self):
        return "Good '{2}{0!s}{4}', price: {3}${1!s}{4}"\
            .format(self.name, self.price, fg.blue, fg.green, fg.rs)

    __repr__ = __str__
