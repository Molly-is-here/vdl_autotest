一、安装环境：
1、安装Airtest库：
pip install airtest
*PS:pip版本:23.2.1

2、安装Easyocr依赖：
pip install easyocr

3、安装pytest库：
pip install pytest

4、性能监控依赖：
pip install nvidia-ml-py3
pip install psutil
pip install pandas

5、安装Allure依赖：
pip install allure-pytest

二、文件层级介绍
·common：公共类
·configs:日志设置
·elements：控件元素
·logs：日志存储
·pages：各个页面操作方法
·testcase：测试用例
·tools：其他工具
·run：运行入口
