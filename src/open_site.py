# src/open_site.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def main():
    # إعداد خيارات المتصفح
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # إذا لاحقاً عايز تشغّل بدون نافذة: uncomment السطر التالي
    # options.add_argument("--headless=new")

    # هذا السطر يحمل ChromeDriver تلقائياً
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        url = "https://example.com"
        driver.get(url)
        print("Opened:", url)
        time.sleep(1)  # نفّذ إيقاف بسيط عشان الصفحة تحمل
        print("Title:", driver.title)

        # مثال: لو عايز تشوف وجود عنصر
        elems = driver.find_elements(By.TAG_NAME, "p")
        print("Found", len(elems), "paragraph(s).")
        for i, e in enumerate(elems[:3], 1):
            print(f"p{i}:", e.text.strip())
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
