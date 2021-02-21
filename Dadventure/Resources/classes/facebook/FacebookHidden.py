from bs4 import BeautifulSoup

__author__ = "Dadventures"

""" Facebook Hidden scrapping data """
class FacebookHidden():
    def __init__(self, arg, driver):
        self._driver = driver

    def read(self, uri):
        print(uri)
        self._driver.get(uri)
        # Note: xpath sometimes get change. If so, please change the xpath address or manually click on "Accept All"
        #self._driver.find_element_by_xpath('//*[@id="u_0_n_Pz"]').click()
        self._driver.find_element_by_xpath('//*[@id="sibling_time_series"]/div[2]/div/a/div/div').click()
        self.result()
        self._driver.close()

    def result(self):
        html = self._driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        raw_data = soup.find('div', class_='uiScrollableAreaContent')
        print(raw_data)
        #.get_attribute("innerHTML")