from elements.public_control import control
#from airtest.core.api import *
from common.Airtest_method import airtest_method 

class mark():
    '''切换至图像标注'''
    def image_label():
        airtest_method.touch_button(control.image_label)
        airtest_method.operate_sleep()

    '''自动划分'''
    def auto_divide():
        airtest_method.touch_button(control.auto_divide)
        airtest_method.operate_sleep()
