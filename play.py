import CTC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Play:
  def play_with_bot(self):
    driver = CTC.ConnectToChess()
    wait = WebDriverWait(driver,10)

    try : 
      bot_button = driver.find_element(By.CLASS_NAME,value="index-guest-button-title")
      sleep(1)
      bot_button.click()
      del bot_button
    except:
      pass
    
    sleep(11)

    button = driver.find_element(by=By.CSS_SELECTOR, 
    value=".cc-button-component.cc-button-primary.cc-button-xx-large.cc-bg-primary.cc-button-full.bot-selection-cta-button-button")    
    
    wait.until(EC.element_to_be_clickable(button))

    button.click()

    sleep(3)

    move_piece(driver=driver,from_square=42,to_square=44)  

    sleep(100)

  def play_with_other(self):
    CTC.ConnectToChess()

def move_piece(driver, from_square, to_square):
    # First click the piece you want to move
    pieces = driver.find_elements(by=By.CLASS_NAME, value="piece")
    for piece in pieces:
        if f"square-{from_square}" in piece.get_attribute("class"):
            piece.click()
            break

    # Then click the destination square
    squares = driver.find_elements(by=By.CLASS_NAME, value="hint")
    for square in squares:
        if f"square-{to_square}" in square.get_attribute("class"):
            wait = WebDriverWait(driver,10)
            wait.until(EC.element_to_be_clickable(square))
            square.click()
            break
    
    # Add a small delay to allow the move to complete
    sleep(0.5)

