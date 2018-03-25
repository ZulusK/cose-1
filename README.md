# cose-1
[![Build Status][travis]](https://travis-ci.org/ZulusK/cose-1)
[![codecov][codecov]](https://codecov.io/gh/ZulusK/cose-1)

Сontains the source code for the first assignment (Components of Software Engineering, 2018, KP-61, FAM, KPI).
#### [Demo](#)
These days it's getting crucial for the wayfaring Internet users to orient themselves in the superfluity of dazzling ads,for it is the last resort in disclosing the most expedient price for the desired product. To that end, we proudly present a piece of software that would automatically analyse the market for you, and eventually bestow the user with a recommended venue to carry out the purchase.
### Prerequisites
 You will need Telegram client to use our bot or any OS with python3 to run console application.
## Getting Started
1. install dependecies
```bash
pip install
```
2. install Geckodriver - firefox webdriver (Linux x64)
```bash
sudo chmod + install_geckodriver_ubuntu.sh
sudo ./install_geckodriver_ubuntu.sh
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