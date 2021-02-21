import pandas as pd
from bs4 import BeautifulSoup

__author__ = "Dadventures"

""" facebook Gb library """
class FacebookGB():
    event_links = []
    Event_Link = []
    Event_Name = []
    Event_Date = []
    Days_Left = []
    People_Responded = []
    Address = []
    Hosted_By = []
    Descriptions = []
    Tags = []
    Ticket_Purchase_Link = []

    def __init__(self, arg, driver):
        self._driver = driver

    def read(self, file_path):
        """ Reading the Excel file (FB_event_links) consisting of FB Event links from Desktop"""
        self.import_fb_links = pd.read_excel(file_path)
        """ Converting to list """
        self.event_links = self.import_fb_links['FB_Links'].tolist()
        """ assigning event link value """
        self.Event_Link = self.event_links
        """ calling extra function to generate resultset """
        self.parseArguments() # parse arguments
        self._driver.close() # driver close
        self.result() # export result

    def parseArguments(self):
        for i in self.event_links:
            self._driver.get(i)
            html = self._driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            try:
                en = soup.find(class_="_5gmx").text
                self.Event_Name.append(en)
            except:
                self.Event_Name.append("")
            try:
                ed = soup.find('div', class_=['_2ycp _5xhk']).text
                self.Event_Date.append(ed)
            except:
                self.Event_Date.append("")
            try:
                dl = soup.find('div', class_=['_5xhp fsm fwn fcg']).text
                self.Days_Left.append(dl)
            except:
                self.Days_Left.append("")
            try:
                pr = soup.find('span', class_=['_5z74']).text
                self.People_Responded.append(pr)
            except:
                self.People_Responded.append("")
            try:
                ad = soup.find('div', class_=['_4930']).text
                self.Address.append(ad)
            except:
                self.Address.append("")
            try:
                hb = soup.find('div', class_=['_5gnb']).text
                self.Hosted_By.append(hb)
            except:
                self.Hosted_By.append("")
            try:
                ds = soup.find('div', class_=['_63ew']).text
                self.Descriptions.append(ds)
            except:
                self.Descriptions.append("")
            try:
                tg = soup.find('ul', class_=['_63er']).text
                self.Tags.append(tg)
            except:
                self.Tags.append("")
            try:
                tp = self._driver.find_element_by_xpath(
                    "//*[@id='u_0_z']/table/tbody/tr/td[2]/div/div[1]/div/div[2]/div/div").text
                self.Ticket_Purchase_Link.append(tp)
            except:
                self.Ticket_Purchase_Link.append("")

    """ export resultset in xls format"""
    def result(self):
        # Save work in excel file
        data = {}
        data = {'Event_Link': self.Event_Link, 'Event_Name': self.Event_Name, 'Event_Date': self.Event_Date, 'Days_Left': self.Days_Left,
                'People_Responded': self.People_Responded, 'Address': self.Address, 'Hosted_By': self.Hosted_By,
                'Descriptions': self.Descriptions, 'Tags': self.Tags, 'Ticket_Purchase_Link': self.Ticket_Purchase_Link}

        result = pd.DataFrame(data)
        header = ['Event_Name', 'Event_Date', 'Days_Left', 'People_Responded', 'Hosted_By', 'Address', 'Event_Link',
                  'Descriptions', 'Tags', 'Ticket_Purchase_Link']

        result.to_excel("/Users/manishj/Downloads/result.xlsx", columns=header, index=False)