import xml.etree.ElementTree as ET

from split import partition
from sty import fg


def levenshteinDistance(s1, s2):
    if len(s1) < len(s2):
        return levenshteinDistance(s2, s1)
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


class Product:
    def to_XML(self):
        root = ET.Element('product')
        ET.SubElement(root, 'name').text = self.goods[0].name
        ET.SubElement(root, 'min-price').text = str(self.min_price())
        ET.SubElement(root, 'max-price').text = str(self.max_price())
        ET.SubElement(root, 'average-price').text = str(self.average_price())
        goods = ET.SubElement(root, 'goods')
        for good in self.goods:
            goods.append(good.to_XML())
        return root

    def collect_from_list(self, original, list_of_goods, *, accuracy=10):
        self.goods, list_of_goods = partition(
            lambda x: levenshteinDistance(x.name, original.name) < accuracy,
            list_of_goods)
        self.goods = list(self.goods)
        return list(list_of_goods)

    def average_price(self):
        if not self.__averagePriceValue:
            self.__averagePriceValue = \
                sum([g.price for g in self.goods]) / len(self.goods)
        return self.__averagePriceValue

    def max_price(self):
        if not self.__maxPriceValue:
            self.__maxPriceValue = max(self.goods, key=lambda x: x.price).price
        return self.__maxPriceValue

    def min_price(self):
        if not self.__minPriceValue:
            self.__minPriceValue = min(self.goods, key=lambda x: x.price).price
        return self.__minPriceValue

    def __str__(self):
        return "Product '{cName}{name}{cRS}', "
        "price: {cMinPrice}${min}{cRS}-{cMaxPrice}${max}{cRS}".format(
            name=self.goods[0].name,
            min=self.min_price(),
            max=self.max_price(),
            cName=fg.li_yellow,
            cMinPrice=fg.li_green,
            cMaxPrice=fg.li_red,
            cRS=fg.rs)

    __repr__ = __str__

    def __init__(self):
        self.goods = []
        self.__averagePriceValue = None
        self.__maxPriceValue = None
        self.__minPriceValue = None
