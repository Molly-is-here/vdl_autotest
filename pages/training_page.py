from elements.public_control import control
from common.Airtest_method import airtest_method 
from airtest.core.api import *

class training():
    '''切换至模型训练页面'''
    def model_training():
        airtest_method.touch_button(control.model_training)
        airtest_method.operate_sleep()

    '''新增小卡片'''
    def add_card():
        airtest_method.touch_button(control.add_card)
        airtest_method.operate_sleep()

    '''将鼠标移动至自定义'''
    def mouse_move():
        airtest_method.touch_button(control.mouse_move)
        airtest_method.operate_sleep()
    
    '''选项为自定义'''
    def zidingyi_button():
        airtest_method.touch_button(control.zidingyi_button)
        airtest_method.operate_sleep()
    
    '''下调benchsize'''
    def cut_benchsize():
        airtest_method.touch_button(control.cut_benchsize,times= 3)
        airtest_method.operate_sleep()

    def set_study():
        airtest_method.touch_button(control.set_study)
        airtest_method.operate_sleep()
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        airtest_method.input_text('3')
        airtest_method.operate_sleep()
    
    '''点击开始训练'''
    def star_training():
        #status = 0
        airtest_method.touch_button(control.star_training)
        airtest_method.operate_sleep()
        #return status
    
    '''点击查看评估'''
    def review_assess():
        if not airtest_method.check_exit(control.review_assess,'FALSE',36000) :
            assert False,'训练未完成'
        else:     
            # airtest_method.touch_button(control.task_finished)               
            # airtest_method.touch_button(control.close_task)
            airtest_method.touch_button(control.model_assess)
            

        