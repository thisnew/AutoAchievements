# -*- coding: utf-8 -*-

# 单个环境只支持双向选配置
#   配置一名称 = 【路径】
#   配置二名称 = 【路径】
from PyQt5.QtWidgets import QDialog
from RechargeEnv import Ui_change
import os
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import configparser

rd = configparser.ConfigParser()  # 调用配置操作句柄
rd.read('WinOS_Env.ini')


class Login(QDialog):

    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        self.ui = Ui_change()
        self.ui.setupUi(self)
        try:
            java_path='未设置'
            python_path='未设置'
            java_path=os.environ["JAVA_HOME"]
            python_path=os.environ["PYTHON_HOME"]
            java_choice_name1=rd.items('java')[0][0]
            java_choice_name2=rd.items('java')[1][0]
            java_choice_path1=rd.items('java')[0][1]
            java_choice_path2=rd.items('java')[1][1]

            py_choice_name1=rd.items('python')[0][0]
            py_choice_name2=rd.items('python')[1][0]
            py_choice_path1=rd.items('python')[0][1]
            py_choice_path2=rd.items('python')[1][1]
        except Exception as e:
            pass
        self.ui.radioButton_java_1.setText(java_choice_name1)
        self.ui.radioButton_java_2.setText(java_choice_name2)
        self.ui.radioButton_python_1.setText(py_choice_name1)
        self.ui.radioButton_python_2.setText(py_choice_name2)

        self.ui.java_path_show.setText(java_path)
        self.ui.python_path_shw.setText(python_path)
        # # 连接槽函数登录按钮
        self.ui.java_pushButton.clicked.connect(self.env_set)
        # # 连接槽函数退出按钮
        self.ui.python_pushButton_3.clicked.connect(self.env_set)
        # # 连接槽函数退出按钮
        # self.ui.pushButton_3.clicked.connect(self.slotCancle)
        #C:\java\Python\Python36
    def env_set(self):
        if self.ui.radioButton_java_1.isChecked():
            os.environ['PYTHON_HOME']=rd.items('java')[0][1]
            print(os.environ['PYTHON_HOME'])
            os.system('''wmic ENVIRONMENT where "name='JAVA_HOME'" delete''')
            #os.popen('''wmic ENVIRONMENT where "name='JAVA_HOME'" delete''')
        elif self.ui.radioButton_java_2.isChecked():
            print('2222')
        else:
            print("a")
        # jjj=rd.items('java')
        # print(jjj)
        # print(jjj[0][0])

        #self.ui.java_path_show.setText(path)

        # def env_set(self):
        #
        #     print(os.environ["JAVA_HOME"])
        #
        #     print(os.environ["path"])






if __name__ == '__main__':
        app = QApplication(sys.argv)
        login =Login()
        login.setWindowTitle("环境变量设置")

        if login.exec():
            print("登录成功")
        else:
            print("登录退出")
            sys.exit()