import pytest

import src


def test_readXMLFile_fileExist():
    assert src.read_XML_file("input.xml")


@pytest.mark.parametrize("filename", ["", "someotherfile.xml"])
def test_readXMLFile_fileNotExist(filename):
    with pytest.raises(IOError):
        src.read_XML_file(filename)


@pytest.mark.parametrize("filename", ["", "someotherfile.xml"])
def test_readSitesFromFile_fileNotExist(filename):
    assert len(src.read_sites_from_file(filename)) == 0


def test_readSitesFromFile_fileExist():
    sites = src.read_sites_from_file("input.xml")
    assert len(sites) > 0
