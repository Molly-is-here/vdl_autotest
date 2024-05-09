from elements.public_control import control
import os
from common.Airtest_method import airtest_method 
from pages.data_page import data

class infering():
    
    def model_infering():
        '''切换至模型推理页面'''
        if not airtest_method.check_exit(control.model_infering,'FALSE') :
            assert False,'找不到模型推理tab按钮'
        else:
            airtest_method.touch_button(control.model_infering)
     
    def images_input(dataset,file):
        '''导入文件夹'''
        airtest_method.touch_button(control.images_input)
        file_path = os.path.join(dataset,file)
        if not airtest_method.check_exit(control.choice_file,'FALSE') :
            assert False,'选择文件夹按钮'
        else:
            airtest_method.touch_button(control.choice_file)   
        airtest_method.input_text(file_path)
        airtest_method.key_event('{ENTER}')
        # airtest_method.touch_button(control.jump_click)       
        airtest_method.touch_button(control.click_area)
        airtest_method.key_event("^a")
        airtest_method.key_event('{ENTER}')
        if not airtest_method.check_exit(control.upload_label,'FALSE',3600) :          
            assert False,'找不到导入完成标志'
        else:
            airtest_method.operate_sleep()
            airtest_method.touch_button(control.file_upload)
      
    def begin_infering():
        '''开始推理'''
        if not airtest_method.check_exit(control.begin_infering,'FALSE',10):      
            assert False,'找不到重新推理按钮'
        else:         
            airtest_method.touch_button(control.begin_infering)

    def return_infering():
        '''重新推理'''
        if not airtest_method.check_exit(control.return_infering,'FALSE',10):      
            assert False,'找不到重新推理按钮'
        else:         
            airtest_method.touch_button(control.return_infering)

        
    def review_infering():
        '''判断推理完成'''
        if not airtest_method.check_exit(control.infering_finished,'FALSE',36000) :
            assert False,'推理未完成'
        else:     
            return True
            
    def unlock_infering():
        '''解锁推理按钮'''  
        if not airtest_method.check_exit(control.unlock_logo,'FALSE'):      
            assert False,'找不到解锁按钮'
        else:         
            airtest_method.touch_button(control.unlock_logo)
   
    def infering_pattern_choice():
        '''模式选择'''
        if not airtest_method.check_exit(control.pattern_choice,'FALSE'):      
            assert False,'找不到模式选择按钮'
        else:         
            airtest_method.touch_button(control.pattern_choice)
 
    def infering_FP32_TRT():
        '''选择TRT-FP32模式'''
        if not airtest_method.check_exit(control.FP32_TRT,'FALSE'):      
            assert False,'找不到TRT-FP32模式'
        else:         
            airtest_method.touch_button(control.FP32_TRT)

    def infering_FP16_TRT():
        '''选择TRT-FP16模式'''
        if not airtest_method.check_exit(control.FP16_TRT,'FALSE'):      
            assert False,'找不到TRT-FP16模式'
        else:         
            airtest_method.touch_button(control.FP16_TRT)
     
    def infering_device_type():
        '''设备类型'''
        if not airtest_method.check_exit(control.device_type,'FALSE'):      
            assert False,'找不到设备类型按钮'
        else:         
            airtest_method.touch_button(control.device_type)
 
    def infering_device_CPU():
        '''选择CPU设备'''
        if not airtest_method.check_exit(control.device_CPU,'FALSE'):      
            assert False,'找不到CPU设备'
        else:         
            airtest_method.touch_button(control.device_CPU)
            airtest_method.operate_sleep(2.0)

    def batch_infering(batch):
        '''批量推理'''
        if not airtest_method.check_exit(control.batch_infering,'FALSE'):      
            assert False,'找不到批量推理编辑框'
        else:         
            airtest_method.touch_button(control.batch_infering)
            airtest_method.key_event("{BACKSPACE}")
            airtest_method.input_text(f'{batch}')




