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
    :return: (list of parsed sites,page_limit,levenstein_accuracy)
    """
    sites = None
    xml = None
    page_limit = None
    lev_acc = None
    try:
        xml = readXMLFile(filename)
        page_limit = int(xml.find("page-limit").text)
        lev_acc = int(xml.find("levenstein-accuracy").text)
        sites = xml.find_all("site")
    except IOError:
        pass
    finally:
        if not sites:
            sites = []
    return ([WebSite(site) for site in sites], page_limit, lev_acc)
