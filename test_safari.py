from selenium import webdriver
driver = webdriver.Safari()

driver.get("https://www.google.com")
print("Window size", driver.get_window_size())