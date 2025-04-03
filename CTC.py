from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#Connect to Chess.com

def ConnectToChess():
  service = Service("/usr/bin/chromedriver")

  driver = webdriver.Chrome(service=service)
  driver.get("https://www.chess.com")

  driver.find_element(by=By.CLASS_NAME, value="index-cute-bot-icon").click()

  button = driver.find_element(by=By.CSS_SELECTOR,value=".cc-button-component.cc-button-primary.cc-button-xx-large.cc-bg-primary.cc-button-full")
  button.click()

