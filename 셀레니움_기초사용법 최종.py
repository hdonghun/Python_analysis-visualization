from re import search
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv  

browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) #로딩이 끝날 떄 까지 10초를 기다려 줍니다.

# 쇼핑 메뉴 클릭
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

#검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

#검색어 입력
search.send_keys('화장품')
search.send_keys(Keys.ENTER)

#스크롤 전 높이
befor_h = browser.execute_script("return window.scrollY")

#무한 스크롤
while True:
    #맨 아래로 스크롤을 내려줍니다.
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    #스크롤 사이 로딩 시간 추가
    time.sleep(2)

    #스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    
    #스크롤 처음부터 끝까지 만들어주는 함수
    if after_h == befor_h:
        break
    befor_h = after_h

# csv 파일 생성하기
f = open(r"C:\Users\toyou\OneDrive\바탕 화면\vsc\크롤링\data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)


# 상품 정보 div
items = browser.find_elements_by_css_selector('.basicList_info_area__17Xyo')
for item in items:
    name = item.find_element_by_css_selector('.basicList_title__3P9Q7').text
    try:
        price = item.find_element_by_css_selector('.basicList_price_area__1UXXR').text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector('.basicList_title__3P9Q7 > a').get_attribute('href')

    print(name,price,link)
    
    #데이터 쓰기
    csvWriter.writerow([name, price, link])


# 파일 닫기
f.close()
