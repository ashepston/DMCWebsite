# SeleniumTesting
DMC Website
pip install selenium required
This program tests many seperate aspects of the DMC website, ranging from search bars to links to simple text checks. The element.py file contains some base functions that are 
used repeatedly throughout the program. The locator.py file contains the locators for each of the elements on each page, divided into classes based on what page those locators 
are on. The page.py file contains all of the actual code for each test, with each class again being for each page. Each function does a different task or group of tasks,
which is directly labeled. The main.py file contains all the neccesary unittest framework, allowing for simple error returning and easy to understand results. Each test on 
page.py is shown here.
