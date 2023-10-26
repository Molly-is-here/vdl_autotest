from elements.public_control import control
from tools.radom_character import radom_Name
from common.Airtest_method import airtest_method
from airtest.core.api import *

class management():
    def create_project():
        airtest_method.touch_button(control.create_project)
        

    def input_name(name):
        airtest_method.touch_button(control.select_textbox)
        '''输入方案名称'''
        random_string = radom_Name.get_character(3)
        project_name = name + random_string
        airtest_method.input_text(project_name)
        return project_name

    def create_model(item):
        #选择模型类型
        template = Template(item, threshold=0.7)
        airtest_method.assert_method(template)
        airtest_method.touch_button(template)
        #点击创建按钮
        airtest_method.touch_button(control.create_button)

    def open_project(dataset):
        airtest_method.touch_button(control.open_project)
        airtest_method.touch_button(control.edit_box)
        airtest_method.operate_sleep()
        file_path = os.path.join(dataset)
        print(file_path)
        airtest_method.input_text(file_path)
        airtest_method.touch_button(control.jump_click)
        airtest_method.operate_sleep()

    def click_project():
        airtest_method.touch_button(control.click_project)       
        airtest_method.touch_button(control.ok_button)



    
            
