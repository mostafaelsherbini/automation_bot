from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # إعداد المتصفح
    options = Options()
    options.add_argument("--headless=new")  # شغل المتصفح بدون واجهة (اختياري)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("🚀 Opening login page...")
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        print("🧠 Typing username and password...")
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        username.send_keys("student")
        password.send_keys("Password123")

        print("🔘 Clicking login button...")
        login_button = driver.find_element(By.XPATH, "//button[@id='submit']")
        login_button.click()
        time.sleep(2)

        print("✅ Checking login result...")
        success_msg = driver.find_element(By.TAG_NAME, "h1").text
        print("Result:", success_msg)

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()
        print("🧹 Browser closed.")

if __name__ == "__main__":
    main()
