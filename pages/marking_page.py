from elements.public_control import control
#from airtest.core.api import *
from common.Airtest_method import airtest_method 

class mark():
    
    def image_label():
        '''切换至图像标注'''
        airtest_method.touch_button(control.image_label)
        airtest_method.operate_sleep()
  
    def auto_divide():
        '''自动划分'''
        airtest_method.touch_button(control.auto_divide)
        airtest_method.operate_sleep()

    def import_label(file_path):
        '''串联方案导入标注'''
        if not airtest_method.check_exit(control.import_label,'FALSE') :
                assert False,'未找到导入标注按钮'
        else:
            airtest_method.touch_button(control.import_label)
        airtest_method.touch_button(control.choice_file1) 
        airtest_method.input_text(file_path)
        airtest_method.touch_button(control.jump_click)
        airtest_method.touch_button(control.click_area)
        '''全选'''
        airtest_method.key_event("^a")
        airtest_method.touch_button(control.ok_button)
        if not airtest_method.check_exit(control.upload_label,'FALSE') :
            assert False,'找不到导入完成标志'
        else:
            airtest_method.touch_button(control.upload_done)
