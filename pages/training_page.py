from elements.public_control import control
from common.Airtest_method import airtest_method 
from airtest.core.api import *
from elements.elements_path import save_path

class training():
    
    def model_training():
        '''切换至模型训练页面'''
        if not airtest_method.check_exit(control.model_training,'FALSE') :
            assert False,'找不到模型训练tab按钮'
        else:
            airtest_method.touch_button(control.model_training)
             
    def add_card():
        '''新增小卡片'''
        airtest_method.touch_button(control.add_card)
        airtest_method.touch_button(control.nomal_training)
        airtest_method.operate_sleep()

    
    def rename_button():
        '''重命名'''
        airtest_method.touch_button(control.rename_button)

    def edit_comment():
        '''修改备注'''
        airtest_method.touch_button(control.edit_comment)
    
   
    def copy_button():
        '''复制'''
        airtest_method.touch_button(control.copy_button)
  
    def delete_button():
     '''删除'''
     airtest_method.touch_button(control.delete_button)
           
    def choice_model():
        '''选择模型类型'''
        if not airtest_method.check_exit(control.choice_model,'FALSE',5) :        
            assert False,'找不到模型选择按钮'
        else:         
            airtest_method.touch_button(control.choice_model)

    def color_mode():
        '''选择颜色模式'''
        if not airtest_method.check_exit(control.color_mode,'FALSE',5) :        
            assert False,'找不到颜色按钮'
        else:         
            airtest_method.touch_button(control.color_mode)
  
    def image_scaling():
        '''图像缩放'''
        if not airtest_method.check_exit(control.image_scaling,'FALSE',5) :        
            assert False,'找不到图像缩放按钮'
        else:         
            airtest_method.touch_button(control.image_scaling)
  
    def image_cropping():
        '''图像裁切'''
        if not airtest_method.check_exit(control.image_cropping,'FALSE',5) :        
            assert False,'找不到图像裁切按钮'
        else:         
            airtest_method.touch_button(control.image_cropping)

    def mouse_move():
        '''将鼠标移动至自定义'''
        airtest_method.touch_button(control.mouse_move)
        airtest_method.operate_sleep()
    
    def zidingyi_button():
        '''选项为自定义'''
        airtest_method.touch_button(control.zidingyi_button)
      
    def cut_benchsize():
        '''下调benchsize'''
        airtest_method.touch_button(control.cut_benchsize,times= 3)
    
    def set_study():
        '''设置学习次数'''
        airtest_method.touch_button(control.set_study)
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        airtest_method.input_text('2')
        airtest_method.operate_sleep()
     
    def star_training():
        '''点击开始训练'''
        airtest_method.touch_button(control.star_training)
        airtest_method.operate_sleep()
      
    def review_assess(name):
        '''点击查看评估'''
        if not airtest_method.check_exit(control.review_assess,'FALSE',3600000) :
            assert False,'训练未完成'
        else:  
            ct_screenshot = os.path.join(save_path.base_path, f"{name}.png")  
            airtest_method.screenshot(ct_screenshot)   #全屏截图  
            airtest_method.touch_button(control.review_assess)
 
    def continu_training():
        '''继续训练'''
        if not airtest_method.check_exit(control.continu_training,'FALSE',5) :        
            assert False,'找不到继续训练按钮'
        else:         
            airtest_method.touch_button(control.continu_training)
  
    def add_training():
        '''增量训练'''
        if not airtest_method.check_exit(control.add_training,'FALSE',5) :        
            assert False,'找不到增量训练按钮'
        else:         
            airtest_method.touch_button(control.add_training)

        
            

        