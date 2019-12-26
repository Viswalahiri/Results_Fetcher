# Gitam_Results

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

A fun project to retrieve large amounts of data from the results forms on GITAM's online results [website](https://doeresults.gitam.edu/onlineresults/pages/Newgrdcrdinput1.aspx).

> This project is a sub-project for an automatic student grades analaysis project. Currently, results of **CSE** batches of **2021** and **2022** can be retrieved. More batches and branches will be supported soon.**

Implemented with [Selenium](https://github.com/SeleniumHQ/selenium) (Python 3) in Python, this repository contains code that helps in automating web browsers to retrieve student examination results. This data can be further used, for analytical purposes to monitor student/section performance.


## Prerequisites

This package assumes using Python 3.x. 

Expected package dependencies are listed in the "requirements.txt" file for PIP, you need to run the following command to get dependencies:
```
pip install -r requirements.txt
```

Browser-specific drivers are to be installed.

Mozilla Firefox 70.0.x : [GeckoDriver](https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-win64.zip)

Chrome 79.0.x / Chromium (Not Tested): [ChromeDriver](https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_win32.zip)

## Examples

```
Enter semester, batch year, and section number.
5 2021 17
```

## Contributing

1. [Fork](https://github.com/Viswalahiri/Gitam_Results/fork) this project.
2. Commit your changes.
3. Create a new Pull Request and link an [issue](https://github.com/Viswalahiri/Gitam_Results/issues/new) with it.


## Meta

Viswalahiri Swamy Hejeebu – [@viswalahiri](https://github.com/viswalahiri) – Message me on [LinkedIn](https://www.linkedin.com/in/viswalahiri/) or send me an [e-mail](mailto:viswalahiriswamyh@gmail.com) for any queries.

Distributed under the [GNU License](https://opensource.org/licenses/GPL-3.0). See [`LICENSE`](https://github.com/Viswalahiri/Gitam_Results/blob/master/LICENSE) for more information.
