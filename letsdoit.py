from selenium import webdriver as wd
browser = wd.Firefox(executable_path='C:\Program Files\geckodriver\geckodriver')
browser.get('https://www.shufersal.co.il/')
close1 = browser.find_element_by_css_selector('.icon-close-1')
close1.click()
search1 = browser.find_element_by_css_selector('#js-site-search-input')
search1.send_keys('קמח')
search1.submit()
