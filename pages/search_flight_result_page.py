import softest
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class search_flights_results(BaseDriver):
    # one stop filter
    onestop_filter_xpath = "//section[@id='Flight-APP']//label[2]"
    # onestop flight list
    onestop_flight_list_xpath = "//div[@class='result-set pr grid']/div/div"

    # one stop filter validates on flight search
    def set_filter_validation_OneStop(self):
        self.driver.find_element(By.XPATH, self.onestop_filter_xpath).click()

    # one stop filter validates on flight search
    def set_onestop_flight_validation(self, OneStop):
        self.OneStopList = self.driver.find_elements(By.XPATH, self.onestop_flight_list_xpath)
        print("List of 1 stop", len(self.OneStopList))
        for onestop in self.OneStopList:
            if OneStop in onestop.text:
                 print("assert pass")


