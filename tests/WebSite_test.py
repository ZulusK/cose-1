import src


def test_WebSite_init_validAgrs():
    xml = src.readXMLFile("input.xml").find_all("site")
    site = src.WebSite(xml[0])
    assert site.name == xml[0].find("name").text
    assert site.url == xml[0].url.text
