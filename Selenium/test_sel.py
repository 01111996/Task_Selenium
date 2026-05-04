import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
LOGIN_URL = "https://the-internet.herokuapp.com/login"

#создаю фикстуру:

@pytest.fixture
def sumple_user():
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage")  
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# успешная авторизация:
    
def test_successful_login(sumple_user):
    sumple_user.get(LOGIN_URL)
    sumple_user.find_element(By.ID, "username").send_keys("tomsmith")
    sumple_user.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    sumple_user.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    success_message = sumple_user.find_element(By.CSS_SELECTOR, ".flash.success")
    assert "Welcome to the Secure Area. When you are done click logout below." in success_message.text

 # не успешная автоизация:

def  test_unsuccessful_login(sumple_user):
    sumple_user.get(LOGIN_URL)
    sumple_user.find_element(By.ID, "username").send_keys("prosto1")
    sumple_user.find_element(By.ID, "password").send_keys("nepassword")
    sumple_user.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_message = user.find_element(By.CSS_SELECTOR, ".flash.error")
    assert "This is where you can log into the secure area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages." in error_message.text
