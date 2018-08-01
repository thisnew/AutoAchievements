
注意事项
    1.xlsx文件必须使用固定样式模板以及文件命名方式
    2.xlsx目前只支持2007之后版本
    3.xlsx必须使用当月日期命名
    4.conf文件默认为GBK编码请勿更改
    5.Mdict/ 下所有文件是关联选项使用的请勿随意更改，除非有选项需要变动



其他参数记录
    JAVA工程师value="1
    UI设计师value="2"
    IOS工程师value="3
    Andrior工程师value=4
    测试工程师value="5"
    WEB前端value="6"
    JAVA设计师value="7
    产品专员value="8"
    综合管理员value="9"
    技术总监value="0"
build命令
    pyinstaller -F -w ChoiceBoard.py


    javac -encoding "utf-8" -Djava.ext.dirs=WebRoot\WEB-INF\lib;D:\Case\apache-tomcat-7.0.82\apache-tomcat-7.0.82\lib; -cp .;WebRoot\WEB-INF\lib; -sourcepath  .;src\  src\com\transfer\service\impl\CapitalServiceImpl.java