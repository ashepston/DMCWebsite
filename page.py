
from locator import MainPageLocators
from locator import OurStoryPageLocators
from locator import OurCompaniesLocators
from locator import InvestorsLocators
from locator import NewsSustainabilityLocators
from locator import ContactUsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from element import test_presence
from element import BaseTest
from playsound import playsound
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        if self.driver.find_elements(*OurStoryPageLocators.ClearCookies):
            cookies_button = self.driver.find_element(*OurStoryPageLocators.ClearCookies)
            cookies_button.click()


class MainPage(BasePage):

    def is_title_matches(self):

        return "DMC" in self.driver.title

    def text_check(self):
        text1 = self.driver.find_element(*MainPageLocators.OurStoryTest)
        text2 = self.driver.find_element(*MainPageLocators.TheDmcFamily)
        return "DMC" in text1.text and 'DMC' in text2.text

# Fix this later
    def rotate_test(self):
        playsound('ding.mp3')
        element = self.driver.find_element(*MainPageLocators.NextButton)
        results = []
        text_element1 = self.driver.find_element(*MainPageLocators.RotatingText1)
        text_element2 = self.driver.find_element(*MainPageLocators.RotatingText2)
        text_element3 = self.driver.find_element(*MainPageLocators.RotatingText3)
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(MainPageLocators.RotatingText2))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(MainPageLocators.NextButton))
        results.append('help' in text_element2.text)
        time.sleep(2)
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(MainPageLocators.RotatingText3))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(MainPageLocators.NextButton))
        results.append('nimbly' in text_element3.text)
        element.click()
        print(text_element1.text)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(MainPageLocators.RotatingText1))
        results.append('human' in text_element1.text)
        print(results)
        return False not in results

    def link_test1(self):
        link1 = self.driver.find_element(*MainPageLocators.DynaLink)
        link1.click()
        return 'systems' in self.driver.title

    def link_test2(self):
        link2 = self.driver.find_element(*MainPageLocators.NobelLink)
        link2.click()
        return 'metal' in self.driver.title

    def top_link1(self):
        results = []
        link1 = self.driver.find_element(*MainPageLocators.OurStoryLink)
        link1.click()
        results.append('enabling' in self.driver.title)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.OurCompaniesLink))
        link2 = self.driver.find_element(*MainPageLocators.OurCompaniesLink)
        link2.click()
        results.append('family' in self.driver.title)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.InvestorsLink))
        link3 = self.driver.find_element(*MainPageLocators.InvestorsLink)
        link3.click()
        results.append('investor' in self.driver.title)
        return False not in results

    def search_function(self):
        search_button = self.driver.find_element(*MainPageLocators.SearchButton)
        text_field = self.driver.find_element(*MainPageLocators.TextField)
        search_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.TextField))
        text_field.click()
        text_field.send_keys('Explosion')
        text_field.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.SearchResults))
        results = self.driver.find_element(*MainPageLocators.SearchResults)
        return results.text != '0 Results'


class OurStoryPage(BasePage):
    def text_match_our_story(self):
        results = []
        text_top = self.driver.find_element(*OurStoryPageLocators.MainText)
        subtext = self.driver.find_element(*OurStoryPageLocators.SubImageText)
        bottom_text = self.driver.find_element(*OurStoryPageLocators.BottomText)
        text_medium = self.driver.find_element(*OurStoryPageLocators.MediumTextS)
        results.append('diversified' in text_top.text and 'empowers' in subtext.text)
        results.append('organic' in bottom_text.text)
        results.append('responsive' in text_medium.text)
        return False not in results

    def values_text_match(self):
        values1 = self.driver.find_element(*OurStoryPageLocators.Values1)
        values2 = self.driver.find_element(*OurStoryPageLocators.Values2)
        values3 = self.driver.find_element(*OurStoryPageLocators.Values3)
        values4 = self.driver.find_element(*OurStoryPageLocators.Values4)
        return 'decisions' in values1.text and 'entrepreneurs' in values2.text and 'celebrating' in values3.text and \
               'inspiration' in values4.text

    def pictures_are_present(self):
        picture1 = self.driver.find_element(*OurStoryPageLocators.Picture1)
        picture2 = self.driver.find_element(*OurStoryPageLocators.Picture2)
        return test_presence(picture1, picture2)

    # Failed for some reason
    def signup_works(self):
        return BaseTest.test_signup(self)

    def sub_link_click(self):
        results = []
        sub_link1 = self.driver.find_element(*OurStoryPageLocators.SubLink1)
        sub_link2 = self.driver.find_element(*OurStoryPageLocators.SubLink2)
        sub_link3 = self.driver.find_element(*OurStoryPageLocators.SubLink3)
        sub_link1.click()
        results.append('Overview' in self.driver.current_url)
        sub_link2.click()
        results.append('Culture' in self.driver.current_url)
        sub_link3.click()
        results.append('Tenets' in self.driver.current_url)
        return False not in results

    def to_top(self):
        top_button = self.driver.find_element(*MainPageLocators.UpButton)
        top_button.click()
        return 'content' in self.driver.current_url


class OurCompaniesPage(BasePage):
    def text_check(self):
        main_text1 = self.driver.find_element(*OurCompaniesLocators.MainText1)
        main_text2 = self.driver.find_element(*OurCompaniesLocators.MainText2)
        main_text3 = self.driver.find_element(*OurCompaniesLocators.MainText3)
        dmc_family_text = self.driver.find_element(*OurCompaniesLocators.DMCFamilyText)
        return 'strategically' in main_text1.text and 'united' in main_text2.text and 'collective' in main_text3.text \
               and 'enterprise' in dmc_family_text.text

    def link_click_dyna(self):
        dyna_link = self.driver.find_element(*OurCompaniesLocators.DynaLink)
        dyna_link.click()
        return 'systems' in self.driver.title

    def link_click_nobel(self):
        nobel_link = self.driver.find_element(*OurCompaniesLocators.NobelLink)
        nobel_link.click()
        return 'metal' in self.driver.title

    def link_click_contact_us(self):
        contact_link = self.driver.find_element(*OurCompaniesLocators.ContactUsLink)
        contact_link.click()
        return 'contact' in self.driver.current_url

    def dyna_section(self):
        results = []
        dyna_text1 = self.driver.find_element(*OurCompaniesLocators.DynaText1)
        dyna_text2 = self.driver.find_element(*OurCompaniesLocators.DynaText2)
        dyna_text_link = self.driver.find_element(*OurCompaniesLocators.DynaTextLink)
        results.append(test_presence(dyna_text1, dyna_text2))
        dyna_text_link.click()
        results.append('systems' in self.driver.title)
        return False not in results

    def nobel_section(self):
        results = []
        nobel_text1 = self.driver.find_element(*OurCompaniesLocators.NobelText1)
        nobel_text_link = self.driver.find_element(*OurCompaniesLocators.NobelTextLink)
        results.append(test_presence(nobel_text1))
        nobel_text_link.click()
        results.append('metal' in self.driver.title)
        return False not in results

# Do something here
    def dyna_bullet(self):
        results = []
        button2 = self.driver.find_element(*OurCompaniesLocators.DynaBullet2)
        button3 = self.driver.find_element(*OurCompaniesLocators.DynaBullet3)
        button4 = self.driver.find_element(*OurCompaniesLocators.DynaBullet4)
        image = self.driver.find_element(*OurCompaniesLocators.Images)
        button2.click()
        results.append(test_presence(image))
        button3.click()
        results.append(test_presence(image))
        button4.click()
        results.append(test_presence(image))
        return False not in results

    def nobel_bullet(self):
        results = []
        bullet2 = self.driver.find_element(*OurCompaniesLocators.NobelBullet2)
        bullet3 = self.driver.find_element(*OurCompaniesLocators.NobelBullet2)
        image = self.driver.find_element(*OurCompaniesLocators.Images)
        bullet2.click()
        results.append(test_presence(image))
        bullet3.click()
        results.append(test_presence(image))
        return False not in results

    def sub_link_click(self):
        results = []
        sub_link1 = self.driver.find_element(*OurCompaniesLocators.SubLink1)
        sub_link2 = self.driver.find_element(*OurCompaniesLocators.SubLink2)
        sub_link3 = self.driver.find_element(*OurCompaniesLocators.SubLink3)
        sub_link4 = self.driver.find_element(*OurCompaniesLocators.SubLink4)
        sub_link1.click()
        results.append('Overview' in self.driver.current_url)
        sub_link2.click()
        results.append('Family' in self.driver.current_url)
        sub_link3.click()
        results.append('DynaEnergetics' in self.driver.current_url)
        sub_link4.click()
        results.append('NobelClad' in self.driver.current_url)
        return False not in results

    def to_top(self):
        top_button = self.driver.find_element(*MainPageLocators.UpButton)
        top_button.click()
        return 'content' in self.driver.current_url


class InvestorsPage(BasePage):
    def text_check(self):
        text = self.driver.find_element(*InvestorsLocators.MainText)
        title = self.driver.find_element(*InvestorsLocators.Title)
        lower_text1 = self.driver.find_element(*InvestorsLocators.LowerText1)
        lower_text2 = self.driver.find_element(*InvestorsLocators.LowerText2)
        lower_text3 = self.driver.find_element(*InvestorsLocators.LowerText3)
        lower_text4 = self.driver.find_element(*InvestorsLocators.LowerText4)
        lower_text5 = self.driver.find_element(*InvestorsLocators.LowerText5)
        return test_presence(lower_text1, lower_text2, lower_text3, lower_text4, lower_text5) and 'diversified' in \
            text.text and 'CORPORATE' in title.text

    def image_check(self):
        image1 = self.driver.find_element(*InvestorsLocators.picture1)
        image2 = self.driver.find_element(*InvestorsLocators.picture2)
        image3 = self.driver.find_element(*InvestorsLocators.picture3)
        image4 = self.driver.find_element(*InvestorsLocators.picture4)
        return test_presence(image1, image2, image3, image4)

    def link_check(self):
        results = []
        link1 = self.driver.find_element(*InvestorsLocators.LinkText1)
        link2 = self.driver.find_element(*InvestorsLocators.LinkText1)
        results.append(test_presence(link1, link2))
        link1.click()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window)
        results.append('investor' not in self.driver.title)
        return False not in results

    def signup_works(self):
        return BaseTest.test_signup(self)

    # Error here
    def recent_news(self):
        playsound('ding.mp3')
        results = []
        recent_news_text2 = self.driver.find_element(*InvestorsLocators.RecentNewsText2)
        recent_news_text3 = self.driver.find_element(*InvestorsLocators.RecentNewsText3)
        recent_news_text4 = self.driver.find_element(*InvestorsLocators.RecentNewsText4)
        next_button = self.driver.find_element(*InvestorsLocators.NextButton)
        results.append(test_presence(recent_news_text2))
        next_button.click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_all_elements_located(InvestorsLocators.RecentNewsText3))
        results.append(test_presence(recent_news_text3, recent_news_text4))
        return False not in results

    def to_top(self):
        top_button = self.driver.find_element(*MainPageLocators.UpButton)
        top_button.click()
        return 'content' in self.driver.current_url

    # Failed once
    def news_and_events(self):
        playsound('ding.mp3')
        results = []
        sub_link2 = self.driver.find_element(*InvestorsLocators.SubLink2)
        sub_link2.click()
        if self.driver.find_elements(*OurStoryPageLocators.ClearCookies):
            cookies_button = self.driver.find_element(*OurStoryPageLocators.ClearCookies)
            cookies_button.click()
        news_count = self.driver.find_element(*InvestorsLocators.NewsCount)
        load_more = self.driver.find_element(*InvestorsLocators.LoadMore)
        results.append('events' in self.driver.current_url)
        results.append(news_count.text != '0 Posts')
        news_story1 = self.driver.find_elements(*InvestorsLocators.NewsStory1)
        results.append(test_presence(news_story1))
        load_more.click()
        news_story2 = self.driver.find_elements(*InvestorsLocators.NewsStory2)
        results.append(test_presence(news_story2))
        link1 = self.driver.find_element(*InvestorsLocators.LinkText1)
        link2 = self.driver.find_element(*InvestorsLocators.LinkText1)
        results.append(test_presence(link1, link2))
        link1.click()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window)
        results.append('investor' not in self.driver.title)
        print(results)
        return False not in results

    def company_info(self):
        results = []
        link3 = self.driver.find_element(*InvestorsLocators.SubLink3)
        link3.click()
        main_text = self.driver.find_element(*InvestorsLocators.CompanyInfoMainText)
        biography = self.driver.find_element(*InvestorsLocators.Biography1)
        results.append('Oilfield' in main_text.text)
        results.append(test_presence(biography))
        return False not in results

# not consistent
    def shareholder_results(self):
        playsound('ding.mp3')
        results = []
        link4 = self.driver.find_element(*InvestorsLocators.SubLink4)
        link4.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(InvestorsLocators.ShareholderResults))
        shareholder_results = self.driver.find_element(*InvestorsLocators.ShareholderResults)
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(InvestorsLocators.ShareholderLetter))
        shareholder_letter1 = self.driver.find_element(*InvestorsLocators.ShareholderLetter)
        results.append(shareholder_results.text != '0 Results')
        results.append(test_presence(shareholder_letter1))
        print('shareholder')
        print(results)
        return False not in results

# Find something better for this
    def stock_info(self):
        link5 = self.driver.find_element(*InvestorsLocators.SubLink5)
        link5.click()
        sub_name1 = self.driver.find_element(*InvestorsLocators.SubName1)
        sub_name2 = self.driver.find_element(*InvestorsLocators.SubName2)
        return test_presence(sub_name1, sub_name2)

    def sec_filing(self):
        link6 = self.driver.find_element(*InvestorsLocators.SubLink6)
        link6.click()
        if self.driver.find_elements(*OurStoryPageLocators.ClearCookies):
            cookies_button = self.driver.find_element(*OurStoryPageLocators.ClearCookies)
            cookies_button.click()
        results = []
        sec_count = self.driver.find_element(*InvestorsLocators.SecResultsCount)
        sec_result1 = self.driver.find_element(*InvestorsLocators.SECResult1)
        load_more = self.driver.find_element(*InvestorsLocators.LoadMoreSEC)
        results.append(sec_count != '0 Results')
        results.append(test_presence(sec_result1))
        load_more.click()
        sec_result2 = self.driver.find_element(*InvestorsLocators.SECResult2)
        results.append(test_presence(sec_result2))
        return False not in results

    def governance(self):
        link7 = self.driver.find_element(*InvestorsLocators.SubLink7)
        link7.click()
        bio1 = self.driver.find_elements(*InvestorsLocators.GovernanceBio1)
        bio2 = self.driver.find_elements(*InvestorsLocators.GovernanceBio2)
        return test_presence(bio1, bio2)


class NewsSustainabilityPage(BasePage):
    # Problem Once, second append
    def news_check(self):
        playsound('ding.mp3')
        results = []
        news_results = self.driver.find_element(*NewsSustainabilityLocators.Results)
        load_more = self.driver.find_element(*NewsSustainabilityLocators.LoadMore)
        results.append(news_results.text != '0 Results')
        load_more.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(NewsSustainabilityLocators.News1))
        news1 = self.driver.find_elements(*NewsSustainabilityLocators.News1)
        results.append(test_presence(news1))
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(NewsSustainabilityLocators.News2))
        news2 = self.driver.find_elements(*NewsSustainabilityLocators.News2)
        results.append(test_presence(news2))
        print('news')
        print(results)
        return False not in results

    def sustainability_check(self):
        link = self.driver.find_element(*NewsSustainabilityLocators.SustainabilityLink)
        link.click()
        text = self.driver.find_elements(*NewsSustainabilityLocators.SustainabilityText)
        doc = self.driver.find_elements(*NewsSustainabilityLocators.SustainabilityDoc)
        return test_presence(doc, text)


class ContactUsPage(BasePage):

    # Problem Once, third append
    def check_info(self):
        playsound('ding.mp3')
        results = []
        text1 = self.driver.find_element(*ContactUsLocators.Text1)
        text2 = self.driver.find_element(*ContactUsLocators.Text2)
        contact_results = self.driver.find_element(*ContactUsLocators.Results)
        results.append(test_presence(text1, text2))
        results.append(contact_results.text != '0 Results')
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(ContactUsLocators.Contact2))
        contact2 = self.driver.find_element(*ContactUsLocators.Contact2)
        results.append(test_presence(contact2))
        print('contact us')
        print(results)
        return False not in results

    def signup_works(self):
        return BaseTest.test_signup(self)





















