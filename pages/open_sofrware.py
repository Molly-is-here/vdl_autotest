import os
from elements.public_control import light_control
from common.Airtest_method import airtest_method 
from pywinauto import Application


class open_Software():
    
    def open_sofeware(app_path):
        '''打开软件'''
        vdl_path = os.path.join(r"D:\ViMo-Deeplearning", app_path)
        app = Application().start(vdl_path)
        # start_app(app_path)
        airtest_method.operate_sleep(10.0)
 
    def connect_sofeware(url):
        '''连接当前设备'''
        airtest_method.connect_app(url)
        airtest_method.operate_sleep(3.0)
        #将当前窗口截图
        airtest_method.screenshot("当前窗口截图.png")
   
    def click_maximize():
        '''点击窗口最大化'''
        if not airtest_method.check_exit(light_control.max_screen,5):
            return True
        else:
            airtest_method.touch_button(light_control.max_screen)
                  
       
    
