import sys
import threading

from sty import bg

import src


def parseXML():
    """Returns list with parsed sites from command-line argument
    :return: (list of parsed web-sites from file, page limit)
    """
    if len(sys.argv) < 2:
        raise Exception(bg.red + "No filename specified, please add command-line args" + bg.rs)
    else:
        print(bg.yellow + "Try to read file %s" % sys.argv[1] + bg.rs)
        sites, page_limit, lev_acc = src.readSitesFromFile(sys.argv[1])
        if not sites:
            raise Exception(bg.red + "No such file %s, try again" % sys.argv[1] + bg.rs)
        else:
            print(bg.da_green + "Success, read %d sites" % len(sites) + bg.rs)
        if not page_limit:
            page_limit = 5
        return (sites, page_limit)


def asyncLoadGoods(sites, pageLimit):
    threads = [threading.Thread(target=site.loadGoods, kwargs={'pageLimit': pageLimit}) for site in sites]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def collectGoods(websites):
    all_goods = []
    for site in websites:
        all_goods.extend(site.goods)
    products = []
    while len(all_goods):
        p = src.Product()
        all_goods = p.collectFromList(all_goods[0], all_goods)
        products.append(p)
    for p in products:
        print(p)

def main():
    sites, pageLimit = parseXML()
    for site in sites:
        print(site)
    asyncLoadGoods(sites, pageLimit)
    collectGoods(sites)


main()
