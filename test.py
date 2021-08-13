from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe") #Chromeを動かすドライバを読み込み
driver.get("https://sfc.jp/ie/contact/inquiry/home/form.php")

driver.find_elements_by_css_selector(".submitWrapper")[0].click()

driver.execute_async_script("window.setTimeout(arguments[arguments.length - 1], 3000);")
driver.quit()   
