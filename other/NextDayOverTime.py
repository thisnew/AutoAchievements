# coding=utf-8
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import sys

class PythonOrgSearch():

    def test_search_in_python_org(username, userpasswd, StarTime, EndTime, things):
         try:
            driver = webdriver.Chrome(executable_path="bin/chromedriver.exe")
            print("wait install ")
            driver.implicitly_wait(3)
            driver.get("http://113.231.68.122/seeyon/index.jsp")
            elemuser = driver.find_element_by_id("login_username")
            elemuser.send_keys(username)
            elempswd = driver.find_element_by_id("login_password")
            elempswd.send_keys(userpasswd)
            elempswd.send_keys(Keys.RETURN)
            driver.execute_async_script("javascript:getCtpTop().openCtpWindow({'url':'/seeyon/collaboration/collaboration.do?method=newColl&templateId=-2157116420916165977'});")
            print("wait 2 sec")
            time.sleep(2)
         except TimeoutException as t:
            pass
            print("pass the exception")
            print(driver.current_window_handle)
            handles = driver.window_handles
            print(handles)
            for handle in handles:
                if handle != driver.current_window_handle:
                    print('switch to ', handle)
                    driver.switch_to.window(handle)
                    print(driver.current_window_handle)
                    break
                    driver.switch_to_window(handles[1])

            print("page ok")
            getFrame = driver.find_element_by_id("zwIframe")
            driver.switch_to.frame(getFrame)
            print("change iframe")
            elStarTime = driver.find_element_by_id("field0006")
            elStarTime.send_keys(StarTime)
            elEndTime = driver.find_element_by_id("field0007")
            elEndTime.send_keys(EndTime)
            elThins=driver.find_element_by_id("field0003")
            elThins.send_keys(things)
            print("return to main")
            driver.switch_to.default_content()
            print("next do save")
            driver.find_element_by_id("saveDraft_a").click()

            print("以存储至待发")
            driver.quit()
            #driver.close()
            return 'ture'
         except Exception as e:
             #driver.close()
             driver.quit()
             sys.exit()
             return false, e
