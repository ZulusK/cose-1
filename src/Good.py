class Good:
    def __init__(self, name, website, price, url):
        self.name = "".join(name.split('\n'))
        self.website = website
        self.url = url
        self.price = int("".join(price.split()))

    def __str__(self):
        return "good '%s' from '%s' price ₴%d" % (self.name, self.website.name, self.price)

    __repr__ = __str__
