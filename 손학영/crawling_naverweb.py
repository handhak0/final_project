from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver.exe')

#  웹 자원 로드 위해 3초 기다리기
driver.implicitly_wait(3)

# 특정 url 열기
driver.get("https://novel.naver.com/webnovel/genre?genre=101&order=Update&finish=true")
time.sleep(3)
# 팝업창 닫기
popup =  driver.find_element_by_class_name("lk_finish")
popup.click()

# 작품 하나씩 들어가기
driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[1]/a').click()

# 표지 이미지 저장하기
image = driver.find_element_by_css_selector("pic NPI=a:illust")
img_url = image.get_attribute("src")



from urllib.request import urlretrieve
urlretrieve(img_url, "./face/" )

driver.quit()