class Good:
    def __init__(self, name, website, price, url):
        self.name = name
        self.website = website
        self.url = url
        self.price = price

    def __str__(self):
        print(self)
        return "good '{name}' from '{website.name}' price ${price}".format(self.__dict__)
