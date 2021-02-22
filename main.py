from Dadventure.Scraper import Scraper

__author__ = 'Manish Jakhode'


class Main:
    """ initializing scrapper object """
    def __init__(self, terms):
        self.scraper = Scraper(terms)

    """ facebook resources """

    def fbglobalevent(self):
        """ facbookgb get result set"""
        self.scraper.facebookgb.read('/Users/manishj/Downloads/FB_event_links.xls')

    def fbhiddenevent(self,uri):
        """ hidden class attribute fetch """
        self.scraper.facebookhidden.read(uri)

    """ yelp resources """

    def yelpglobalevent(self, uri):
        """ yelp get result set"""
        self.scraper.yelp.read(uri)


#m1 = Main('facebook')
#m1.fbglobalevent()
#m1.fbhiddenevent("https://www.facebook.com/events/325278428447630/")

m2 = Main('yelp')
m2.yelpglobalevent('https://www.yelp.com/search?find_desc=Botanical%20Gardens&find_loc=NYC')
