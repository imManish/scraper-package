from selenium import webdriver
from sys import platform
from Dadventure.Resources.classes.facebook.FacebookGB import FacebookGB
from Dadventure.Resources.classes.facebook.FacebookHidden import FacebookHidden
from Dadventure.Resources.classes.yelp.YelpGB import YelpGB

""" Exception class for unsupported platform """
class UnsupportedPlatform(Exception):
    pass

__author__ = "Dadventures"

class Driver:
    def __init__(self, term):
        if "linux" in platform:
            pass
        elif "darwin" in platform:
            self.driver = webdriver.Chrome(executable_path='/Users/manishj/Downloads/chromedriver')
        elif "win" in platform:
            self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
        else:
            raise UnsupportedPlatform

        # New Resources
        if term == 'facebook':
            self.facebookgb = FacebookGB(self, self.driver)
            self.facebookhidden = FacebookHidden(self, self.driver)
        else:
            print("here")
            self.yelp = YelpGB(self, self.driver)
