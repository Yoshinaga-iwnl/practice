from selenium import webdriver


url = ""
xpath = '//*[@id="memberlist"]/ul[18]/li/p/a'
driver = webdriver.Chrome(executable_path="/Users/vital/Downloads/chromedriver")

for cnt in range(0,10):
	driver.get(url)

	driver.find_element_by_xpath(xpath).click()

	for cookie in driver.get_cookies():
		print(cookie)
	driver.delete_all_cookies()

	for cookie in driver.get_cookies():
		print(cookie)

driver.quit()