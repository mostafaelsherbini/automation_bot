# src/form_fill.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # هنا ممكن تشيل أو تضيف headless حسب رغبتك
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        driver.set_page_load_timeout(20)
        print("Opened form page...")

        time.sleep(2)

        # 1️⃣ نلاقي خانة النص (input)
        text_box = driver.find_element(By.NAME, "my-text")
        text_box.clear()
        text_box.send_keys("Mostafa El Sherbini")

        # 2️⃣ نلاقي زر الإرسال
        submit_button = driver.find_element(By.CSS_SELECTOR, "button")
        submit_button.click()

        print("Filled form and submitted.")
        time.sleep(2)
        print("Current page title:", driver.title)

    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
