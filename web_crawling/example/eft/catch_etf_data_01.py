# 復華 ETF 爬取
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

import re

from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime,timedelta

url = 'https://www.fhtrust.com.tw/ETF/etf_list'

service = Service(executable_path=ChromeDriverManager().install())

# 這些建議都加上，不開頁面、禁用GPU加速等等
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(service=service, options=options)

print("Chrome version:", driver.capabilities['browserVersion'])
print("ChromeDriver version:", driver.capabilities['chrome']['chromedriverVersion'])

driver.get(url=url)

fund_dict = {
    '日期': [],
    '基金資產淨值': [],
    '基金在外流通單位數': [],
    '基金每單位淨值': [],
}

start_date = datetime.strptime("2023/12/3", "%Y/%m/%d")
end_date = datetime.strptime("2023/12/8", "%Y/%m/%d")

try:
    time.sleep(5)

    # 使用 XPath 定位輸入框
    input_xpath = '//*[@id="app"]/main/section/div[1]/div/div[2]/div[2]/div/div/input'
    input_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, input_xpath)))

    # 在輸入框中輸入 "etf代號"
    # input_element.send_keys("00929")
    input_element.send_keys("00878")

    # 按下 Enter 鍵 搜尋
    input_element.send_keys(Keys.ENTER)

    # 點擊搜尋結果
    try:
        result_xpath = '//*[@id="app"]/main/section/div[1]/div/div[2]/div[2]/div/div/div[2]/ul/li'
        result_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, result_xpath)))
        result_element.click()

        # 去分頁
        target_element_xpath = '//*[@id="tns1-item2"]'
        target_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, target_element_xpath)))

        # 點擊目標元素
        target_element.click()

        # 使用 XPath 定位日期輸入框
        date_input_xpath = '//*[@id="etfPanel3"]/section[1]/div/div/div[1]/div/input'
        date_input_element = driver.find_element(By.XPATH, date_input_xpath)

        # 日期範圍資料蒐集
        current_date = start_date
        while current_date <= end_date:
            # 使用 JavaScript 設定日期值
            driver.execute_script("arguments[0].value = '{}';".format(current_date.strftime("%Y/%m/%d")), date_input_element)

            # 搜尋,指定日期
            search_button_xpath = '//*[@id="etfPanel3"]/section[1]/div/div/div[2]/div/button'
            search_button_element = driver.find_element(By.XPATH, search_button_xpath)
            search_button_element.click()

            time.sleep(1)

            no_data_locator = (By.XPATH, '//*[@id="etfPanel3"]/div/section/div/p')
            try:
                # 等待元素出現，最多等待 2 秒
                element = WebDriverWait(driver, 2).until(EC.presence_of_element_located(no_data_locator))
                print(f'{current_date} 無資料,{element.text}')

            except:
                print(f'{current_date} 有資料')

                # re.sub(r'\s', '', text)，正則去除所有空白字符
                # 基金資產淨值
                asset_value_xpath = '//*[@id="etfPanel3"]/section[2]/div/div[2]/div/div[1]/div'
                asset_value_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, asset_value_xpath)))
                asset_value = re.sub(r'\s', '', asset_value_element.get_attribute('textContent').replace('NTD', ''))

                # 基金在外流通單位數
                unit_xpath = '//*[@id="etfPanel3"]/section[2]/div/div[2]/div/div[2]/div'
                unit_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, unit_xpath)))
                unit_value = re.sub(r'\s', '', unit_element.get_attribute('textContent').replace('NTD', ''))

                # 基金每單位淨值
                net_value_xpath = '//*[@id="etfPanel3"]/section[2]/div/div[2]/div/div[3]/div'
                net_value_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, net_value_xpath)))
                net_value = re.sub(r'\s', '', net_value_element.get_attribute('textContent').replace('NTD', ''))

                fund_dict['日期'].append(current_date.strftime("%Y/%m/%d"))
                fund_dict['基金資產淨值'].append(asset_value)
                fund_dict['基金在外流通單位數'].append(unit_value)
                fund_dict['基金每單位淨值'].append(net_value)


            current_date += timedelta(days=1)

    except:
        print('沒有這個代號')
except Exception as e:
    print(e)
finally:
    # 關閉瀏覽器視窗
    driver.quit()


print(fund_dict)

# data = {
#     '日期': ['2023/12/01', '2023/12/04', '2023/12/05', '2023/12/06', '2023/12/07', '2023/12/08', '2023/12/11', '2023/12/12', '2023/12/13', '2023/12/14', '2023/12/15', '2023/12/18'],
#     '基金資產淨值': ['106,994,957,274', '107,799,380,136', '107,311,610,274', '107,918,912,894', '107,483,363,345', '108,472,516,124', '109,040,971,843', '110,596,447,769', '113,561,712,209', '116,863,030,859', '115,362,689,370', '114,032,331,150'],
#     '基金在外流通單位數': ['5,802,639,000', '5,803,639,000', '5,804,639,000', '5,806,639,000', '5,808,639,000', '5,809,139,000', '5,810,639,000', '5,815,139,000', '5,856,639,000', '5,916,639,000', '5,916,639,000', '5,919,639,000'],
#     '基金每單位淨值': ['18.44', '18.57', '18.49', '18.59', '18.5', '18.67', '18.77', '19.02', '19.39', '19.75', '19.5', '19.26']
# }

# 將字典轉換為DataFrame
df = pd.DataFrame(fund_dict)

# 將資料列印出來
print(df)

# df.set_index('etf', inplace=True)
# date = datetime.today().strftime("%Y%m%d")
# file_name = '{}_搜尋.csv'.format(date)
# df.to_csv(file_name, encoding='utf_8_sig')