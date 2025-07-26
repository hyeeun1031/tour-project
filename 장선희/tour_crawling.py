url = "https://www.tripadvisor.co.kr/Attraction_Review-g297884-d1458553-Reviews-Haeundae_Beach-Busan.html"

import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.set_window_size(1920,1080) #반응형 웹의 경우 size를 고정시키는 것이 좋다.
driver.get(url)