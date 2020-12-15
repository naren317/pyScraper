# pyScraper :
Scrapes the resulting pages of google search and stores the data in an excelsheet. parserConfig.config contains the configuration for the script.

# Dependencies :
python 3.5 or higher and pip3 for installing dependent libraries.

# Installation :
Get python setuptools (needs <i>sudo</i>) :<br><br>
`
$ sudo pip3 install setuptools
`
<br><br>Run <i>setup.py</i><br><br>
`
$ sudo python3 setup.py install
`
# Usage :
In order to perform a google search for a keyword :<br><br>
`
$ python3 Scraper.py <KEYWORD>
`
<br><br>The generated results are automatically stored in the path provided in <i>parserConfig.config</i> under the tag <i>ResultFileLocation</i>, which can be modified as per convenience. pyScraper can also be run with pre-defined keyword, which needs to be set in the <i>parserConfig.config</i> under <i>"DefaultSearchKeyword"</i> tag.
