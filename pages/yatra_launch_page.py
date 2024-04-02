import softest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver

from base.base_driver import BaseDriver
from pages.search_flight_result_page import search_flights_results


class LaunchPage(BaseDriver):
    # flight departure from
    flight_departure_xpath = "//label[@for='BE_flight_origin_city']"
    flight_departure_origin_xpath = "//input[@id='BE_flight_origin_city']"
    departure_list_xpath = "//div[@class='viewport']//div [@class='ac_airport']"

    # flight going to
    flight_going_to_location_xpath = "//input[@id='BE_flight_arrival_city']"
    flight_going_to_list_xpath = "//div[@class='viewport']//div[1]/li"
    # date selection from calender
    date_selection_ion_xpath = "//input[@id='BE_flight_origin_date']"
    date_selection_from_calender = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD'] "
    # flight search
    search_xpath = "//input[@value='Search Flights']"

        # flight departure from
    def set_DepartureFrom(self,DepatureLocation):
        self.depart_from = self.driver.find_element(By.XPATH, self.flight_departure_xpath)
        self.depart_place = self.driver.find_element(By.XPATH, self.flight_departure_origin_xpath)
        self.depart_place.click()

        self.depart_list = self.driver.find_elements(By.XPATH, self.departure_list_xpath)
        print(len(self.depart_list))
        for i in self.depart_list:
            if DepatureLocation in i.text:
                i.click()
                break

    def set_GoingTo(self,GoingtoLocation):
        self.going_to = self.driver.find_element(By.XPATH, self.flight_going_to_location_xpath)
        self.going_to.click()
        # self.going_to.send_keys(Keys.ENTER)

        self.arrival_lists = self.driver.find_elements(By.XPATH, self.flight_going_to_list_xpath)
        for arrival in self.arrival_lists:
            if GoingtoLocation in arrival.text:
                arrival.click()
                break

    #selecting date
    def set_dateselection(self,selectdate):
        self.calender = self.driver.find_element(By.XPATH,self.date_selection_ion_xpath)
        self.calender.click()

        self.calender_dates = self.driver.find_elements(By.XPATH,self.date_selection_from_calender)
        print(len(self.calender_dates))

        for date in self.calender_dates:
            if date.get_attribute("data-date") == selectdate:
                date.click()
                break


 #search flight
    def set_searchbutton(self):
        self.driver.find_element(By.XPATH,self.search_xpath).click()

    def set_SearchFlights(self,DepatureLocation , GoingtoLocation, selectdate):
        self.set_DepartureFrom(DepatureLocation)
        self.set_GoingTo(GoingtoLocation)
        self.set_dateselection(selectdate)
        self.set_searchbutton()
        self.search_flights_results_view = search_flights_results(self.driver)
        return self.search_flights_results_view