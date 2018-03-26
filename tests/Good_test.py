from types import SimpleNamespace

import pytest

import src


@pytest.mark.parametrize("testCase", [
    {"website": {"name": "site", "root_url": "https://someURL"},
     "name": "GoodA",
     "expectedName": "GoodA",
     "price": "404",
     "original_price": 404,
     "url": "https://someURL/pruduct"},
    {"website": {"name": "site", "root_url": "https://someURL", "trash": ["мусор", "o*"]},
     "name": "GoodA мусор   мусор",
     "expectedName": "GdA",
     "price": "4 0\n4",
     "original_price": 404,
     "url": "/product"},
])
def test_Good_normalConstructor(testCase):
    website = SimpleNamespace(**testCase["website"])
    g = src.Good(website, testCase["name"], testCase["price"], testCase["url"])
    assert g.name == testCase["expectedName"].strip()
    assert g.price == testCase["original_price"]
    assert g.url.startswith(website.root_url)
    assert g.website.name == website.name


@pytest.mark.parametrize("testCase", [
    {"name": "GoodA",
     "price": "404",
     "url": "https://someURL/pruduct"},
    {"website": {"name": "site", "root_url": "https://someURL", "trash": ["мусор", "o*"]},
     "expectedName": "GdA",
     "price": "4 0\n4",
     "url": "/product"},
    {"website": {"name": "site", "root_url": "https://someURL", "trash": ["мусор", "o*"]},
     "original_price": 404,
     "url": "/product"},
    {"website": {"name": "site", "root_url": "https://someURL", "trash": ["мусор", "o*"]},
     "name":"abs",
     "price": "404"},
])
def test_Good_invalidConstructor(testCase):
    website = None
    if ("website" in testCase):
        website = SimpleNamespace(**testCase["website"])
    with pytest.raises(Exception):
        src.Good(website, testCase["name"], testCase["price"], testCase["url"])
