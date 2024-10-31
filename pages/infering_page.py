import os
from common.Airtest_method import airtest_method 
from elements.public_control import light_control,get_button_from_string

class infering():
    
    def model_infering(color):
        '''切换至模型推理页面
        color light:浅色主题 dark:深色主题
        '''
        model_infering_element = get_button_from_string(f"{color}_control.model_infering")
        if not airtest_method.check_exit(model_infering_element,'FALSE') :
            assert False,'找不到模型推理tab按钮'
        else:
            airtest_method.touch_button(model_infering_element)
     
    def images_input(dataset,file,color):
        '''导入文件夹
        color light:浅色主题 dark:深色主题
        '''
        #导入图片
        images_input_element = get_button_from_string(f"{color}_control.images_input")
        #导入完成标志
        upload_label = get_button_from_string(f"{color}_control.upload_label")
        #完成按钮
        upload_done = get_button_from_string(f"{color}_control.upload_done")
              
        airtest_method.touch_button(images_input_element)
        file_path = os.path.join(dataset,file)
        if not airtest_method.check_exit(light_control.choice_file,'FALSE') :
            assert False,'选择文件夹按钮'
        else:
            airtest_method.touch_button(light_control.choice_file)   
        airtest_method.input_text(file_path)
        airtest_method.key_event('{ENTER}')   
        airtest_method.touch_button(light_control.click_area)
        airtest_method.key_event("^a")
        airtest_method.key_event('{ENTER}')
        if not airtest_method.check_exit(upload_label,'FALSE',3600) :          
            assert False,'找不到导入完成标志'
        else:
            airtest_method.operate_sleep()
            airtest_method.touch_button(upload_done)
      
    def begin_infering(color):
        '''开始推理
        color light:浅色主题 dark:深色主题
        '''
        #开始推理
        begin_infering_element = get_button_from_string(f"{color}_control.begin_infering")
        if not airtest_method.check_exit(begin_infering_element,'FALSE',10):      
            assert False,'找不到推理按钮'
        else:         
            airtest_method.touch_button(begin_infering_element)

    def return_infering():
        '''重新推理'''
        if not airtest_method.check_exit(light_control.return_infering,'FALSE',10):      
            assert False,'找不到重新推理按钮'
        else:         
            airtest_method.touch_button(light_control.return_infering)
       
    def review_infering(color):
        '''判断推理完成
        color light:浅色主题 dark:深色主题
        '''
        infering_finished = get_button_from_string(f"{color}_control.infering_finished")    
        airtest_method.operate_sleep()
        if not airtest_method.check_exit(infering_finished,'FALSE',36000) :
            assert False,'推理未完成'
    def unlock_infering():
        '''解锁推理按钮'''  
        if not airtest_method.check_exit(light_control.unlock_logo,'FALSE'):      
            assert False,'找不到解锁按钮'
        else:         
            airtest_method.touch_button(light_control.unlock_logo)
   
    def infering_pattern_choice():
        '''模式选择'''
        if not airtest_method.check_exit(light_control.pattern_choice,'FALSE'):      
            assert False,'找不到模式选择按钮'
        else:         
            airtest_method.touch_button(light_control.pattern_choice)
 
    def infering_FP32_TRT():
        '''选择TRT-FP32模式'''
        if not airtest_method.check_exit(light_control.FP32_TRT,'FALSE'):      
            assert False,'找不到TRT-FP32模式'
        else:         
            airtest_method.touch_button(light_control.FP32_TRT)

    def infering_FP16_TRT():
        '''选择TRT-FP16模式'''
        if not airtest_method.check_exit(light_control.FP16_TRT,'FALSE'):      
            assert False,'找不到TRT-FP16模式'
        else:         
            airtest_method.touch_button(light_control.FP16_TRT)
     
    def infering_device_type():
        '''设备类型'''
        if not airtest_method.check_exit(light_control.device_type,'FALSE'):      
            assert False,'找不到设备类型按钮'
        else:         
            airtest_method.touch_button(light_control.device_type)
 
    def infering_device_CPU():
        '''选择CPU设备'''
        if not airtest_method.check_exit(light_control.device_CPU,'FALSE'):      
            assert False,'找不到CPU设备'
        else:         
            airtest_method.touch_button(light_control.device_CPU)
            airtest_method.operate_sleep(2.0)
            airtest_method.touch_button(light_control.images_input)

    def batch_infering(batch):
        '''批量推理'''
        if not airtest_method.check_exit(light_control.batch_infering,'FALSE'):      
            assert False,'找不到批量推理编辑框'
        else:         
            airtest_method.touch_button(light_control.batch_infering)
            airtest_method.key_event("{BACKSPACE}")
            airtest_method.input_text(f'{batch}')




