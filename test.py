from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe") #Chromeを動かすドライバを読み込み
driver.get("https://sfc.jp/ie/contact/inquiry/home/form.php")

element = driver.find_element_by_name("q")
element.send_keys("Selenium WebDriver")
element.submit()

driver.quit()
