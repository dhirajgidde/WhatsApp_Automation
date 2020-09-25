from selenium import webdriver
import time


driver =webdriver.Chrome()

driver.get("https://web.whatsapp.com/")



time.sleep(10)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[16]/div/div/div[2]").click()

time.sleep(6)

i=0

while i<600:

    text=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]")

    text.send_keys("System Error: Gradle Build Failure....")

    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()
    i=i+1
    print(i)

time.sleep(5)
driver.close()