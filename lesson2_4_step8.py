import time
import math

import pyperclip
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def main():
    try:
        browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        browser.find_element_by_id("book").click()

        x = browser.find_element_by_id("input_value").text
        value = str(math.log(math.fabs(12 * math.sin(int(x)))))
        browser.find_element_by_id("answer").send_keys(value)
        browser.find_element_by_id("solve").click()

        pyperclip.copy(browser.switch_to.alert.text.split(':')[1].strip())
    finally:
        time.sleep(4)
        browser.quit()


if __name__ == "__main__":
    main()
