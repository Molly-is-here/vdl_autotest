from elements.public_control import control
from tools.radom_character import radom_Name
from common.Airtest_method import airtest_method
from airtest.core.api import *

class management():
    def create_project():
        '''新建方案'''
        if not airtest_method.check_exit(control.create_project,'FALSE',5) :
            assert False,'找不到新建方案按钮'
        else:
            airtest_method.touch_button(control.create_project)
        
    def input_name(name):
        '''输入方案名称'''
        airtest_method.touch_button(control.select_textbox)       
        random_string = radom_Name.get_character(3)
        project_name = name + random_string
        airtest_method.input_text(project_name)
        return project_name
    
    def choice_project_type():
        '''选择方案类型'''
        if not airtest_method.check_exit(control.project_type,'FALSE',5) :
            assert False,'找不到方案类型'   
        else:
            airtest_method.touch_button(control.project_type)
        if not airtest_method.check_exit(control.pipelines_project,'FALSE',5) :
            assert False,'找不到串并联方案类型'   
        else:
            airtest_method.touch_button(control.pipelines_project)
        

    def create_model(item):
        '''选择模型类型'''
        template = Template(item, threshold=0.7)
        airtest_method.assert_method(template)
        airtest_method.touch_button(template)
        #点击创建按钮
        airtest_method.touch_button(control.create_button)

    def open_project(dataset):
        '''打开方案'''
        airtest_method.touch_button(control.open_project)
        airtest_method.touch_button(control.edit_box)
        airtest_method.operate_sleep()
        file_path = os.path.join(dataset)
        print(file_path)
        airtest_method.input_text(file_path)
        airtest_method.touch_button(control.jump_click)
        airtest_method.operate_sleep()

    def click_project():
        '''选中方案'''
        airtest_method.touch_button(control.click_project)       
        airtest_method.touch_button(control.ok_button)

    def manage_remark(content): 
        '''添加方案备注'''       
        if not airtest_method.check_exit(control.manage_remark,'FALSE',5) :
            assert False,'找不到方案备注编辑框' 
        else:      
            airtest_method.touch_button(control.manage_remark)
            airtest_method.input_text(content)

    def create_success():
        '''创建方案'''
        if not airtest_method.check_exit(control.create_button,'FALSE',5) :
            assert False,'找不到创建按钮' 
        else:     
            airtest_method.touch_button(control.create_button)



    
            
