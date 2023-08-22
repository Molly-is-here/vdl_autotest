import os
from elements.public_control import control
from common.Airtest_method import airtest_method 
from pywinauto import Application


class open_Software():
    os.chdir(r"D:\ly\00_VDL\0809_0.4.8.2\中文測試testダイフク0818\ViMo-Deeplearning")

    '''打开软件'''
    def open_sofeware(app_path):
        app = Application().start(app_path)
        # start_app(app_path)
        airtest_method.operate_sleep(5.0)

    '''连接当前设备'''
    def connect_sofeware(url):
        airtest_method.connect_app(url)
        #airtest_method.operate_sleep(3.0)
        #将当前窗口截图
        airtest_method.screenshot("当前窗口截图.png")

    '''点击窗口最大化'''
    def click_maximize():
        airtest_method.assert_method(control.max_screen,"最大化按钮打开失败")
        airtest_method.touch_button(control.max_screen)        
       
    
