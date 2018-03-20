import sys

from src import *


def getSites():
    """Returns list with parsed sites from command-line argument
    :return: list of parsed web-sites from file
    """
    if len(sys.argv[1] ) < 2:
        raise Exception("No filename specified, please add command-line args")
    else:
        print("Try to read file %s" % sys.argv[1])
        sites = readSitesFromDisk(sys.argv[1])
        if not sites:
            raise Exception("No such file %s, try again" % sys.argv[1])
        else:
            print("...Success")
        return sites


def main():
    # try:
    sites = getSites()
    pages = [WR.loadSites(site) for site in sites]
    print(len(pages))


# except Exception as err:
#     print(err.args[0])
#     sys.exit(1)


main()
