import sys
import threading
import xml.etree.ElementTree as ET

from sty import fg

import src

INPUT_FILENAME = ""
OUTPUT_FILENAME = ""


def check_commandline_args():
    global INPUT_FILENAME, OUTPUT_FILENAME
    if len(sys.argv) < 2:
        raise Exception(fg.red + "No filename specified, please add command-line args" + fg.rs)
    INPUT_FILENAME = sys.argv[1]
    OUTPUT_FILENAME = "output.xml" if len(sys.argv) < 3 else sys.argv[2]


def parse_XML():
    global INPUT_FILENAME, OUTPUT_FILENAME
    print("{c1}Try{rs} to read file {c2}{filename}{rs}"
          .format(filename=INPUT_FILENAME, rs=fg.rs, c1=fg.yellow, c2=fg.blue))
    sites, page_limit, lev_acc = src.read_sites_from_file(INPUT_FILENAME)
    if not sites:
        raise Exception(fg.red + "No such file %s, try again" % INPUT_FILENAME + fg.rs)
    if not page_limit:
        page_limit = 5
    if not lev_acc:
        lev_acc = 5
    print("{c1}Success{rs}, read {c2}{count}{rs} sites"
          .format(count=len(sites), rs=fg.rs, c1=fg.green, c2=fg.blue))
    print("{c1}Success{rs}, read {c2}{count}{rs} page-limit"
          .format(count=page_limit, rs=fg.rs, c1=fg.green, c2=fg.blue))
    print("{c1}Success{rs}, read {c2}{acc}{rs} levenstein's distance"
          .format(acc=lev_acc, rs=fg.rs, c1=fg.green, c2=fg.blue))
    return (sites, page_limit, lev_acc)


def async_load_goods(sites, pageLimit):
    threads = [threading.Thread(target=site.load_goods, kwargs={'pageLimit': pageLimit}) for site in sites]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def collect_product(websites, lev_acc):
    all_goods = []
    accuracy = lev_acc if lev_acc else 5
    for site in websites:
        all_goods.extend(site.goods)
    print("{c1}Start{rs} merging goods({c2}{count}"
          " in total{rs}) with Levenstein's algorithm's {c2}accuracy {acc}{rs} "
          .format(c1=fg.yellow, c2=fg.blue, rs=fg.rs, acc=accuracy, count=len(all_goods)))
    products = []
    while all_goods:
        p = src.Product()
        all_goods = p.collect_from_list(all_goods[0], all_goods, accuracy=accuracy)
        products.append(p)
    print("{c1}End{rs} merging goods, {c2}{count} products{rs} in total"
          .format(c1=fg.green, c2=fg.blue, rs=fg.rs, count=len(products)))
    return products


def build_XML_tree(products):
    root = ET.Element('products')
    for p in products:
        root.append(p.to_XML())
    return ET.ElementTree(root)


def main():
    global INPUT_FILENAME, OUTPUT_FILENAME
    try:
        check_commandline_args()
        sites, page_limit, lev_acc = parse_XML()
        for site in sites:
            print(site)
        async_load_goods(sites, page_limit)
        tree = build_XML_tree(collect_product(sites, lev_acc))
        tree.write(OUTPUT_FILENAME)
    except Exception as err:
        print(err.args[0])


main()
