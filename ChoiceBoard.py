# -*- coding: utf-8 -*-
from tkinter import *
from AutoPerformance import Perform as runwork
import time
import calendar
from datetime import datetime
import os
import tkinter.messagebox as MG
import openpyxl
try:
    from ttk import Entry, Button
except ImportError:
    pass
class Login(object):
        def __init__(self):
            self.root = Tk()
            self.root.title(u'用户登录')
            self.root.resizable(False, False)
            self.root.geometry('350x530+700+300')

            self.xmlpath = StringVar()
            dict=self.checkconf()
            dict['xml_path'] = str(self.checkxml())
            self.lb_user = Label(self.root, text=u'用户名：', padx=5)
            self.lb_passwd = Label(self.root, text=u'密码：', padx=5)
            self.checkDep_lab = Label(self.root, text=u'所属部门：', padx=5)
            self.checkRo_lab = Label(self.root, text=u'角色选择：', padx=5)
            self.check_lab1 = Label(self.root, text=u' ', padx=1)
            self.check_lab2 = Label(self.root, text=u'', padx=1)

            self.deptset = StringVar()
            self.deptset.set(dict.get('[dept]'))
            self.roalset = StringVar()
            self.roalset.set(dict.get('[role]'))

            self.checkfrom1 =Radiobutton(self.root,text="项目",variable=self.deptset,value="1")
            self.checkfrom2 =Radiobutton(self.root,text="研发",variable=self.deptset,value="2")
            self.checkfrom3 =Radiobutton(self.root,text="运维",variable=self.deptset,value="3")

            self.checkroal1 =Radiobutton(self.root,text="JAVA工程师",variable=self.roalset,value="1")
            self.checkroal2 =Radiobutton(self.root,text="UI设计师",variable=self.roalset,value="2")
            self.checkroal3 =Radiobutton(self.root,text="IOS工程师",variable=self.roalset,value="3")
            self.checkroal4 =Radiobutton(self.root,text="Andrior工程师",variable=self.roalset,value="4")
            self.checkroal5 =Radiobutton(self.root,text="测试工程师",variable=self.roalset,value="5")
            self.checkroal6 =Radiobutton(self.root,text="WEB前端",variable=self.roalset,value="6")
            self.checkroal7 =Radiobutton(self.root,text="JAVA设计师",variable=self.roalset,value="7")
            self.checkroal8 =Radiobutton(self.root,text="产品专员",variable=self.roalset,value="8")
            self.checkroal9 =Radiobutton(self.root,text="综合管理员",variable=self.roalset,value="9")
            self.checkroal0 =Radiobutton(self.root,text="技术总监",variable=self.roalset,value="0")


            self.lb_user.grid(row=0, column=0, sticky=W)
            self.lb_passwd.grid(row=1, column=0, sticky=W)

            self.checkDep_lab.grid(row=2, column=0, sticky=W)

            self.checkfrom1.grid(row=2, column=1, sticky=W)
            self.checkfrom2.grid(row=3, column=1, sticky=W)
            self.checkfrom3.grid(row=4, column=1, sticky=W)

            self.checkRo_lab.grid(row=5, column=0, sticky=W)

            self.checkroal1.grid(row=6, column=1, sticky=W)
            self.checkroal2.grid(row=7, column=1, sticky=W)
            self.checkroal3.grid(row=8, column=1, sticky=W)
            self.checkroal4.grid(row=9, column=1, sticky=W)
            self.checkroal5.grid(row=10, column=1, sticky=W)
            self.checkroal6.grid(row=11, column=1, sticky=W)
            self.checkroal7.grid(row=12, column=1, sticky=W)
            self.checkroal8.grid(row=13, column=1, sticky=W)
            self.checkroal9.grid(row=14, column=1, sticky=W)
            self.checkroal0.grid(row=15, column=1, sticky=W)


            self.en_user = Entry(self.root, width=20)
            self.en_passwd = Entry(self.root, width=20,show='*')
            self.en_user.insert(0,dict.get('[ID]'))
            self.en_passwd.insert(0,dict.get('[code]'))

            self.check_lab1['text']=' 已获取： '
            self.check_lab2['text']=dict.get('xml_path')
            self.en_user.grid(row=0, column=1, columnspan=1)
            self.en_passwd.grid(row=1, column=1, columnspan=1)
            self.check_lab1.grid(row=20)
            self.check_lab2.grid(row=21)

            self.var = IntVar()
            self.ckb = Checkbutton(self.root, text=u'记住用户名和密码以及设置', underline=0,
                                   variable=self.var)
            self.ckb.grid(row=18, column=0)

            self.bt_print = Button(self.root, text=u'确定', width=20)
            self.bt_print.grid(row=19, column=1, sticky=E, pady=5)
            self.bt_print.config(command=self.print_info)

            self.root.mainloop()


            def validate_func(self, en):
                return False if eval(en).get().strip() != '' else True


            def checkfromclick1(self):

                return list


        def print_info(self):
            if self.var.get()!=0:
                print(self.var.get())
                self.saveconf()

            sendmes = {}
            # 268599543846224672-anchor 项目
            # 6377311728366403805-anchor 研发
            # 4218208322934425649-anchor 运维
            sendmes['xml_path']=self.check_lab2['text']

            if self.deptset.get()=='1':
                sendmes['send_dept']='268599543846224672-anchor'
            elif self.deptset.get()=='2':
                sendmes['send_dept'] = '6377311728366403805-anchor'
            else:
                sendmes['send_dept'] = '4218208322934425649-anchor'
            sendmes['send_role']=self.roalset.get()
            sendmes['en_user']=self.en_user.get().strip()
            sendmes['en_passwd']=self.en_passwd.get().strip()
            sendmes['lastday']=time.strftime('%Y-%m', time.localtime(time.time()))+'-'\
                               +str(calendar.monthrange(datetime.now().year,datetime.now().month)[1])\
                               +' 17:30'
            sendmes['xml_lastday']=time.strftime('%m', time.localtime(time.time()))+'月'\
                               +str(calendar.monthrange(datetime.now().year,datetime.now().month)[1])+'日'
            #isok=runwork.test(sendmes)
            isok=runwork.doLoginSession(sendmes)
            #isok="ture"

            if isok=="ture":
                MG.showinfo(title="完成", message="已保存至待发事项，请注意及时发送")
                sys.exit(0)
            else:
                MG.showerror(title="失败", message="失败 可以再尝试下，或者放弃")

        def saveconf(self):
            f = open("local.conf", 'r')  # 以读方式打开文件
            result = list()
            for line in f.readlines():  # 依次读取每行
                line = line.strip()  # 去掉每行头尾空白
                if line.strip().find("=") and '[ID]' in line.strip():
                    result.append(line.strip().split("=")[0]+'='+self.en_user.get())
                if line.strip().find("=") and '[code]' in line.strip():
                    result.append(line.strip().split("=")[0]+'='+self.en_passwd.get())
                if line.strip().find("=") and '[dept]' in line.strip():
                    result.append(line.strip().split("=")[0] + '=' + self.deptset.get())
                if line.strip().find("=") and '[role]' in line.strip():
                    result.append(line.strip().split("=")[0] + '=' + self.roalset.get())
                if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
                    continue  # 是的话，跳过不处理
            print(result)
            f.close() # 关闭文件
            with open('local.conf', 'w') as fw:  # with方式不需要再进行close
                fw.write('%s' % '\n'.join(result))


        def checkconf(self):

            if os.path.exists("local.conf") and os.path.getsize("local.conf")!= 0:
                dict = {}
                with open('local.conf', 'r') as f:
                     for line in f.readlines():
                         if line.strip().find("="):
                            dict[line.strip().split("=")[0]]=line.strip().split("=")[1]
                         #print(line.strip())
                print('读取配置文件：')
                print(dict)
                return dict

            else:
                dictDefault ={'[ID]': '输入用户名', '[code]': '密码', '[dept]': '1', '[role]': '1'}
                return dictDefault

        def checkxml(self):
            xmlpath=time.strftime('%Y-%m', time.localtime(time.time()))+'月份绩效填写用表.xlsx'
            print(xmlpath)
            if os.path.exists(xmlpath):
                return xmlpath
            else:
                MG.showerror(title="失败", message="不存在"+xmlpath+"文件,停止进程")
                sys.exit(0)
                return '-1'
if __name__ == "__main__":
    Login()
