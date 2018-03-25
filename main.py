import sys
import threading
from sty import fg,bg
import src


def parseXML():
    """Returns list with parsed sites from command-line argument
    :return: (list of parsed web-sites from file, page limit)
    """
    if len(sys.argv) < 2:
        raise Exception(bg.red+"No filename specified, please add command-line args"+bg.rs)
    else:
        print(bg.yellow+"Try to read file %s" % sys.argv[1]+bg.rs)
        sites, pageLimit = src.readSitesFromFile(sys.argv[1])
        if not sites:
            raise Exception(bg.red+"No such file %s, try again" % sys.argv[1]+bg.rs)
        else:
            print(bg.da_green+"Success, read %d sites" % len(sites)+bg.rs)
        if not pageLimit:
            pageLimit = 5
        return (sites, pageLimit)


def asyncLoadGoods(sites, pageLimit):
    threads = [threading.Thread(target=site.loadGoods, kwargs={'pageLimit': pageLimit}) for site in sites]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def main():
    sites, pageLimit = parseXML()
    for site in sites:
        print(site)
    asyncLoadGoods(sites, pageLimit)


main()
