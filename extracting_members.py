from selenium.webdriver.common.by import By
import time
from search import search


def extract_member(driver, page, lv, target_group):
    driver.refresh()
    search(driver, target_group)
    time.sleep(10)
    try:
        members = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/div[4]/div/header/div[2]/div[2]/span",
        ).text
    except:
        pass
    members = members.split(",")
    members_list = []
    for member in members:
        # if "+" in member:
        #     member = member.replace(" +", "")
        #     member = member.replace(" ", "")
        members_list.append(member.strip())
    return members_list
