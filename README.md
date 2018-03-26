# cose-1
[![Build Status][travis]](https://travis-ci.org/ZulusK/cose-1)
[![codecov][codecov]](https://codecov.io/gh/ZulusK/cose-1)

Сontains the source code for the first assignment (Components of Software Engineering, 2018, KP-61, FAM, KPI).

These days it's getting crucial for the wayfaring Internet users to orient themselves in the superfluity of dazzling ads,for it is the last resort in disclosing the most expedient price for the desired product. To that end, we proudly present a piece of software that would automatically analyse the market for you, and eventually bestow the user with a recommended venue to carry out the purchase.
### Prerequisites
 You will need python > v3 and installed  Firefox
## Getting Started
Install dependecies
```bash
pip install
```
Install Geckodriver - firefox webdriver (Linux x64)
```bash
sudo chmod + install_geckodriver_ubuntu.sh
sudo ./install_geckodriver_ubuntu.sh
```
Create xml-file with web-sites using template
```xml
<xml>
    <!--number of pages to load-->
    <page-limit>1</page-limit>
    <!--accuracy of comparing good's names-->
    <levenstein-accuracy>3</levenstein-accuracy>
    <sites>
        <site>
            <!--name, that will be displayed for this web-site-->
            <name>Store</name> 
            <!--url of index page-->
            <rootURL>https://store.com</rootURL>
            <!--url for scrapping, use %d to mark pagination destination-->
            <catalogURL>https://store.com/goods?page=%d</catalogURL>
            <good-item>
                <!--absolute path to item's box-->
                <path>//div[contains(@class,"item")]</path>
                <!--relative path to item's price-->
                <price>.//div[@class="price"]/span/text()</price>
                <!--relative path to item's title-->
                <title>.//div[@class="title"]/a/text()</title>
                <!--relative path to item's page-->
                <url>.//div[@class='title']/a/@href</url>
            </good-item>
            <trash>
                <!--list of rubbish in a good's names, that should be deleted-->
                <!--you can use regex-->
                <item>Суперцена!!!</item>
            </trash>
        </site>
    </sites>
</xml>
```

## Running the tests
run tests without code coverage
```bash
pytest
```
run tests with coverage
```bash
pytest --cov=. tests/
```
## Built With
* Python
* Travis CI
* Codecov.io

## Authors
* __[Kazimirov Danil](https://github.com/ZulusK)__
* __[Rukhailo Pavlo](https://github.com/IceBroForever)__
* __[Artem Herasymov](https://github.com/ArtHerasymov)__

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

[codecov]: https://codecov.io/gh/ZulusK/cose-1/branch/master/graph/badge.svg "Code coverage master"
[travis]: https://travis-ci.org/ZulusK/cose-1.svg?branch=master "Travis CI build status"