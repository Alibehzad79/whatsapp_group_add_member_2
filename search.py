import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def search(driver, text):
    time.sleep(5)
    os.system(f"echo {text}|clip")
    try:
        search_box = driver.find_element(
            By.XPATH, '//div[@title="Search input textbox"]'
        )
        search_box.click()
        time.sleep(1)
        search_box.send_keys(Keys.CONTROL, "v")
        time.sleep(5)
    except:
        pass
    try:
        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]",
        ).click()
        time.sleep(2)
    except:
        pass
