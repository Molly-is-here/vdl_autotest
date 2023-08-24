from elements.public_control import control
import os
from common.Airtest_method import airtest_method 
from pages.data_page import data

class infering():
    '''切换至模型推理页面'''
    def model_infering():
        airtest_method.touch_button(control.model_infering)
    
    '''导入文件夹'''
    def images_input(dataset,file):
        airtest_method.touch_button(control.images_input)
        file_path = os.path.join(dataset,file)
        airtest_method.touch_button(control.choice_file)
        airtest_method.input_text(file_path)
        airtest_method.touch_button(control.jump_click)
        airtest_method.touch_button(control.choice_button)
        if not airtest_method.check_exit(control.upload_label,'FALSE',3600) :          
            assert False,'找不到导入完成标志'
        else:
            airtest_method.operate_sleep()
            airtest_method.touch_button(control.file_upload)
    
    '''开始推理'''
    def begin_infering():
        if not airtest_method.check_exit(control.begin_infering,'FALSE',5):      
            assert False,'找不到开始推理按钮'
        else:         
            airtest_method.touch_button(control.begin_infering)
       

    '''判断推理完成'''
    def review_infering():
        if not airtest_method.check_exit(control.infering_finished,'FALSE',36000) :
            assert False,'推理未完成'
        else:     
            return True



