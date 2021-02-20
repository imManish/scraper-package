# Dadventures Scraper Python 
This is the official Python bindings to the Dadventures Scraper scripts

## Installation
This library requires Python 3.0 or later

It is recommended to install this library using PyPi inside a virtualenv
* Create the virtualenv (Python 3!) and activate it:
```
$ virtualenv -p python3  dadventures
$ cd dadventures && source bin/activate
```
* Install from PyPi:
```
$ pip install -r requirements.txt
```

## Quick Start

```python
from Dadventure.Scraper import Scraper
# parameters could be facebook or yelp
client = Scraper('facebook') 
```

## Resources
Below is a list of resources with there available methods

### FacebookGb
```python
# read xls files
client.facebookgb.read(file_path)
```


