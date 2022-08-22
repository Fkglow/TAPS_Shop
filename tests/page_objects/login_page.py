from tests.helpers.support_functions import *

username = 'username'
password = 'password'
login_button = "//*[@id='customer_login']/div/form/p[3]/button"

proper_email1 = 'cotaga1249@maillei.net'
proper_password1 = 'VRrMhK8MqFyd'


def correct_login(driver_instance):
    elem = driver_instance.find_element_by_id(username)
    elem.send_keys(proper_email1)
    elem1 = driver_instance.find_element_by_id(password)
    elem1.send_keys(proper_password1)
    elem2 = driver_instance.find_element_by_xpath(login_button)
    elem2.click()


