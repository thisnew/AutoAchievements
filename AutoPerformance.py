# coding=utf-8
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import os
from openpyxl import load_workbook

class Perform:
   def test(sendmes):
      print(sendmes['en_user'])

      return 'ture'
   def doLoginSession(sendmes):
          try:
               driver = webdriver.Chrome(executable_path="bin/chromedriver.exe")
               print("wait install ")
               driver.implicitly_wait(3)
               driver.get("http://113.231.68.122/seeyon/index.jsp")
               elemuser = driver.find_element_by_id("login_username")
               elemuser.send_keys(sendmes['en_user'])
               elempswd = driver.find_element_by_id("login_password")
               elempswd.send_keys(sendmes['en_passwd'])
               elempswd.send_keys(Keys.RETURN)
               driver.get("http://113.231.68.122/seeyon/collaboration/collaboration.do?method=newColl&templateId=-6727894578816138688")
               #-------中心选择--------------------------------------------------------
               #中心

               setDept=sendmes['send_dept']
               # 部门列表
               # 6377311728366403805-anchor 研发
               # 268599543846224672-anchor 项目
               # 4218208322934425649-anchor 运维
               getFrame = driver.find_element_by_id("zwIframe")
               print('外部')
               print(getFrame)
               driver.switch_to.frame(getFrame)
               datakey=driver.find_element_by_xpath('// *[ @ id = "field0008"]')
               for i in range(20):
                  datakey.send_keys(Keys.BACKSPACE)
               driver.find_element_by_xpath('// *[ @ id = "field0008"]').send_keys(sendmes['lastday'])
               #获取span
               but_spans_cent = driver.find_element_by_xpath('//*[@id="field0002_span"]/span')
               print(but_spans_cent)
               but_spans_cent.click()
               #返回默认
               driver.switch_to.default_content()
               getSelectPeopleFrame = driver.find_element_by_id("SelectPeopleDialog_main_iframe_content")
               print('内部：')
               print(getSelectPeopleFrame)
               driver.switch_to.frame(getSelectPeopleFrame)
               listroot= driver.find_element_by_id("2384162786666955069-anchor")
               ActionChains(driver).double_click(listroot).perform()
               listcent=driver.find_element_by_id("-5904001499047966778-anchor")
               ActionChains(driver).double_click(listcent).perform()
               driver.execute_script("selectOne()")
               #确定动作
               driver.switch_to.default_content()
               done=driver.find_element_by_link_text("确定")
               done.click()
               #---------部门选择-----------------------------------------------------------
               # 部门
               getFrame = driver.find_element_by_id("zwIframe")
               print('外部')
               print(getFrame)
               driver.switch_to.frame(getFrame)
               but_spans_dept = driver.find_element_by_xpath('//*[@id="field0091_span"]/span')
               print(but_spans_dept)
               but_spans_dept.click()
               driver.switch_to.default_content()
               getSelectPeopleFrame = driver.find_element_by_id("SelectPeopleDialog_main_iframe_content")
               print('内部：')
               print(getSelectPeopleFrame)
               driver.switch_to.frame(getSelectPeopleFrame)
               listroot = driver.find_element_by_id(setDept)
               ActionChains(driver).double_click(listroot).perform()
               driver.execute_script("selectOne()")
               # driver.switch_to.active_element
               # 确定动作
               driver.switch_to.default_content()
               done = driver.find_element_by_link_text("确定")
               done.click()
               #_____________________________________________

               getFrame = driver.find_element_by_id("zwIframe")
               print('外部')
               print(getFrame)
               driver.switch_to.frame(getFrame)
               # driver.execute_script("showRelationList(this)")  //*[@id="row-7824964076276987674"]/td[3]/div
               listFrom= driver.find_element_by_xpath('//*[@id="field0056_span"]/span[2]')
               listFrom.click()#打开表单
               print('ok')
               driver.switch_to.default_content()
               getFrame_checkfrom = driver.find_element_by_xpath('//*[contains(@id,"main_iframe_content")]')
               driver.switch_to.frame(getFrame_checkfrom)
                  #//iframe[ends-with(@id,"main_iframe_content")]·
               lenth=0
               indexarry = []
               indexpersent =[]
               #
               filename='Mdict/'+sendmes['send_role']+'.txt'
               print(filename)
               if os.path.exists(filename) and os.path.getsize(filename)!= 0:
                   with open(filename, 'r') as f:
                        for line in f.readlines():
                           indexarry.append(line.strip().split('#')[1])
                           indexpersent.append(line.strip().split('#')[2])
               else:
                  return 'no temp file found'
               #
               print(indexarry)
               print(indexpersent)
               if '7299443944487013551' or '3811026317094570347' in indexarry:
                   driver.find_element_by_xpath('//*[@id = "rpInputChange"]').send_keys(Keys.BACKSPACE)
                   driver.find_element_by_xpath('//*[@id = "rpInputChange"]').send_keys('5')
                   driver.find_element_by_xpath('//*[@id="grid_go"]').click()
               for index in indexarry:
                   mypath= '//*[@id="row'+index+'"]/td[1]/div/input'
                   selectIndex = driver.find_element_by_xpath(mypath)
                   selectIndex.click()

               driver.switch_to.default_content()
               donefrom = driver.find_element_by_link_text("确定")
               donefrom.click()
               #-----------------填写
               getFrame = driver.find_element_by_id("zwIframe")
               print('外部')
               print(getFrame)
               driver.switch_to.frame(getFrame)
               time.sleep(1)
               #填写占比
               block1s= driver.find_elements_by_xpath('//*[@id="field0059_txt"]')
               print(block1s)
               for block in range(len(block1s)):
                     block1s[block].send_keys(indexpersent[block])

               showAdd = driver.find_element_by_xpath('//*[@id="field0065"]')
               showAdd.click()
               myadd = driver.find_element_by_xpath('//*[@id="addEmptyImg"]')
               path=sendmes['xml_path']
               wb = load_workbook(path)

               print(wb.sheetnames)
               sheet = wb.get_sheet_by_name("Sheet1")
               tabRow = sheet.max_row

               print('num:'+str(tabRow))
               for i in range(2,tabRow):
                  myadd.click()
               print("add done")

               for i in range(1 , tabRow):
                     print(i)
                     sheetB=driver.find_element_by_xpath('//*[@id="formson_24252"]/tbody/tr['+str(i)+']/td[2]/div/span/textarea')
                     sheetB.send_keys(sheet['B' + str(i+1)].value)
                     sheetTime=driver.find_element_by_xpath('//*[@id="formson_24252"]/tbody/tr['+str(i)+']/td[3]/div/span/textarea')
                     sheetTime.send_keys(sendmes['xml_lastday'])
                     sheetC=driver.find_element_by_xpath('//*[@id="formson_24252"]/tbody/tr['+str(i)+']/td[4]/div/span/textarea')
                     sheetC.send_keys(sheet['C'+str(i+1)].value)
                     sheetD=driver.find_element_by_xpath('//*[@id="formson_24252"]/tbody/tr['+str(i)+']/td[5]/div/span/input[2]')
                     sheetD.send_keys(sheet['D'+str(i+1)].value)
                     sheetE=driver.find_element_by_xpath('//*[@id="formson_24252"]/tbody/tr['+str(i)+']/td[6]/div/span/textarea')
                     sheetE.send_keys(sheet['E'+str(i+1)].value)
               # time.sleep(1000)
               # time.sleep(200)
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
                print(e)
                driver.quit()
                sys.exit()
                return 'false', e