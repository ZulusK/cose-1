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
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


class Product:
    def collectFromList(self, original, list_of_goods, *, accuracy=10):
        self.goods, list_of_goods = partition(lambda x: levenshteinDistance(x.name, original.name) < 10, list_of_goods)
        self.goods=list(self.goods)
        return list(list_of_goods)

    def maxPrice(self):
        return max(self.goods, key=lambda x: x.price).price

    def minPrice(self):
        return min(self.goods, key=lambda x: x.price).price
    def __str__(self):
        return "Product '{cName}{name}{cRS}', price: {cMinPrice}${min}{cRS}-{cMaxPrice}${max}{cRS}".format(
            name=self.goods[0].name, min=self.minPrice(), max=self.maxPrice(), cName=fg.li_yellow,
            cMinPrice=fg.li_green, cMaxPrice=fg.li_red, cRS=fg.rs)

    __repr__=__str__

    def __init__(self):
        self.goods = []
