import urllib.request as url

class YelpGB:
    """ initializing Yelp Gb Class"""
    def __init__(self, arg):
        self._diver = arg.driver

    """ read method for reading yelp resources"""
    def read(self, uri):
        print(uri)
        #source = url.urlopen(uri)
        #print(source)
