import pytest

import src

data = src.read_XML_file("input.xml").find_all("site")[0]

#
# def test_WebSite_init_validAgrs():
#     site = src.WebSite(xml=data)
#     assert site.name == data.find("name").text
#     assert site.url == data.url.text
#
#
# def test_WebSite_init_invalidArgs():
#     with pytest.raises(Exception):
#         src.WebSite()
#
#
# def test_WebSite_repr():
#     site = src.WebSite(xml=data)
#     repr = str(site)
#     assert site.name in repr
#     assert site.url in repr
#
#
# def test_loadPages():
#     site = src.WebSite(xml=data)
#     pageLimit = 1
#     pages = site.load_goods(pageLimit=pageLimit)
#     assert len(pages) == pageLimit
