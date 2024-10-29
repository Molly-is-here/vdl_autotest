from common.Airtest_method import airtest_method 
from airtest.core.api import *
from elements.elements_path import save_path
from elements.public_control import light_control,get_button_from_string

class training():
    
    def model_training(color):
        '''切换至模型训练页面
        color light:浅色主题 dark:深色主题
        '''
        model_training_element = get_button_from_string(f"{color}_control.model_training")
        if not airtest_method.check_exit(model_training_element,'FALSE',5) :
            assert False,'找不到模型训练tab按钮'
        else:
            airtest_method.touch_button(model_training_element)
    def add_card(color):
        '''新增小卡片
        color light:浅色主题 dark:深色主题
        '''
        #新增训练小卡片
        add_card_element = get_button_from_string(f"{color}_control.add_card")
        #常规训练
        nomal_training = get_button_from_string(f"{color}_control.nomal_training")
        
        airtest_method.touch_button(add_card_element)
        airtest_method.touch_button(nomal_training)
        airtest_method.operate_sleep()

    def renamed_card(content):
        '''重命名卡片'''
        airtest_method.touch_button(light_control.new_card)
        airtest_method.right_click(coords=(199,195)) #鼠标右键（自己填坐标）
        airtest_method.touch_button(light_control.rename_button)
        airtest_method.key_event("^a") #全选
        airtest_method.input_text(content)
  
    def edit_comment(content):
        '''修改备注'''
        if not airtest_method.check_exit(light_control.more_button,'FALSE',5) :
            assert False,'找不到更多按钮'
        else:
            airtest_method.touch_button(light_control.more_button,2)
        airtest_method.touch_button(light_control.edit_comment)
        airtest_method.input_text(content)

    def copy_card():
        '''复制卡片'''
        if not airtest_method.check_exit(light_control.more_button,'FALSE',5) :
            assert False,'找不到更多按钮'
        else:
            airtest_method.touch_button(light_control.more_button,2)
        airtest_method.touch_button(light_control.copy_button)

    def delete_card():
        '''删除卡片'''
        airtest_method.right_click(coords=(199,195)) #鼠标右键（自己填坐标）
        airtest_method.touch_button(light_control.delete_button)
        if not airtest_method.check_exit(light_control.delete_prompt,'FALSE',10):
            assert False,'未出现删除提示，删除失败'
        else:
            airtest_method.touch_button(light_control.training_okbutton)

    def set_template():
        '''设置为模版'''
        airtest_method.right_click(coords=(199,195)) #鼠标右键（自己填坐标）
        airtest_method.touch_button(light_control.set_template)
           
    def choice_model(type):
        '''选择模型类型'''
        if not airtest_method.check_exit(light_control.choice_model,'FALSE',5) :        
            assert False,'找不到模型选择按钮'
        else:         
            airtest_method.touch_button(light_control.choice_model)            
            if not airtest_method.check_exit(type,'FALSE',5):      
                assert False,'模型类型切换失败'
            else:
                airtest_method.touch_button(type) #选择模型类型

    def uad_moudle_type():
        '''选择无监督训练模型类型'''
        if not airtest_method.check_exit(light_control.uad_cls,'FALSE',5) :      
                assert False,'展示类型按钮选中失败'
        else:
            airtest_method.touch_button(light_control.uad_cls)
            airtest_method.touch_button(light_control.uad_seg)

    def uad_choice_model(type):
        '''选择UAD模型类型'''
        if not airtest_method.check_exit(light_control.uad_choice_model,'FALSE',5) :        
            assert False,'找不到模型选择按钮'
        else:         
            airtest_method.touch_button(light_control.uad_choice_model)
            if not airtest_method.check_exit(type,'FALSE',5) :      
                assert False,'模型类型切换失败'
            else:
                airtest_method.touch_button(type) #选择模型类型               

    def color_mode(color):
        '''选择颜色模式'''
        if not airtest_method.check_exit(light_control.color_mode,'FALSE',5) :        
            assert False,'找不到颜色按钮'
        else: 
            if color == 0:
                return True
            else:        
                airtest_method.touch_button(light_control.color_mode)
                if not airtest_method.check_exit(color,'FALSE',5) :        
                    assert False,f'找不到{color}按钮'
                else:       
                    airtest_method.touch_button(color)
  
    def image_scaling(size):
        '''图像缩放'''
        if not airtest_method.check_exit(light_control.image_scaling,'FALSE',5) :        
            assert False,'找不到图像缩放按钮'
        else:  
            if size == 0:
                return True 
            else:      
                airtest_method.touch_button(light_control.image_scaling)
                if not airtest_method.check_exit(size,'FALSE',5) :        
                    assert False,f'找不到{size}按钮'
                else:       
                    airtest_method.touch_button(size)
  
    def image_cropping():
        '''图像裁切'''
        if not airtest_method.check_exit(light_control.image_cropping,'FALSE',5) :        
            assert False,'找不到图像裁切按钮'
        else:         
            airtest_method.touch_button(light_control.image_cropping)
        airtest_method.operate_sleep()
        if not airtest_method.check_exit(light_control.cropping_true,'FALSE',5) :        
            assert False,'找不到是按钮'
        else:      
            airtest_method.touch_button(light_control.cropping_true)
            
    def mouse_move(color):
        '''将鼠标移动至自定义
        color light:浅色主题 dark:深色主题
        '''
        mouse_move_element = get_button_from_string(f"{color}_control.mouse_move")
        airtest_method.touch_button(mouse_move_element)
        airtest_method.operate_sleep()
    
    def zidingyi_button(color):
        '''选项为自定义
        color light:浅色主题 dark:深色主题
        '''
        zidingyi_button_element = get_button_from_string(f"{color}_control.zidingyi_button")
        airtest_method.touch_button(zidingyi_button_element)
      
    def cut_benchsize(color):
        '''下调benchsize
        color light:浅色主题 dark:深色主题
        '''
        training.mouse_move(color)
        training.zidingyi_button(color)
        cut_benchsize_element = get_button_from_string(f"{color}_control.cut_benchsize")
        airtest_method.touch_button(cut_benchsize_element,times= 3)
    
    def set_study(learning_times,color):
        '''设置学习次数
        color light:浅色主题 dark:深色主题
        '''
        set_study_element = get_button_from_string(f"{color}_control.set_study")
        airtest_method.touch_button(set_study_element)
        keyevent("^a")
        keyevent("{BACKSPACE}")
        airtest_method.input_text(learning_times)
        airtest_method.operate_sleep()

    def seq_set_study(learning_times):
        '''字符串算法设置学习次数'''
        #阶段1
        airtest_method.touch_button(light_control.seq_step1_study)
        keyevent("^a")
        keyevent("{BACKSPACE}")
        airtest_method.input_text(learning_times)
        airtest_method.operate_sleep()
        #阶段2
        airtest_method.touch_button(light_control.seq_step2_study)
        keyevent("^a")
        keyevent("{BACKSPACE}")
        airtest_method.input_text(learning_times)
        airtest_method.operate_sleep()
        #阶段3
        airtest_method.touch_button(light_control.seq_step3_study)
        keyevent("^a")
        keyevent("{BACKSPACE}")
        airtest_method.input_text(learning_times)
        airtest_method.operate_sleep()

    def star_training(color):
        '''点击开始训练
        color light:浅色主题 dark:深色主题
        '''
        star_training_element = get_button_from_string(f"{color}_control.star_training")
        airtest_method.touch_button(star_training_element)
        airtest_method.operate_sleep(5.0)

    def training_success(name):
        ct_screenshot = os.path.join(save_path.base_path, f"{name}.png")  
             
        if not airtest_method.check_exit(light_control.review_assess,'TRUE',3600000): 
            assert False,'训练未完成'
        else: 
            airtest_method.screenshot(ct_screenshot)   #全屏截图
      
    def review_assess(name):
        '''点击查看评估'''
        ct_screenshot = os.path.join(save_path.base_path, f"{name}.png")       
        if not airtest_method.check_exit(light_control.infering_finished,'FALSE',3600000): 
            assert False,'训练未完成'
        else: 
            airtest_method.screenshot(ct_screenshot)   #全屏截图
        
    def continu_training():
        '''继续训练'''
        if not airtest_method.check_exit(light_control.continu_training,'FALSE',5) :        
            assert False,'找不到继续训练按钮'
        else:         
            airtest_method.touch_button(light_control.continu_training)
  
    def add_training():
        '''增量训练'''
        if not airtest_method.check_exit(light_control.more_button,'FALSE',5) :
            assert False,'找不到更多按钮'
        else:
            airtest_method.touch_button(light_control.more_button)
        if not airtest_method.check_exit(light_control.add_training,'FALSE',5) :        
            assert False,'找不到增量训练按钮'
        else:         
            airtest_method.touch_button(light_control.add_training)

        
            

        