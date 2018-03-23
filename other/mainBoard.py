# -*- coding: utf-8 -*-
from tkinter import *
from other.NextDayOverTime import PythonOrgSearch as job
import time
import os
import tkinter.messagebox as MG
try:
    from ttk import Entry, Button
except ImportError:
    pass
class Login(object):
        def __init__(self):
            self.root = Tk()
            self.root.title(u'用户登录')
            self.root.resizable(False, False)
            self.root.geometry('+600+500')
            self.lb_user = Label(self.root, text=u'用户名：', padx=5)
            self.lb_passwd = Label(self.root, text=u'密码：', padx=5)

            self.lb_stime = Label(self.root, text=u'日期: ', padx=5)
            self.lb_sexmp = Label(self.root, text=u'      （输入格式01，02，03）', padx=5)
            self.lb_mytext = Label(self.root, text=u'原因: ', padx=5)
            self.lb_user.grid(row=0, column=0, sticky=W)
            self.lb_passwd.grid(row=1, column=0, sticky=W)
            self.lb_stime.grid(row=2, column=0, sticky=W)
            self.lb_sexmp.grid(row=3, column=0, sticky=W)
            self.lb_mytext.grid(row=4, column=0, sticky=W)

            self.en_user = Entry(self.root, width=20)
            self.en_passwd = Entry(self.root, width=20)
            self.en_stime = Entry(self.root, width=20)
            self.en_reson = Entry(self.root, width=20)
            self.en_user.grid(row=0, column=1, columnspan=1)
            self.en_passwd.grid(row=1, column=1, columnspan=1)
            self.en_stime.grid(row=2, column=1, columnspan=1)
            self.en_reson.grid(row=4, column=1, columnspan=1, rowspan=3)

            self.var = IntVar()
            self.ckb = Checkbutton(self.root, text=u'记住用户名和密码', underline=0,
                                   variable=self.var)
            self.ckb.grid(row=9, column=0)
            self.bt_print = Button(self.root, text=u'确定', width=20)
            self.bt_print.grid(row=9, column=1, sticky=E, pady=5)
            self.bt_print.config(command=self.print_info)
            self.checkconf()
            self.root.mainloop()


            def validate_func(self, en):
                return False if eval(en).get().strip() != '' else True

        def print_info(self):
            en1_value = self.en_user.get().strip()
            en2_value = self.en_passwd.get().strip()
            en3_value = self.en_stime.get().strip()
            nowtime = time.strftime('%Y-%m-',time.localtime(time.time()))
            real_en3_value=nowtime+en3_value+" 18:00"
            real_en4_value=nowtime+en3_value+" 20:00"
            en4_value = self.en_stime.get().strip()
            en5_value = self.en_reson.get().strip()
            print(real_en3_value,real_en4_value)
            isok=job.test_search_in_python_org(en1_value,en2_value,real_en3_value,real_en4_value,en5_value)
            #isok="ture"

            if isok=="ture":
                MG.showinfo(title="完成", message="已保存至待发事项，请注意及时发送")
                sys.exit(0)
            else:
                MG.showerror(title="失败", message="失败 可以再尝试下，或者放弃")

                #print(isok)
        def checkconf(self):
            if os.path.exists("local.conf") and os.path.getsize("local.conf")!= 0:
                list = []
                with open('local.conf', 'r') as f:
                    for line in f.readlines():
                        list.append(line.strip())
                        print(line.strip())
                self.en_user.insert(0, list[0])
                self.en_passwd.insert(0, list[1])
                self.en_stime.insert(0, u'01')
                self.en_reson.insert(0, list[2])
            else:
                self.en_user.insert(0, u'input you name')
                self.en_passwd.insert(0, u'input you password')
                self.en_stime.insert(0, u'01')
                self.en_reson.insert(0, u'值班')



if __name__ == "__main__":
    Login()
