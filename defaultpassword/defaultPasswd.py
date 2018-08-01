# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from defaultpassword import defaultPasswd_login as Dui

app = QApplication(sys.argv)
login = Dui.Login()

if login.exec():
    print("登录成功")
else:
    print("登录退出")
    sys.exit(0)





































# from tkinter import *

# class UIBoard(object):
#     def __init__(self):
#         self.root = Tk()
#         self.root.title(u'密码临时修改器')
#         self.root.resizable(False, False)
#         self.root.geometry('350x530+700+300')
#
#         self.inp_query=Entry(self.root,width=20).grid(row=1, column=2)
#
#         self.but_query=Button(self.root,text=u'查询')
#         #self.but_query.config(command=self.saveQuery)
#         self.but_query.grid(row=1, column=3)
#
#
#
#
#
#
#
#         self.root.mainloop()
#
#
# if __name__ == "__main__":
#     UIBoard()

# 读取当前密码

# 存储当前密码 以及备份
    #日志输出


# 更改当前密码到默认


# 读取原密码
# 更改回到原密码

# 查询确认

