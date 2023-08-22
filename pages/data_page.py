from elements.public_control import control
from common.Airtest_method import airtest_method
import os
from airtest.core.api import *

class data():

    '''点击完成'''    
    def finish_button():
        airtest_method.touch_button(control.upload_done)

    '''选择文件夹'''
    def add_file(dataset,file):
        
        airtest_method.touch_button(control.add_file) #点击添加文件夹按钮
        airtest_method.operate_sleep(2.0) 
    
        file_path = os.path.join(dataset,file)
        print(file_path)

        airtest_method.touch_button(control.choice_file)
        airtest_method.operate_sleep()

        airtest_method.input_text(file_path)  #输入文件路径
        airtest_method.touch_button(control.jump_click)   

        airtest_method.operate_sleep(2.0)

        airtest_method.touch_button(control.choice_button) 
        '''导入数据，等待导入完成'''
        if not airtest_method.check_exit(control.upload_label,'FALSE',3600) :          
            assert False,'找不到导入完成标志'
        else:
            airtest_method.operate_sleep()
            data.finish_button()

        #airtest_method.operate_sleep(2.0)
        # #选择相应的文件夹
        # data_file = Template(file_path, threshold=0.7)
        # airtest_method.assert_method(data_file,"数据集文件夹无法选中，请重试")
        # airtest_method.touch_button(data_file)

        # #点击选择文件夹
        # airtest_method.touch_button(control.choice_file)
        # airtest_method.operate_sleep(10.0)

    
    