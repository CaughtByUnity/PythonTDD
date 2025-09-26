from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service('/home/caughtbyunity/PycharmProjects/PythonTDD/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('http://localhost:8000')

assert "The install worked successfully! Congratulations!" in driver.title