from selenium.webdriver.support.ui import WebDriverWait
from locator import OurStoryPageLocators
from selenium.webdriver.support import expected_conditions as EC


def test_presence(test_object1, test_object2=True, test_object3=True, test_object4=True, test_object5=True):
    element1 = test_object1
    element2 = test_object2
    element3 = test_object3
    element4 = test_object4
    element5 = test_object5
    if element1 and element2 and element3 and element4 and element5:
        return True
    else:
        return False


class BaseTest(object):

    def __init__(self, driver):
        self.driver = driver

    def test_signup(self):
        submit_button = self.driver.find_element(*OurStoryPageLocators.SubmitButton)
        text_field = self.driver.find_element(*OurStoryPageLocators.TextField)
        consent_button = self.driver.find_element(*OurStoryPageLocators.ConsentButton)
        consent_button.click()
        text_field.click()
        text_field.send_keys('test@dmcglobal.com')
        submit_button.click()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window)
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(OurStoryPageLocators.Confirmation))
        confirmation = self.driver.find_element(*OurStoryPageLocators.Confirmation)
        return 'subscription' in confirmation.text
