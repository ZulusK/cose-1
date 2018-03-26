import re
import xml.etree.ElementTree as ET
from . import WebSite
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
        if not name:
            raise ValueError("Param 'name' is None")
        if hasattr(self.website, "trash"):
            for regex in self.website.trash:
                name = re.sub(regex, '', name)
        return name.strip()

    def __normalize_URL(self, url):
        if not url:
            raise ValueError("Param 'url' is None")
        if url.startswith("/"):
            return self.website.root_url + url
        else:
            return url

    def __normalize_price(self, price):
        if not price:
            raise ValueError("Param 'price' is None")
        elif isinstance(price, str):
            return int("".join(price.split()))
        elif isinstance(price, int):
            return price
        else:
            raise ValueError("Param 'price' in unsupported form. Only string and int are allowed")

    def __init__(self, website, name, price, url):
        if not website:
            raise Exception("Param 'website' is None")
        self.website = website
        self.name = self.__normalize_name(name)
        self.price = self.__normalize_price(price)
        self.url = self.__normalize_URL(url)

    def __str__(self):
        return "Good '{2}{0!s}{4}', price: {3}${1!s}{4}" \
            .format(self.name, self.price, fg.blue, fg.green, fg.rs)

    __repr__ = __str__
