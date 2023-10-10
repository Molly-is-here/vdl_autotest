from elements.public_control import control
import os
from common.Airtest_method import airtest_method 
from pages.data_page import data

class infering():
    '''切换至模型推理页面'''
    def model_infering():
        if not airtest_method.check_exit(control.model_infering,'FALSE') :
            assert False,'找不到模型推理tab按钮'
        else:
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
        
    '''解锁推理按钮'''    
    def unlock_infering():
        if not airtest_method.check_exit(control.unlock_logo,'FALSE'):      
            assert False,'找不到解锁按钮'
        else:         
            airtest_method.touch_button(control.unlock_logo)

    '''模式选择'''
    def infering_pattern_choice():
        if not airtest_method.check_exit(control.pattern_choice,'FALSE'):      
            assert False,'找不到模式选择按钮'
        else:         
            airtest_method.touch_button(control.pattern_choice)

    '''选择TRT模式'''
    def infering_pattern_TRT():
        if not airtest_method.check_exit(control.pattern_TRT,'FALSE'):      
            assert False,'找不到TRT模式'
        else:         
            airtest_method.touch_button(control.pattern_TRT)
    
    '''设备类型'''
    def infering_device_type():
        if not airtest_method.check_exit(control.device_type,'FALSE'):      
            assert False,'找不到设备类型按钮'
        else:         
            airtest_method.touch_button(control.device_type)

    '''选择CPU设备'''
    def infering_device_CPU():
        if not airtest_method.check_exit(control.device_CPU,'FALSE'):      
            assert False,'找不到CPU设备'
        else:         
            airtest_method.touch_button(control.device_CPU)



