from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from datetime import datetime, timedelta
from selenium.webdriver.firefox.options import Options

# Настройки для запуска в headless режиме
firefox_options = Options()
firefox_options.add_argument('-headless')
# browser = webdriver.Chrome() # Сокращаем команду обращения к браузеру
browser = webdriver.Firefox(options=firefox_options)
browser.set_window_size(1280, 1400)
browser.implicitly_wait(10)

today_date = datetime.today().strftime("%Y-%m-%d")
# print(today_date)
past_date = (datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d")
# print(past_date)

try:
    browser.get('https://mon-dc.mos.ru/')
    time.sleep(5)
    input_login = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div/div/input')
    input_login.send_keys("ambrazhevichav")
    input_passwrd = browser.find_element(By.XPATH, '//form/div[2]/div[2]/div/div/input')
    input_passwrd.send_keys("Lexicon321")
    button = browser.find_element(By.XPATH, '//form/button')
    button.click()
    time.sleep(10)

    browser.get('https://mon-dc.mos.ru/d/1_hpN8jWz/systems?orgId=1&refresh=1m&var-system_name=%D0%A6%D0%90%D0%A4%D0%90%D0%9F&var-vm=All')
    date_input_button = browser.find_element(By.XPATH, '//header/nav/div[2]/div[1]/div[1]/button[1]')
    date_input_button.click()
    # Ввод фильтра прошлой даты
    past_input = browser.find_element(By.XPATH, '//section/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[1]/input')
    past_input.clear()
    past_input.send_keys(past_date)
    # Ввод фильтра сегодняшней даты
    today_input = browser.find_element(By.XPATH, '//section/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/input')
    today_input.clear()
    today_input.send_keys(today_date)
    # Применить фильтр
    apply_input_button = browser.find_element(By.XPATH, '//section/div/div[1]/div[2]/div[1]/div[2]/button')
    apply_input_button.click()
    time.sleep(5)
    test_hide_button = browser.find_element(By.XPATH, '//main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[13]/div/button')
    test_hide_button.click()
    time.sleep(15)
    browser.save_screenshot("screenshot.png")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
