import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

 
def test_login():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://azure.microsoft.com/en-us/services/devops/")
    driver.find_element(By.CLASS_NAME,"devops-signin").click()
    driver.find_element(By.NAME, "loginfmt").send_keys("t-bpadaliya@microsoft.com")
    driver.find_element(By.ID, "idSIButton9").click()
    sleep(20)
    driver.find_element(By.ID, "idBtn_Back").click()
    driver.find_element(By.ID, "__bolt-ms-vss-test-web-test-hub-group-link").click()
    visible = driver.find_element(By.CLASS_NAME, "bolt-header-title").is_displayed()
    assert visible
    sleep(3)
    driver.quit()