from bs4 import BeautifulSoup

from .WebSite import WebSite


def readXMLFile(filename):
    """Reads file, with specific filename and returns parsed XML-tree
    :param filename: path to file with urls
    :return: parsed XML-tree, that contains in specefied file
    """
    with open(filename) as xml:
        soup = BeautifulSoup(xml, "lxml-xml")
    return soup


def readSitesFromFile(filename):
    """Read file, with specific filename and returns inner URLs
    :param filename:name of file with all sites
    :return:list of parsed sites
    """
    xml = None
    try:
        xml = readXMLFile(filename)
    except IOError:
        pass
    finally:
        if (not xml):
            xml = []
        else:
            xml = xml.find_all("site")
        return [WebSite(site) for site in xml]
