import sys
import threading

import src


def parseXML():
    """Returns list with parsed sites from command-line argument
    :return: (list of parsed web-sites from file, page limit)
    """
    if len(sys.argv) < 2:
        raise Exception("No filename specified, please add command-line args")
    else:
        print("Try to read file %s" % sys.argv[1])
        sites, pageLimit = src.readSitesFromFile(sys.argv[1])
        if not sites:
            raise Exception("No such file %s, try again" % sys.argv[1])
        else:
            print("...Success")
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
