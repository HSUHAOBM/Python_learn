# pip install -U selenium
# pip install webdriver-manager

# webdriver_manager 會自動根據 google-chrome-stable版本
# 自動在主機內安裝對應的 ChromeDrive 版本，

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())

# 這些建議都加上，不開頁面、禁用GPU加速等等
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(service=service, options=options)

print("Chrome version:", driver.capabilities['browserVersion'])
print("ChromeDriver version:",
      driver.capabilities['chrome']['chromedriverVersion'])


# 開始使用
driver.get('https://www.twse.com.tw/zh/trading/holiday.html')

# input("Press Enter to close the browser...")

# 最後關閉瀏覽器
driver.quit()
