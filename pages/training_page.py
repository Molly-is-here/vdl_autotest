from elements.public_control import control
from common.Airtest_method import airtest_method 
from airtest.core.api import *
from elements.elements_path import save_path

class training():
    '''切换至模型训练页面'''
    def model_training():
        if not airtest_method.check_exit(control.model_training,'FALSE') :
            assert False,'找不到模型训练tab按钮'
        else:
            airtest_method.touch_button(control.model_training)
            

    '''新增小卡片'''
    def add_card():
        airtest_method.touch_button(control.add_card)
        airtest_method.touch_button(control.nomal_training)
        airtest_method.operate_sleep()

    '''重命名'''
    def rename_button():
        airtest_method.touch_button(control.rename_button)

    '''修改备注'''
    def edit_comment():
        airtest_method.touch_button(control.edit_comment)
    
    '''复制'''
    def copy_button():
        airtest_method.touch_button(control.copy_button)

    '''删除'''
    def delete_button():
     airtest_method.touch_button(control.delete_button)
        
    '''选择模型类型'''
    def choice_model():
        if not airtest_method.check_exit(control.choice_model,'FALSE',5) :        
            assert False,'找不到模型选择按钮'
        else:         
            airtest_method.touch_button(control.choice_model)

    '''选择颜色模式'''
    def color_mode():
        if not airtest_method.check_exit(control.color_mode,'FALSE',5) :        
            assert False,'找不到颜色按钮'
        else:         
            airtest_method.touch_button(control.color_mode)

    '''图像缩放'''
    def image_scaling():
        if not airtest_method.check_exit(control.image_scaling,'FALSE',5) :        
            assert False,'找不到图像缩放按钮'
        else:         
            airtest_method.touch_button(control.image_scaling)

    '''图像裁切'''
    def image_cropping():
        if not airtest_method.check_exit(control.image_cropping,'FALSE',5) :        
            assert False,'找不到图像裁切按钮'
        else:         
            airtest_method.touch_button(control.image_cropping)

    '''将鼠标移动至自定义'''
    def mouse_move():
        airtest_method.touch_button(control.mouse_move)
        airtest_method.operate_sleep()
    
    '''选项为自定义'''
    def zidingyi_button():
        airtest_method.touch_button(control.zidingyi_button)
    
    '''下调benchsize'''
    def cut_benchsize():
        airtest_method.touch_button(control.cut_benchsize,times= 3)
    
    '''设置学习次数'''
    def set_study():
        airtest_method.touch_button(control.set_study)
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        airtest_method.input_text('2')
        airtest_method.operate_sleep()
    
    '''点击开始训练'''
    def star_training():
        airtest_method.touch_button(control.star_training)
        airtest_method.operate_sleep()
    
    '''点击查看评估'''
    def review_assess(name):
        if not airtest_method.check_exit(control.review_assess,'FALSE',3600000) :
            assert False,'训练未完成'
        else:  
            ct_screenshot = os.path.join(save_path.base_path, f"{name}.png")  
            airtest_method.screenshot(ct_screenshot)   #全屏截图  
            airtest_method.touch_button(control.review_assess)

    '''继续训练'''
    def continu_training():
        if not airtest_method.check_exit(control.continu_training,'FALSE',5) :        
            assert False,'找不到继续训练按钮'
        else:         
            airtest_method.touch_button(control.continu_training)

    '''增量训练'''
    def add_training():
        if not airtest_method.check_exit(control.add_training,'FALSE',5) :        
            assert False,'找不到增量训练按钮'
        else:         
            airtest_method.touch_button(control.add_training)

        
            

        