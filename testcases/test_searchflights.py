import pytest
import softest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from pages.search_flight_result_page import search_flights_results
from pages.yatra_launch_page import LaunchPage

@pytest.mark.usefixtures("setup")
class Test_SearchOneStopFlight():

    @pytest.fixture(autouse=True)
    def class_setup(self):
       self.lp = LaunchPage(self.driver)


    def test_searchflights(self):
        
        SF = self.lp.set_SearchFlights("Bangalore (BLR)","Hyderabad (HYD)","10/04/2024")
        # lp.set_DepartureFrom("Bangalore (BLR)")
        # self.driver.implicitly_wait(10)
        # lp.set_GoingTo("Hyderabad (HYD")
        # lp.set_dateselection("10/04/2024")
        # lp.set_searchbutton()
        
        # sf = search_flights_results(self.driver)
        SF.set_filter_validation_OneStop()
        SF.set_onestop_flight_validation("1 Stop")






