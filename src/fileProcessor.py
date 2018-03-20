from bs4 import BeautifulSoup


def readFile(filename):
    """Reads file, with specific filename and returns parsed XML-tree"""
    with open(filename) as xml:
        soup = BeautifulSoup(xml,"lxml-xml")
    return soup
    # try:
    #     parsed = BeautifulSoup.parse().getroot()
    # except IOError as error:
    #     print("Error at read file ", error)
    # return parsed


def readSitesFromDisk(filename):
    """Read file, with specific filename and returns inner URLs"""
    xml = readFile(filename)
    if (xml):
        return xml.find_all('site')
    else:
        return []
