# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from defaultpassword.defaultpasswd_ui import Ui_GroupBox
from defaultpassword.DBinstall import database
class Login(QDialog):

    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)
        # 连接槽函数登录按钮
        self.ui.pushButton.clicked.connect(self.query_num)
        # 连接槽函数退出按钮
        self.ui.pushButton_2.clicked.connect(self.setdefault)
        # 连接槽函数退出按钮
        self.ui.pushButton_3.clicked.connect(self.slotCancle)
        #todo 实时日志

    def query_num(self):
        if self.ui.lineEdit.text()!='':  #todo 校验
            phone_num=self.ui.lineEdit.text()
            sql="""select realname,password,mobile_number,username,id from user where mobile_number='"""+phone_num+"""' limit 1"""
            db= database()
            res=db.fetch_all(sql)
            print(res)
            for each in res:
                db.getLogger().info(each[0]+' '+each[1]+' '+each[2]+' '+each[3]+' '+each[4])
                self.ui.lineEdit_2.setText(each[0])
                self.ui.lineEdit_3.setText(each[1])
                self.ui.lineEdit_4.setText(each[2])
                self.ui.lineEdit_6.setText(each[3])
            #todo 存储数据



            db_sec= database(dbname='aucu')
            res_sec=db_sec.fetch_all(sql)
            for each in res_sec:
                if each[0]==self.ui.lineEdit_2.text():
                    print('exists')

            db_sec.update()

            #todo 事物按钮
        else:
            print('error num')

    def setdefault(self):




        # if self.ui.lineEditUser.text() != "admin" or self.ui.lineEditPasswd.text() != "123456":
        #     self.ui.labelTips.show()
        #     self.ui.labelTips.setText("用户名或密码错误！")
        # else:
        #     self.accept()
        print('1')

    def slotCancle(self):
        # self.reject()
        print('2')