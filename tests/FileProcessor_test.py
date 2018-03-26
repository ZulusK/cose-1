import pytest

import src


def test_readXMLFile_fileExist():
    assert src.read_XML_file("input.xml")


@pytest.mark.parametrize("filename", ["", "someotherfile.xml"])
def test_readXMLFile_invalidFile(filename):
    with pytest.raises(Exception):
        src.read_XML_file(filename)


@pytest.mark.parametrize("filename", ["", "someotherfile.xml", "src/Good.py"])
def test_readSitesFromFile_invalidFile(filename):
    assert len(src.read_sites_from_file(filename)[0]) == 0


def test_readSitesFromFile_fileExist():
    sites, page_limit, lev_acc = src.read_sites_from_file("input.xml")
    assert len(sites) > 0
    assert page_limit > 0
    assert lev_acc > 0
