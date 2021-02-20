from selenium import webdriver
from sys import platform
from Dadventure.Resources.classes.FacebookGB import FacebookGB
from Dadventure.Resources.classes.FacebookHidden import FacebookHidden

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
            self.facebookgb = FacebookGB(self)
            self.facebookhidden = FacebookHidden(self)
        else:
            print("here")
            #self.yelp = Yelp(self)
