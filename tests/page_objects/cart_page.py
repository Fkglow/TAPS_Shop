import time

from tests.helpers.support_functions import *

item_in_cart = "//*[@id='post-7']/div/div/form/table/tbody/tr[1]"
remove_item_from_cart_button = "//*[@id='post-7']/div/div/form/table/tbody/tr[1]/td[1]/a"
submit_cart = "//*[@id='post-7']/div/div/div[2]/div/div/a"

def check_item_in_cart(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, item_in_cart)
    elem.is_displayed()
