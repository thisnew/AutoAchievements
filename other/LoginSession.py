# coding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time


class LoginWeb():
    def Login_Main_Page(username, userpasswd):
        try:
                driver = webdriver.Chrome(executable_path="bin/chromedriver.exe")
                # print("wait install ")
                driver.implicitly_wait(3)
                driver.get("http://113.231.68.122/seeyon/index.jsp")
                elemuser = driver.find_element_by_id("login_username")
                elemuser.send_keys(username)
                elempswd = driver.find_element_by_id("login_password")
                elempswd.send_keys(userpasswd)
                elempswd.send_keys(Keys.RETURN)
        except TimeoutException as t:
            pass
