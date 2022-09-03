import time
from tests.helpers.support_functions import *


order_confirmation = "//*[@id='post-8']/header/h1"
order_product = "//*[@id='post-8']/div/div/div/section[2]/table/tbody/tr/td/a"
total_price = "//*[@id='post-8']/div/div/div/section[2]/table/tfoot/tr[5]/td/span"

def order_received_confirmation(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, order_confirmation)
    return elem.is_displayed()

def price_is_correct(driver_instance):
    elem = driver_instance.find_element_by_xpath(total_price)
    price_amount = elem.text
    correct_amount = '€61,50'
    if price_amount == correct_amount:
        return True
    else:
        return False


