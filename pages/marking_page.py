from elements.public_control import control
#from airtest.core.api import *
from common.Airtest_method import airtest_method 

class mark():
    
    def image_label(self):
        '''切换至图像标注'''
        airtest_method.touch_button(control.image_label)
        airtest_method.operate_sleep()
  
    def auto_divide(self):
        '''自动划分'''
        airtest_method.touch_button(control.auto_divide)
        airtest_method.operate_sleep()
