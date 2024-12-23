from tools.radom_character import radom_Name
from common.Airtest_method import airtest_method
from airtest.core.api import *
from elements.public_control import light_control,get_button_from_string

class management():
    def create_project(color):
        '''新建方案
        color light:浅色主题 dark:深色主题
        '''
        create_project_element = get_button_from_string(f"{color}_control.create_project")
        if not airtest_method.check_exit(create_project_element,'FALSE',5) :
            assert False,'找不到新建方案按钮'
        else:
            airtest_method.touch_button(create_project_element)
    
    def create_success(color):
        '''创建方案
        color light:浅色主题 dark:深色主题
        '''
        create_button = get_button_from_string(f"{color}_control.create_button")
        if not airtest_method.check_exit(create_button,'FALSE',5) :
            assert False,'找不到创建按钮' 
        else:     
            airtest_method.touch_button(create_button)
        
    def input_name(name,color):
        '''输入方案名称
        color light:浅色主题 dark:深色主题
        '''
        select_textbox = get_button_from_string(f"{color}_control.select_textbox")
        if not airtest_method.check_exit(select_textbox,'FALSE',5):
            assert False,'找不到方案名称编辑框' 
        else:     
            airtest_method.touch_button(select_textbox)  
        if name ==  '1':
            airtest_method.input_text(name)
        else:
            random_string = radom_Name.get_character(3)
            project_name = name + random_string
            airtest_method.input_text(project_name)
            return project_name
    
    def choice_project_type(color):
        '''选择方案类型
        color light:浅色主题 dark:深色主题
        '''
        #方案类型
        project_type = get_button_from_string(f"{color}_control.project_type")
        #串并联方案类型
        pipelines_project = get_button_from_string(f"{color}_control.pipelines_project")
        
        if not airtest_method.check_exit(project_type,'FALSE',5) :
            assert False,'找不到方案类型'   
        else:
            airtest_method.touch_button(project_type)
        if not airtest_method.check_exit(pipelines_project,'FALSE',5) :
            assert False,'找不到串并联方案类型'   
        else:
            airtest_method.touch_button(pipelines_project)

    def create_model(item):
        '''选择模型类型'''
        template = Template(item, threshold=0.7)
        if not airtest_method.check_exit(template,'FALSE',10) :
            assert False,'找不到算法类型'   
        else:
            airtest_method.touch_button(template)
        #点击创建按钮
        airtest_method.touch_button(light_control.create_button)

    def open_project(dataset):
        '''打开方案'''
        airtest_method.touch_button(light_control.open_project)
        airtest_method.touch_button(light_control.edit_box)
        airtest_method.operate_sleep()
        file_path = os.path.join(dataset)
        print(file_path)
        airtest_method.input_text(file_path)
        airtest_method.key_event('{ENTER}')
        airtest_method.operate_sleep()

    def click_project():
        '''选中方案'''
        airtest_method.touch_button(light_control.click_project)  
        airtest_method.key_event('{ENTER}')  
        airtest_method.operate_sleep(2.0)

    def manage_remark(remark): 
        '''添加方案备注'''       
        if not airtest_method.check_exit(light_control.create_remark,'FALSE',5) :
            assert False,'找不到方案备注编辑框' 
        else:      
            airtest_method.touch_button(light_control.create_remark)
            airtest_method.input_text(remark)

    def home():
        '''home键返回首页'''
        if not airtest_method.check_exit(light_control.home_button,'FALSE',10) :
            assert False,'找不到home键'
        else:
            airtest_method.touch_button(light_control.home_button)
            airtest_method.operate_sleep()

    def mixed_filtering(project_name):
        '''混合筛选'''
        if not airtest_method.check_exit(light_control.manage_input,'FALSE',10) :
            assert False,'找不到方案搜索框'
        else:
            airtest_method.touch_button(light_control.manage_input)
        airtest_method.input_text(project_name)
        airtest_method.key_event("{ENTER}")  #关键字筛选

        airtest_method.touch_button(light_control.manage_search)  #算法类型筛选
        airtest_method.touch_button(light_control.search_seg)
        if not airtest_method.check_exit(light_control.choice_proj,'FALSE',5) :
            assert False,'找不到选中方案'
        else:
            airtest_method.touch_button(light_control.choice_proj)   

    def right_click_toedit(text):
        '''右键编辑方案备注'''
        airtest_method.right_click((530,804)) #坐标自己填
        airtest_method.operate_sleep()
        if not airtest_method.check_exit(light_control.edited,'FALSE',5) :
            assert False,'找不到编辑按钮'
        else:
            airtest_method.touch_button(light_control.edited)
        if not airtest_method.check_exit(light_control.manage_remark,'FALSE',5) :
            assert False,'找不到方案备注编辑框' 
        else:      
            airtest_method.touch_button(light_control.manage_remark)
            airtest_method.input_text(text)
            airtest_method.touch_button(light_control.training_okbutton)


    def right_click_toclosed():
        '''右键关闭方案'''
        airtest_method.right_click((530,804)) #坐标自己填
        airtest_method.operate_sleep()
        if not airtest_method.check_exit(light_control.right_click_toclosed,'FALSE',5) :
            assert False,'找不到关闭按钮'
        else:
            airtest_method.touch_button(light_control.right_click_toclosed)

    def double_click_toopened():
        '''双击打开方案'''        
        airtest_method.double_click((557,804))
        airtest_method.operate_sleep(5.0)
    

    



    
            
