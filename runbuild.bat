@echo off
chcp 65001
echo 版本号参数

set /p num1=输入版本1号参数 如：

svn diff --summarize -r%num1% >> diff_%num1%_.list
