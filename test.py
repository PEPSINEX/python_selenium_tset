from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe") #Chromeを動かすドライバを読み込み
driver.get("https://google.co.jp")
