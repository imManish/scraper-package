import pandas as pd
from bs4 import BeautifulSoup

class FacebookGB:
    event_links=[]
    def __init__(self, arg):
        self._driver = arg

    def read(self, file_path):
        """ Reading the Excel file (FB_event_links) consisting of FB Event links from Desktop"""
        self.import_fb_links = pd.read_excel(file_path)
        """ Converting to list """
        self.event_links = self.import_fb_links['FB_Links'].tolist()
        print(self.event_links)
