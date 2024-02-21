from elements.public_control import control
from common.Airtest_method import airtest_method
import os
from airtest.core.api import *

class data():
     
    def finish_button():
        '''点击完成''' 
        airtest_method.touch_button(control.upload_done)
   
    def add_file(file_path):
        '''导入文件夹'''   
        if not airtest_method.check_exit(control.add_file,'FALSE') :
            assert False,'找不到添加文件夹按钮'
        else:
            airtest_method.touch_button(control.add_file)
        airtest_method.operate_sleep() 
        if not airtest_method.check_exit(control.choice_file,'FALSE') :
            assert False,'选择文件夹按钮'
        else:
            airtest_method.touch_button(control.choice_file)            
        airtest_method.input_text(file_path)
        airtest_method.key_event('{ENTER}')
        # airtest_method.touch_button(control.jump_click)
        airtest_method.key_event('{ENTER}')
        # airtest_method.touch_button(control.choice_button)

        if not airtest_method.check_exit(control.upload_label,'FALSE') :
            assert False,'找不到导入完成标志'
        else:
            airtest_method.touch_button(control.upload_done)

    def add_image(file_path):   
        '''导入图像'''
        if not airtest_method.check_exit(control.add_image,'FALSE') :
            assert False,'找不到添加图像按钮'
        else:
            airtest_method.touch_button(control.add_image)
        airtest_method.touch_button(control.choice_file)   
        airtest_method.input_text(file_path)
        airtest_method.key_event('{ENTER}')
        # airtest_method.touch_button(control.jump_click)
        airtest_method.touch_button(control.click_area)
        '''全选图片'''
        airtest_method.key_event("^a")
        airtest_method.touch_button(control.ok_button)
        if not airtest_method.check_exit(control.upload_label,'FALSE') :
            assert False,'找不到导入完成标志'
        else:
            airtest_method.touch_button(control.upload_done)

    def add_label(file_path):
        '''导入标注'''   
        if not airtest_method.check_exit(control.add_label,'FALSE',5) :
            assert False,'找不到添加标注按钮'
        else:
            airtest_method.touch_button(control.add_label)
        airtest_method.touch_button(control.choice_file) 
        airtest_method.input_text(file_path)
        airtest_method.key_event('{ENTER}')
        # airtest_method.touch_button(control.jump_click)
        airtest_method.touch_button(control.click_area)
        '''全选标注'''
        airtest_method.key_event("^a")
        airtest_method.touch_button(control.ok_button)

        if not airtest_method.check_exit(control.upload_label,'FALSE') :
            assert False,'找不到导入完成标志'
        else:
            airtest_method.touch_button(control.upload_done)

    def project_flow():
        '''点击方案流程'''
        if not airtest_method.check_exit(control.project_flow,'FALSE',5) :
            assert False,'找不到方案流程按钮'
        else:
            airtest_method.touch_button(control.project_flow)

    def add_dataset():
        '''添加数据源'''
        if not airtest_method.check_exit(control.add_dataset,'FALSE',5) :
            assert False,'数据源添加失败'
        else:
            airtest_method.touch_button(control.add_dataset)

    def add_pre_module(element):
        '''添加后置模块'''
        data.add_dataset()
        if not airtest_method.check_exit(element,'FALSE',5) :
            assert False,'未找到前置模块'
        else:
            airtest_method.touch_button(element)

    def add_post_module(element):
        '''添加后置模块'''
        airtest_method.touch_button(control.pre_module)  #点击前置模块的‘+’符号新增模块
        if not airtest_method.check_exit(element,'FALSE',5) :
            assert False,'未找到后置模块'
        else:
            airtest_method.touch_button(element)
        airtest_method.operate_sleep()

    def dataset_management():
        '''数据源管理页面'''
        airtest_method.operate_sleep(2.0)
        data.project_flow()
        airtest_method.touch_button(control.dataset_module)
        data.project_flow()
        
        
    