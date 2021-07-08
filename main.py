import page
import unittest
from selenium import webdriver

path_dmc = "C:\\Users\\ashepston\\Downloads\\chromedriver_win32\\chromedriver.exe"
path_home = "C:\\Users\\aidan\\Documents\\chromedriver_win32\\chromedriver.exe"


class DMCHome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.dmcglobal.com/")
        self.driver.implicitly_wait(5)

    def test_home_text(self):
        main_page = page.MainPage(self.driver)
        assert main_page.text_check()

    def test_rotating(self):
        self.driver.implicitly_wait(5)
        main_page = page.MainPage(self.driver)
        assert main_page.rotate_test()

    def test_link1(self):
        main_page = page.MainPage(self.driver)
        assert main_page.link_test1()

    def test_link2(self):
        main_page = page.MainPage(self.driver)
        assert main_page.link_test2()

    def test_top_link1(self):
        main_page = page.MainPage(self.driver)
        assert main_page.top_link1()

    def test_search(self):
        self.driver.implicitly_wait(10)
        main_page = page.MainPage(self.driver)
        assert main_page.search_function()

    def tearDown(self):
        self.driver.quit()


class DMCOurStory(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.dmcglobal.com/our-story")

    def test_text_main(self):
        our_story_page = page.OurStoryPage(self.driver)
        assert our_story_page.text_match_our_story()

    def test_values(self):
        our_story_page = page.OurStoryPage(self.driver)
        assert our_story_page.values_text_match()

    def test_pictures(self):
        our_story_page = page.OurStoryPage(self.driver)
        assert our_story_page.pictures_are_present()

    def test_signup(self):
        our_story_page = page.OurStoryPage(self.driver)
        assert our_story_page.signup_works()

    def test_links(self):
        our_story_page = page.OurStoryPage(self.driver)
        assert our_story_page.sub_link_click()

    def test_to_top(self):
        our_story_page = page.OurStoryPage(self.driver)
        assert our_story_page.to_top()

    def tearDown(self):
        self.driver.quit()


class DMCOurCompanies(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.dmcglobal.com/our-companies")

    def test_main_text(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.text_check()

    def test_link_dyna(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.link_click_dyna()

    def test_link_nobel(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.link_click_nobel()

    def test_contact_link(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.link_click_contact_us()

    def test_dyna_section(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.dyna_section()

    def test_nobel_section(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.nobel_section()

    def test_dyna_bullets(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.dyna_bullet()

    def test_nobel_bullets(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.nobel_bullet()

    def test_sublink(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.sub_link_click()

    def test_to_top(self):
        our_companies_page = page.OurCompaniesPage(self.driver)
        assert our_companies_page.to_top()

    def tearDown(self):
        self.driver.quit()


class DMCInvestors(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.dmcglobal.com/investors")

    def test_text(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.text_check()

    def test_image(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.image_check()

    def test_links(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.link_check()

    def test_signup(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.signup_works()

    def test_news(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.recent_news()

    def test_to_top(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.to_top()

    def test_news_and_events(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.news_and_events()

    def test_company_info(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.company_info()

    def test_shareholder_results(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.shareholder_results()

    def test_stock_info(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.stock_info()

    def test_sec_filing(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.sec_filing()

    def test_governance(self):
        investors_page = page.InvestorsPage(self.driver)
        assert investors_page.governance()
        
    def tearDown(self):
        self.driver.quit()


class DMCNewsSustainability(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.dmcglobal.com/news")

    def test_news(self):
        news_page = page.NewsSustainabilityPage(self.driver)
        assert news_page.news_check()

    def test_sustainability(self):
        sustainability_page = page.NewsSustainabilityPage(self.driver)
        assert sustainability_page.sustainability_check()

    def tearDown(self):
        self.driver.quit()


class DMCContactUs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path_dmc)
        self.driver.get("https://www.dmcglobal.com/contact-us")

    def test_info(self):
        contact_us_page = page.ContactUsPage(self.driver)
        assert contact_us_page.check_info()

    def test_signup(self):
        contact_us_page = page.ContactUsPage(self.driver)
        assert contact_us_page.signup_works()

    def tearDown(self):
        self.driver.quit()
