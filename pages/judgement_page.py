import os
from common.Airtest_method import airtest_method 
from elements.public_control import control
from pages.data_page import data

class judgement(): 
    def judgement_page():
        '''切换至综合判定页面'''
        data.project_flow()  #点击方案流程按钮
        if not airtest_method.check_exit(control.judgement_page,'FALSE'):
            assert False,'找不到综合判定按钮'
        else:
            airtest_method.touch_button(control.judgement_page)
            data.project_flow()

    def judgement_area():
        '''判定范围'''
        if not airtest_method.check_exit(control.judgement_area,'FALSE'):
            assert False,'找不到判定范围按钮'
        else:
            airtest_method.touch_button(control.judgement_area)
        '''勾选判定范围'''
        if airtest_method.check_exit(control.checkbox):
            airtest_method.touch_button(control.checkbox)  #勾选全部的判定范围
        airtest_method.touch_button(control.save_button)  #若校验无未勾选的范围后点击保存

    def judgement_infering():
        '''开始推理'''
        if not airtest_method.check_exit(control.judgement_infering,'FALSE'):
            assert False,'找不到判定范围按钮'
        else:
            airtest_method.touch_button(control.judgement_infering)

    def judgement_done():
        '''综合判定判定完成'''
        if not airtest_method.check_exit(control.judgement_done,'FALSE',3600000):
            assert False,'判定推理失败'
        else:
            airtest_method.operate_sleep(5.0)




        