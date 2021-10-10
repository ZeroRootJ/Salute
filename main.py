from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def sendmail(name, title, contents):

    soldier_name = "이진규"
    birthYear = "2001"
    birthMonth = "11"
    birthDay = "28"

    addr = '둔산북로 215'
    addr_spec = '8동 404'

    rel = '친구'
    pwd = '1234'

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("disable-gpu")
    driver_path = '/Users/yk/PycharmProjects/IPbot/chromedriver'
    driver_path = '/home/ubuntu/base/Salute/chromedriver'
    driver = webdriver.Chrome(driver_path, options=options)

    print("webdriver initialized")

    # ROKAF main
    driver.get('https://www.google.com/search?q=%EA%B8%B0%EB%B3%B8%EA%B5%B0%EC%82%AC%ED%9B%88%EB%A0%A8%EB%8B%A8&newwindow=1&sxsrf=AOaemvJrncjSP0NasmiAriUSfFMQMjvVIQ%3A1633863640083&ei=2MdiYZy_BM-U-Abu0Qo&ved=0ahUKEwici4Ov2L_zAhVPCt4KHe6oAgAQ4dUDCA4&uact=5&oq=%EA%B8%B0%EB%B3%B8%EA%B5%B0%EC%82%AC%ED%9B%88%EB%A0%A8%EB%8B%A8&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjoECCMQJzoICAAQgAQQsQM6CwgAEIAEELEDEIMBOgcIIxDqAhAnOgoIABCABBCHAhAUOgQIABBDSgQIQRgAUJp1WOyKAWCgjAFoBHAAeAKAAYoCiAGnF5IBBjAuMTguMZgBAKABAbABCsABAQ&sclient=gws-wiz')
    driver.implicitly_wait(10)

    driver.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/a/h3').click()
    driver.implicitly_wait(10)

    driver.switch_to.window(driver.window_handles[1])
    # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/a[3]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[3]/a[3]'))).click()

    # driver.find_element_by_css_selector('#popupWrap > div:nth-child(3) > a:nth-child(5)').click()


    driver.find_element_by_name('searchName').send_keys(soldier_name)
    print("ROKAF main2")
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[2]/table/tbody/tr[2]/td[2]/input[1]').send_keys(birthYear)
    print("ROKAF main3")
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[2]/table/tbody/tr[2]/td[2]/input[2]').send_keys(birthMonth)
    print("ROKAF main4")
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[2]/table/tbody/tr[2]/td[2]/input[3]').send_keys(birthDay)
    print("ROKAF main5")
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[3]/span/input').click()

    print("ROKAF main complete")

    # Pop up
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element_by_xpath('/html/body/div/ul/li/input').click()

    print("pop up")

    # Submit
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[3]/span/input').click()

    # Submit
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[1]/div/div[3]/span/input').click()

    # Input Address
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[1]/table/tbody/tr[3]/td/div[1]/span/input').click()
    driver.switch_to.window(driver.window_handles[2])
    # driver.find_element_by_xpath('/html/body/div/div[2]/button[2]').click() # warning discard
    driver.find_element_by_xpath('/html/body/form[2]/div/div[1]/div/div[1]/fieldset/span/input[1]').send_keys(addr)
    driver.find_element_by_xpath('/html/body/form[2]/div/div[1]/div/div[1]/fieldset/span/input[2]').click()
    driver.find_element_by_xpath('/html/body/form[2]/div/div[1]/div/div[2]/table/tbody/tr/td[2]/a/div/span[2]').click()
    driver.find_element_by_xpath('/html/body/form[2]/div/div[1]/div/div[3]/table/tbody/tr[2]/td/input').send_keys(addr_spec)
    driver.find_element_by_xpath('/html/body/form[2]/div/div[1]/div/div[3]/div/a').click()

    print("address")

    # Switch to main
    driver.switch_to.window(driver.window_handles[1])

    # Name
    driver.find_element_by_id('senderName').send_keys(name)
    # Relation
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[1]/table/tbody/tr[5]/td/input').send_keys(rel)
    # Title
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[1]/table/tbody/tr[6]/td/input').send_keys(title)
    # Contents
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[1]/table/tbody/tr[7]/td/textarea').send_keys(contents)
    # Pwd
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[1]/table/tbody/tr[8]/td/input').send_keys(pwd)

    # Submit
    # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/form/div[2]/span[1]/input').click()

    driver.quit()


if __name__ == '__main__':
    print(sendmail('홍길동', '인편인편', "인편인편인편"))















