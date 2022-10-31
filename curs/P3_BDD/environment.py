from curs.P3_BDD.browser import Browser
from curs.P3_BDD.pages.advanced_search_page import Advanced_search_page
from curs.P3_BDD.pages.home_page import Home_page

def before_all(context):
		context.browser = Browser()
		context.home_page_object = Home_page()
		context.advanced_search_page_object = Advanced_search_page()

def after_all(context):
		context.browser.close()