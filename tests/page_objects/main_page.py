from tests.helpers.support_functions import *

taps_logo = "//*[@id='masthead']/div[1]/div[1]/a/img"

my_account_header_link = 'menu-item-100'
cart_page_header_link = 'menu-item-99'

def logo_is_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, taps_logo)
    return elem.is_displayed()

def go_to_login_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, my_account_header_link)
    elem = driver_instance.find_element_by_id(my_account_header_link)
    elem.click()

