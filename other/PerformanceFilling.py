# # coding=utf-8
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import TimeoutException
# import time
#
#
#
# class performanceMa():
#
#     def toFill():
#         driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
#         # print("wait install ")
#         driver.implicitly_wait(3)
#         driver.get("http://113.231.68.122/seeyon/index.jsp")
#         elemuser = driver.find_element_by_id("login_username")
#         #elemuser.send_keys(username)
#         elempswd = driver.find_element_by_id("login_password")
#         #elempswd.send_keys(userpasswd)
#         elempswd.send_keys(Keys.RETURN)
#         driver.execute_async_script("ja
#
# '''javascript:getCtpTop().openCtpWindow({'url':'/seeyon/collaboration/collaboration.do?method=newColl&templateId=-6727894578816138688'});'''