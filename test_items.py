import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_is_exist(browser):
	browser.get(link)
	time.sleep(30)
	add_to_basket = browser.find_element_by_css_selector("button.btn-add-to-basket")
