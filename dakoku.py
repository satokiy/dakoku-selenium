from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os

# get env
load_dotenv()
USER = os.getenv('DAKOKU_USER')
PW = os.getenv('DAKOKU_PW')

driver = webdriver.Chrome(ChromeDriverManager().install())

# Access Smartlink
url = os.getenv('DAKOKU_URL')

driver.get(url)

time.sleep(1)

## Login
login_id = driver.find_element_by_name("USER_ID")
login_id.send_keys(USER)
login_pw = driver.find_element_by_name("USER_PW")
login_pw.send_keys(PW)
login_btn = driver.find_element_by_name("login").click()

time.sleep(2)

frame = driver.find_element_by_name("right")
driver.switch_to_frame(frame)
#exit_btn = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/div[1]/table/tbody/tr[2]/td/input")
exit_btn = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/input")

exit_btn.click()

print(driver.title)

