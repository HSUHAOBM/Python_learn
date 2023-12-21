from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas
from datetime import datetime

url = 'https://fund.cnyes.com/Fixedincome/search.aspx'

service = Service(executable_path=ChromeDriverManager().install())

# 這些建議都加上，不開頁面、禁用GPU加速等等
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-infobars")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(service=service, options=options)

print("Chrome version:", driver.capabilities['browserVersion'])
print("ChromeDriver version:", driver.capabilities['chrome']['chromedriverVersion'])

driver.get(url=url)

# 計價幣別為(台幣)
select_element = driver.find_element("xpath", '//*[@id="ctl00_ContentPlaceHolder1_DD_classCurrent"]')
Select(select_element).select_by_index(10)

# 投資區域（全球市場）
driver.find_element("xpath", '//*[@id="ctl00_ContentPlaceHolder1_DropDownList1"]').click()
driver.find_element("xpath", '//*[@id="ctl00_ContentPlaceHolder1_DropDownList1"]/option[8]').click()

# # 基金組別（高收益債）
# driver.find_element("xpath", '//*[@id="ctl00_ContentPlaceHolder1_DropDownList2"]').click()
# driver.find_element("xpath", '//*[@id="ctl00_ContentPlaceHolder1_DropDownList2"]/option[7]').click()

# 年化配息率（2%）
driver.find_element("xpath", '//*[@id="aspnetForm"]/div[4]/div[1]/select[1]').click()
driver.find_element("xpath", '//*[@id="aspnetForm"]/div[4]/div[1]/select[1]/option[4]').click()

# 至（4%以上）
driver.find_element("xpath", '//*[@id="aspnetForm"]/div[4]/div[1]/select[2]').click()
driver.find_element("xpath", '//*[@id="aspnetForm"]/div[4]/div[1]/select[2]/option[2]').click()

# 配息頻率
driver.find_element("xpath", '//*[@id="div_type"]').click()
driver.find_element("xpath", '//*[@id="div_type"]/option[4]').click()

# 搜尋
driver.find_element("xpath", '//*[@id="aspnetForm"]/div[4]/div[3]/button').click()

time.sleep(5)

# 三年績效排序
driver.find_element("xpath", '/html/body/div[2]/section[3]/div/div[4]/table[2]/thead/tr/th[3]/select').click()
driver.find_element("xpath", '/html/body/div[2]/section[3]/div/div[4]/table[2]/thead/tr/th[3]/select/option[6]').click()

time.sleep(5)

html_source = driver.page_source
driver.close()

soup = BeautifulSoup(html_source, 'lxml')

# # 找到目標 table
# target_table = soup.find('table', class_='search_result_table')

fund_dict = {
    '基金名稱': [],
    '淨值': [],
    '三年績效': [],
    '配息日': [],
    '配息金額': [],
    '年化配息率': [],
    '晨星評級': [],
    '連結': []
}

# 第一個 tbody 中的 tr
for tr in soup.select_one('tbody').select('tr'):
    # 評定等級
    morning_star = len(tr.select('td')[5].select('li.on'))

    if morning_star >= 3:

        fund_dict['基金名稱'].append(tr.select('td')[0].text.strip())
        fund_dict['淨值'].append(tr.select('td')[1].text.strip().split('\n')[0])
        fund_dict['三年績效'].append(tr.select('td')[2].text.strip())
        fund_dict['配息日'].append(tr.select('td')[3].text.strip().split('\n')[-1].strip())
        fund_dict['配息金額'].append(tr.select('td')[4].text.strip().split('\n')[0].strip())
        fund_dict['年化配息率'].append(tr.select('td')[4].text.strip().split('\n')[-1].strip())
        fund_dict['晨星評級'].append(morning_star)
        fund_dict['連結'].append('https://fund.cnyes.com' + tr.select('td')[0].a['href'].strip().replace(' ', '%20'))


print(fund_dict)

df = pandas.DataFrame(fund_dict)
df.set_index('基金名稱', inplace=True)
date = datetime.today().strftime("%Y%m%d")
file_name = '{}_基金搜尋.csv'.format(date)
df.to_csv(file_name, encoding='utf_8_sig')