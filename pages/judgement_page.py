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

    def judgement_area(area):
        '''判定范围'''
        if not airtest_method.check_exit(control.judgement_area,'FALSE'):
            assert False,'找不到判定范围按钮'
        else:
            airtest_method.touch_button(control.judgement_area)
        '''勾选判定范围'''
        if airtest_method.check_exit(area):
            airtest_method.touch_button(area)  #勾选判定范围  
            airtest_method.operate_sleep()        
        airtest_method.touch_button(control.save_button)  #点击保存
        airtest_method.operate_sleep()

    def judgement_rules():
        '''添加判定标准'''
        if not airtest_method.check_exit(control.judgement_rules,'FALSE'):
            assert False,'找不到判定规则按钮'
        else:
            airtest_method.touch_button(control.judgement_rules)
            airtest_method.touch_button(control.add_rules)

    def advanced_trt_acceleration():
        '''高级配置-trt加速'''
        if not airtest_method.check_exit(control.advanced,'FALSE'):
            assert False,'找不到高级配置按钮'
        else:
            airtest_method.touch_button(control.advanced)
        if not airtest_method.check_exit(control.not_use_acceleration,'FALSE'):
            assert False,'找不到使用加速按钮'
        else:
            airtest_method.touch_button(control.not_use_acceleration)
            airtest_method.touch_button(control.use_trt_acceleration)
            airtest_method.touch_button(control.training_okbutton)

    def advanced_batch_infering(batch):
        '''高级配置-批量推理'''
        if not airtest_method.check_exit(control.advanced,'FALSE'):
            assert False,'找不到高级配置按钮'
        else:
            airtest_method.touch_button(control.advanced)
            airtest_method.touch_button(control.batch_infering)
            airtest_method.key_event("{BACKSPACE}")
            airtest_method.input_text(f'{batch}')
            airtest_method.touch_button(control.training_okbutton)


    def select_image(content):
        '''筛选图片'''
        if not airtest_method.check_exit(control.judgement_search,'FALSE'):
            assert False,'找不到图像搜索框'
        else:
            airtest_method.touch_button(control.judgement_search)
            airtest_method.input_text(content)
            airtest_method.double_click(control.select_image)


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
            airtest_method.operate_sleep(10.0)




        