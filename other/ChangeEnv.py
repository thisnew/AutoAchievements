import os
from tkinter import *

print(os.environ["JAVA_HOME"])
print(os.environ["path"])


class ChangeBoard(object):
    def __init__(self):
        self.root = Tk()
        self.root.title(u'用户登录')
        self.root.resizable(False, False)
        self.root.geometry('350x530+700+300')


# mydir= "c:\\mydir"
# os.environ["MYDIR"] = mydir
# print(os.environ["MYDIR"])
#
# pathV = os.environ["PATH"]
# print(pathV)
# os.environ["PATH"]= mydir + ";" + os.environ["PATH"]
# print(os.environ["PATH"])