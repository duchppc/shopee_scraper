from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


def wait_for_products_load(chrome_driver):
    element = WebDriverWait(chrome_driver, 10).until(
        ec.presence_of_element_located(
            (
                By.CLASS_NAME,
                "carousel-arrow",
            )
        )
    )

    return element


def scroll_down(chrome_driver):
    y = 1000

    last_height = chrome_driver.execute_script("return document.body.scrollHeight")

    for timer in range(0, 60):
        chrome_driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 1000
        time.sleep(3)

        if y >= last_height:
            break


def hover_to_photos(chrome_driver, element_to_hover_over):
    hover = ActionChains(chrome_driver).move_to_element(element_to_hover_over)
    hover.perform()
