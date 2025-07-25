from common.Airtest_method import airtest_method 
from elements.public_control import light_control

class judgement(): 
    def judgement_page():
        '''切换至综合判定页面'''
        if not airtest_method.check_exit(light_control.judgement_page,'FALSE'):
            assert False,'找不到综合判定按钮'
        else:
            airtest_method.touch_button(light_control.judgement_page)
            airtest_method.touch_button(light_control.judgement_area)

    def judgement_area(area):
        '''判定范围'''
        if not airtest_method.check_exit(light_control.judgement_area,'FALSE'):
            assert False,'找不到判定范围按钮'
        else:
            airtest_method.touch_button(light_control.judgement_area)
        '''勾选判定范围'''
        if not airtest_method.check_exit(area):
            assert False,'勾选判定范围失败'
        else:
            airtest_method.touch_button(area)  #勾选判定范围  
            airtest_method.operate_sleep()        
        airtest_method.touch_button(light_control.save_button)  #点击保存
        airtest_method.operate_sleep()

    def judgement_rules():
        '''添加判定标准'''
        if not airtest_method.check_exit(light_control.judgement_rules,'FALSE'):
            assert False,'找不到判定规则按钮'
        else:
            airtest_method.touch_button(light_control.judgement_rules)
            airtest_method.touch_button(light_control.add_rules)
            airtest_method.touch_button(light_control.save_button)  #点击保存

    def advanced_trt_acceleration():
        '''高级配置-trt加速'''
        if not airtest_method.check_exit(light_control.advanced,'FALSE'):
            assert False,'找不到高级配置按钮'
        else:
            airtest_method.touch_button(light_control.advanced)
        if not airtest_method.check_exit(light_control.not_use_acceleration,'FALSE'):
            assert False,'找不到使用加速按钮'
        else:
            airtest_method.touch_button(light_control.not_use_acceleration)
            airtest_method.touch_button(light_control.use_trt_16acceleration)
            airtest_method.touch_button(light_control.training_okbutton)

    def advanced_batch_infering(batch):
        '''高级配置-批量推理'''
        if not airtest_method.check_exit(light_control.advanced,'FALSE'):
            assert False,'找不到高级配置按钮'
        else:
            airtest_method.touch_button(light_control.advanced)
            airtest_method.touch_button(light_control.batch_infering)
            airtest_method.key_event("{BACKSPACE}")
            airtest_method.input_text(f'{batch}')
            airtest_method.touch_button(light_control.training_okbutton)

    def select_image(content):
        '''筛选图片'''
        if not airtest_method.check_exit(light_control.judgement_search,'FALSE'):
            assert False,'找不到图像搜索框'
        else:
            airtest_method.touch_button(light_control.judgement_search)
            airtest_method.input_text(content)
            airtest_method.key_event('{ENTER}')

    def export_rendering_image():
        '''导出渲染图'''
        airtest_method.double_click((376,243)) #切换到大图模式
        airtest_method.right_click((871,529)) #右键
        if not airtest_method.check_exit(light_control.export_rendering_image,'FALSE'):
            assert False,'找不到渲染图导出按钮'
        else:
            airtest_method.touch_button(light_control.export_rendering_image)
            airtest_method.operate_sleep(2.0)
        airtest_method.touch_button(light_control.choice_button)
        if not airtest_method.check_exit(light_control.upload_done,'FALSE'):      
            assert False,'找不到完成按钮'
        else:
            airtest_method.touch_button(light_control.upload_done)

    def judgement_infering():
        '''开始推理'''
        if not airtest_method.check_exit(light_control.judgement_infering,'FALSE'):
            assert False,'找不到判定范围按钮'
        else:
            airtest_method.touch_button(light_control.judgement_infering)

    def judgement_done():
        '''综合判定判定完成'''
        if not airtest_method.check_exit(light_control.judgement_done,'FALSE',3600000):
            assert False,'判定推理失败'
        else:
            airtest_method.operate_sleep(10.0)




        