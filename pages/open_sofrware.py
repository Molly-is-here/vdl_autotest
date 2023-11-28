import os
from elements.public_control import control
from common.Airtest_method import airtest_method 
from pywinauto import Application


class open_Software():
    os.chdir(r"D:\ViMo-Deeplearning")

    
    def open_sofeware(app_path):
        '''打开软件'''
        app = Application().start(app_path)
        # start_app(app_path)
        airtest_method.operate_sleep(10.0)

    
    def connect_sofeware(url):
        '''连接当前设备'''
        airtest_method.connect_app(url)
        airtest_method.operate_sleep(5.0)
        #将当前窗口截图
        airtest_method.screenshot("当前窗口截图.png")
   
    def click_maximize():
        '''点击窗口最大化'''
        airtest_method.assert_method(control.max_screen,"最大化按钮打开失败")
        airtest_method.touch_button(control.max_screen)        
       
    
