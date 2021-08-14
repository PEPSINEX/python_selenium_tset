from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://sfc.jp/ie/contact/inquiry/home/form.php")

inputList = driver.find_elements_by_xpath("//input[not(contains(@type, 'hidden'))]")

print('Start')
for inputNode in inputList:
    print(inputNode.get_attribute('outerHTML'))
print('End')

driver.quit()
