from os import environ as env
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-data-dir=/Users/Zach/Library/Application Support/Google/Chrome/Profile 2")
driver = webdriver.Chrome(options=options)
driver.get("https://secure07c.chase.com/web/auth/#/logon/logon/chaseOnline?")

driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "userId-text-input-field"))).send_keys("zjleblanc27")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password-text-input-field"))).send_keys(env.get("CHASE_PWD"))

driver.find_element(By.CSS_SELECTOR, "button#signin-button").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.seeAllOffer"))).click()

offers = True
while offers:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.offerList")))
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "iconAddToCard")))
    except:
        offers = False
        continue
    driver.find_element(By.CSS_SELECTOR, "span.iconAddToCard [type=button]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "flyoutClose"))).click()

driver.close()