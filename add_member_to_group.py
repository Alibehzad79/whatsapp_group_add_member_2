import flet as ft
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from search import search
from datetime import datetime


def add_member(driver, page, lv, my_group, members):
    counter_btn = ft.TextButton(text="Added Member: 0")
    lv.controls.append(counter_btn)
    page.update(lv)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    time.sleep(5)
    driver.refresh()
    search(driver, my_group)
    try:
        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/div[4]/div/header/div[2]/div[1]/div/span",
        ).click()
        time.sleep(5)
    except:
        pass
    try:
        driver.find_element(By.XPATH, "//div[text()='Add member']").click()
        time.sleep(5)
    except:
        pass
    counter = 0
    for member in members:
        os.system(f"echo {member}|clip")
        try:
            search_box = driver.find_element(
                By.XPATH, '//div[@title="Search input textbox"]'
            )
            search_box.click()
            time.sleep(1)
            search_box.send_keys(Keys.CONTROL, "v")
            time.sleep(2)
        except:
            pass
        try:
            driver.find_element(By.XPATH, f'//span[@title="{member}"]').click()
            time.sleep(2)
        except:
            pass
        try:
            search_box = driver.find_element(
                By.XPATH, '//div[@title="Search input textbox"]'
            )
            search_box.send_keys(Keys.CONTROL, "a")
            search_box.send_keys(Keys.DELETE)
        except:
            pass
        counter += 1
        counter_btn.text = f"Added Member: {counter}"
        page.update(lv)
        if counter >= 250:
            break

    time.sleep(5)
    try:
        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/span[2]/div/span/div/div/div/div/div/div/span[2]/div/div/div",
        ).click()
        time.sleep(5)
    except:
        pass
    try:
        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]",
        ).click()
        time.sleep(4)
    except:
        pass
    try:
        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]",
        ).click()
    except:
        pass

    try:
        driver.find_element(
            By.XPATH,
            "//div[@aria-label='Next']",
        ).click()
    except:
        pass
    lv.controls.append(ft.Text(f"{counter} Members added."))
    page.update(lv)
