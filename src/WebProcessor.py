import requests


def loadSites(site, *,pageLimit=10):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    # products=[]
    print("Load site '%s'" % site.find('name').text)
    for i in range(1, pageLimit + 1):
        page = requests.get(site.url.text.replace("$    {page}", str(i)),headers=headers)
        print('.' * 3 + "Loaded #%d page" % i)
        with open('test%d.html' % i, 'w') as output_file:
            output_file.write(page.text)
