from elements.public_control import control
import os
from common.Airtest_method import airtest_method 

class assess():
    '''切换至模型评估页面'''
    def model_assess():
        if not airtest_method.check_exit(control.model_assess,'FALSE') :
            assert False,'找不到模型评估tab按钮'
        else:
            airtest_method.touch_button(control.model_assess)
    
    '''判断是否评估完成'''
    def assess_success():
        if not airtest_method.check_exit(control.report_button,'FALSE',36000) :
            assert False,'评估未完成'
        else:
            airtest_method.operate_sleep()

    '''点击更多按钮'''
    def more_button():
         airtest_method.touch_button(control.more_button)
         airtest_method.operate_sleep()

    '''导出模型'''
    def export_model():
        airtest_method.touch_button(control.export_model)

        airtest_method.touch_button(control.file_name)
        airtest_method.operate_sleep()

        airtest_method.touch_button(control.edit_box)
        airtest_method.operate_sleep()

        #输入指定路径
        current_dir = os.getcwd()
        airtest_method.input_text(current_dir)

        airtest_method.touch_button(control.jump_click)

        airtest_method.touch_button(control.choice_button)

        airtest_method.touch_button(control.export_button)
        airtest_method.operate_sleep(20.0)
    
    '''导出报告'''
    def export_report():
        airtest_method.touch_button(control.report_button)
        airtest_method.touch_button(control.report_name)
        airtest_method.touch_button(control.ok_button)
        airtest_method.operate_sleep()
        #airtest_method.touch_button(control.add_parameter)
        airtest_method.touch_button(control.export_button)     
   
    '''点击文件按钮'''
    def template_file():
        airtest_method.touch_button(control.template_file)
        airtest_method.operate_sleep()
    
    '''点击关闭按钮'''
    def template_close():
        airtest_method.touch_button(control.template_close)
        airtest_method.operate_sleep()

    def home():
        airtest_method.touch_button(control.home_button)

    def change_type():
        airtest_method.touch_button(control.change_type)