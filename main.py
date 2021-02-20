from Dadventure.Scraper import Scraper

__author__ = 'Manish Jakhode'


class Main:
    """ initializing scrapper object """

    def __init__(self, terms):
        self.scaper = Scraper(terms)

    """ facebook resources """

    def fbglobalevent(self):
        """ facbookgb get result set"""
        self.scaper.facebookgb.read('/Users/manishj/Downloads/FB_event_links.xls')

    def fbhiddenevent(self):
        """ hidden class attribute fetch """
        self.scaper.facebookhidden.execute()

    """ yelp resources """

    def yelpglobalevent(self):
        """ yelp get result set"""
        self.scraper.yelp.read('https://www.yelp.com/search?find_desc=Botanical%20Gardens&find_loc=NYC')


m1 = Main('facebook')
m1.fbglobalevent()
m1.fbhiddenevent()

# m2 = main('yelp')
# m2.yelpglobalevent()
