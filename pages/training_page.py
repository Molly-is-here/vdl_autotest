from elements.public_control import control
from common.Airtest_method import airtest_method 
from airtest.core.api import *
from elements.elements_path import save_path


class training():
    
    def model_training():
        '''切换至模型训练页面'''
        if not airtest_method.check_exit(control.model_training,'FALSE',5) :
            assert False,'找不到模型训练tab按钮'
        else:
            airtest_method.touch_button(control.model_training)
             
    def add_card():
        '''新增小卡片'''
        airtest_method.touch_button(control.add_card)
        airtest_method.touch_button(control.nomal_training)
        airtest_method.operate_sleep()

    def renamed_card(content):
        '''重命名卡片'''
        airtest_method.touch_button(control.new_card)
        airtest_method.right_click(coords=(199,195)) #鼠标右键（自己填坐标）
        airtest_method.touch_button(control.rename_button)
        airtest_method.key_event("^a") #全选
        airtest_method.input_text(content)
  
    def edit_comment(content):
        '''修改备注'''
        if not airtest_method.check_exit(control.more_button,'FALSE',5) :
            assert False,'找不到更多按钮'
        else:
            airtest_method.touch_button(control.more_button,2)
        airtest_method.touch_button(control.edit_comment)
        airtest_method.input_text(content)

    def copy_card():
        '''复制卡片'''
        if not airtest_method.check_exit(control.more_button,'FALSE',5) :
            assert False,'找不到更多按钮'
        else:
            airtest_method.touch_button(control.more_button,2)
        airtest_method.touch_button(control.copy_button)

    def delete_card():
        '''删除卡片'''
        airtest_method.right_click(coords=(199,195)) #鼠标右键（自己填坐标）
        airtest_method.touch_button(control.delete_button)
        if not airtest_method.check_exit(control.delete_prompt,'FALSE',10):
            assert False,'未出现删除提示，删除失败'
        else:
            airtest_method.touch_button(control.training_okbutton)

    def set_template():
        '''设置为模版'''
        airtest_method.right_click(coords=(199,195)) #鼠标右键（自己填坐标）
        airtest_method.touch_button(control.set_template)
           
    def choice_model(type):
        '''选择模型类型'''
        if not airtest_method.check_exit(control.choice_model,'FALSE',5) :        
            assert False,'找不到模型选择按钮'
        else:         
            airtest_method.touch_button(control.choice_model)            
            if not airtest_method.check_exit(type,'FALSE',5):      
                assert False,'模型类型切换失败'
            else:
                airtest_method.touch_button(type) #选择模型类型

    def uad_choice_model(type):
        '''选择UAD模型类型'''
        if not airtest_method.check_exit(control.uad_choice_model,'FALSE',5) :        
            assert False,'找不到模型选择按钮'
        else:         
            airtest_method.touch_button(control.uad_choice_model)
            if not airtest_method.check_exit(type,'FALSE',5) :      
                assert False,'模型类型切换失败'
            else:
                airtest_method.touch_button(type) #选择模型类型               

    def color_mode(color):
        '''选择颜色模式'''
        if not airtest_method.check_exit(control.color_mode,'FALSE',5) :        
            assert False,'找不到颜色按钮'
        else: 
            if color == 0:
                return True
            else:        
                airtest_method.touch_button(control.color_mode)
                if not airtest_method.check_exit(color,'FALSE',5) :        
                    assert False,f'找不到{color}按钮'
                else:       
                    airtest_method.touch_button(color)
  
    def image_scaling(size):
        '''图像缩放'''
        if not airtest_method.check_exit(control.image_scaling,'FALSE',5) :        
            assert False,'找不到图像缩放按钮'
        else:  
            if size == 0:
                return True 
            else:      
                airtest_method.touch_button(control.image_scaling)
                if not airtest_method.check_exit(size,'FALSE',5) :        
                    assert False,f'找不到{size}按钮'
                else:       
                    airtest_method.touch_button(size)
  
    def image_cropping():
        '''图像裁切'''
        if not airtest_method.check_exit(control.image_cropping,'FALSE',5) :        
            assert False,'找不到图像裁切按钮'
        else:         
            airtest_method.touch_button(control.image_cropping)
        airtest_method.operate_sleep()
        if not airtest_method.check_exit(control.cropping_true,'FALSE',5) :        
            assert False,'找不到是按钮'
        else:      
            airtest_method.touch_button(control.cropping_true)
            
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
    
    def set_study(learning_times):
        '''设置学习次数'''
        airtest_method.touch_button(control.set_study)
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        airtest_method.input_text(learning_times)
        airtest_method.operate_sleep()
     
    def star_training():
        '''点击开始训练'''
        airtest_method.touch_button(control.star_training)
        airtest_method.operate_sleep(5.0)

    def training_success(name):
        ct_screenshot = os.path.join(save_path.base_path, f"{name}.png")       
        if not airtest_method.check_exit(control.review_assess,'TRUE',3600000): 
            assert False,'训练未完成'
        else: 
            airtest_method.screenshot(ct_screenshot)   #全屏截图
      
    def review_assess(name):
        '''点击查看评估'''
        ct_screenshot = os.path.join(save_path.base_path, f"{name}.png")       
        if not airtest_method.check_exit(control.infering_finished,'FALSE',3600000): 
            assert False,'训练未完成'
        else: 
            airtest_method.screenshot(ct_screenshot)   #全屏截图
        
    def continu_training():
        '''继续训练'''
        if not airtest_method.check_exit(control.continu_training,'FALSE',5) :        
            assert False,'找不到继续训练按钮'
        else:         
            airtest_method.touch_button(control.continu_training)
  
    def add_training():
        '''增量训练'''
        if not airtest_method.check_exit(control.more_button,'FALSE',5) :
            assert False,'找不到更多按钮'
        else:
            airtest_method.touch_button(control.more_button)
        if not airtest_method.check_exit(control.add_training,'FALSE',5) :        
            assert False,'找不到增量训练按钮'
        else:         
            airtest_method.touch_button(control.add_training)

        
            

        