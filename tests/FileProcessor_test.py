import pytest

import src


def test_readXMLFile_fileExist():
    assert src.readXMLFile("input.xml")


@pytest.mark.parametrize("filename", ["", "someotherfile.xml"])
def test_readXMLFile_fileNotExist(filename):
    with pytest.raises(IOError):
        src.readXMLFile(filename)


@pytest.mark.parametrize("filename", ["", "someotherfile.xml"])
def test_readSitesFromFile_fileNotExist(filename):
    assert len(src.readSitesFromFile(filename)) == 0


def test_readSitesFromFile_fileExist():
    sites = src.readSitesFromFile("input.xml")
    assert len(sites) > 0
