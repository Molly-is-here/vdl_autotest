from common.Airtest_method import airtest_method
from airtest.core.api import *
from elements.public_control import light_control,get_button_from_string

class data():
    
    def data_management_page():
        '''数据管理页面'''
        if not airtest_method.check_exit(light_control.data_management_page,'FALSE',5) :
            assert False,'找不到数据管理tab按钮'
        else:
            airtest_method.touch_button(light_control.data_management_page)

    def finish_button():
        '''点击完成''' 
        airtest_method.touch_button(light_control.upload_done)
   
    def add_file(file_path):
        '''导入文件夹'''   
        if not airtest_method.check_exit(light_control.add_file,'FALSE') :
            assert False,'找不到添加文件夹按钮'
        else:
            airtest_method.touch_button(light_control.add_file)
        airtest_method.operate_sleep() 
        if not airtest_method.check_exit(light_control.choice_file,'FALSE',20) :
            assert False,'选择文件夹按钮'
        else:
            airtest_method.touch_button(light_control.choice_file)            
        airtest_method.input_text(file_path)
        airtest_method.key_event('{ENTER}')
        # airtest_method.touch_button(light_control.jump_click)
        # airtest_method.key_event('{ENTER}')
        airtest_method.touch_button(light_control.choice_button)

        if not airtest_method.check_exit(light_control.upload_label,'FALSE') :
            assert False,'找不到导入完成标志'
        else:
            airtest_method.touch_button(light_control.upload_done)

    def add_image(file_path,color):   
        '''导入图像
        color light:浅色主题 dark:深色主题
        '''
        #添加图像
        add_image_element = get_button_from_string(f"{color}_control.add_image")
        #导入完成标志
        upload_label = get_button_from_string(f"{color}_control.upload_label")
        #完成按钮
        upload_done = get_button_from_string(f"{color}_control.upload_done")

        if not airtest_method.check_exit(add_image_element,'FALSE') :
            assert False,'找不到添加图像按钮'
        else:
            airtest_method.touch_button(add_image_element)
        airtest_method.touch_button(light_control.choice_file)   
        airtest_method.input_text(file_path)
        airtest_method.key_event('{ENTER}')
        airtest_method.touch_button(light_control.click_area)
        '''全选图片'''
        airtest_method.key_event("^a")
        airtest_method.key_event('{ENTER}')
        if not airtest_method.check_exit(upload_label,'FALSE') :
            assert False,'找不到导入完成标志'
        else:
            airtest_method.touch_button(upload_done)


    def add_label(file_path,color):
        '''导入标注
        color light:浅色主题 dark:深色主题
        '''   
        #添加标注
        add_label_element = get_button_from_string(f"{color}_control.add_label")
        #导入完成标志
        upload_label = get_button_from_string(f"{color}_control.upload_label")
        #完成按钮
        upload_done = get_button_from_string(f"{color}_control.upload_done")

        if not airtest_method.check_exit(add_label_element,'FALSE',5) :
            assert False,'找不到添加标注按钮'
        else:
            airtest_method.touch_button(add_label_element)
        airtest_method.touch_button(light_control.choice_file) 
        airtest_method.input_text(file_path)
        airtest_method.key_event('{ENTER}')
        airtest_method.touch_button(light_control.click_area)
        '''全选标注'''
        airtest_method.key_event("^a")
        airtest_method.key_event('{ENTER}')

        if not airtest_method.check_exit(upload_label,'FALSE') :
            assert False,'找不到导入完成标志'
        else:
            airtest_method.touch_button(upload_done)

    def add_image_underscore(file_path):
        '''下划线添加图像'''
        if not airtest_method.check_exit(light_control.add_image_underscore,'FALSE') :
            assert False,'找不到添加图像下划线'
        else:
            airtest_method.touch_button(light_control.add_image_underscore)
        airtest_method.touch_button(light_control.choice_file)   
        airtest_method.input_text(file_path)
        airtest_method.key_event("{ENTER}")
        airtest_method.touch_button(light_control.click_area)
        '''全选图片'''
        airtest_method.key_event("^a")
        airtest_method.key_event("{ENTER}")
        if not airtest_method.check_exit(light_control.upload_label,'FALSE') :
            assert False,'找不到导入完成标志'

    def project_flow(color):
        '''点击方案流程
        color light:浅色主题 dark:深色主题
        '''
        project_flow_element = get_button_from_string(f"{color}_control.project_flow")       
        if not airtest_method.check_exit(project_flow_element,'FALSE',5) :
            assert False,'找不到方案流程按钮'
        else:
            airtest_method.touch_button(project_flow_element)

    def add_dataset():
        '''添加数据源'''
        if not airtest_method.check_exit(light_control.add_dataset,'FALSE',5) :
            assert False,'数据源添加失败'
        else:
            airtest_method.touch_button(light_control.add_dataset)

    def add_module(element):
        '''添加模块'''
        data.add_dataset()
        if not airtest_method.check_exit(element,'FALSE',5) :
            assert False,'未找到前置模块'
        else:
            airtest_method.touch_button(element)

    def add_post_module(element):
        '''添加后置模块'''
        airtest_method.touch_button(light_control.pre_module)  #点击前置模块的‘+’符号新增模块
        if not airtest_method.check_exit(element,'FALSE',5) :
            assert False,'未找到后置模块'
        else:
            airtest_method.touch_button(element)
        airtest_method.operate_sleep()

    def dataset_management(color):
        '''数据源管理页面'''
        airtest_method.operate_sleep(2.0)
        data.project_flow(color)
        airtest_method.touch_button(light_control.dataset_module)
        data.project_flow(color)

    def add_tag(content):
        '''添加标签'''       
        if not airtest_method.check_exit(light_control.tag_dropdown,'FALSE',5) :
            assert False,'未找到标签下拉框'
        else:
            airtest_method.touch_button(light_control.tag_dropdown)
            airtest_method.touch_button(light_control.tag_searching)
            airtest_method.input_text(content)
            airtest_method.key_event('{ENTER}')
            airtest_method.touch_button(light_control.checkbox)
            airtest_method.touch_button(light_control.upload_label)
            airtest_method.touch_button(light_control.upload_done)

    def mixed_filtering(content):
        '''混合筛选'''
        if not airtest_method.check_exit(light_control.manage_input,'FALSE',10) :
            assert False,'找不到方案搜索框'
        else:
            airtest_method.touch_button(light_control.manage_input)
        airtest_method.input_text(content)
        airtest_method.key_event("{ENTER}")  #关键字筛选

        airtest_method.touch_button(light_control.manage_search) #标注状态筛选
        airtest_method.touch_button(light_control.finish_labeled)
        airtest_method.touch_button(light_control.add_file)
        if not airtest_method.check_exit(light_control.add_image_underscore,'TRUE',5) :
            assert False,'组合筛选无效'

    def add_roi():
        '''新增ROI'''
        if not airtest_method.check_exit(light_control.add_roi,'FALSE',10) :
            assert False,'找不到新增ROI按钮'
        else:
            airtest_method.touch_button(light_control.add_roi)

    def setting_size(size1,size2):
        '''自定义ROI-大小设置'''
        if not airtest_method.check_exit(light_control.roi_size_left,'FALSE',10) :
            assert False,'找不到大小左边的编辑框'
        else:
            airtest_method.touch_button(light_control.roi_size_left)
            airtest_method.key_event('^a')
            airtest_method.key_event('{BACKSPACE}')
            airtest_method.input_text(size1)
            airtest_method.key_event('{ENTER}')

        if not airtest_method.check_exit(light_control.roi_size_right,'FALSE',10) :
            assert False,'找不到大小右边的编辑框'
        else:
            airtest_method.touch_button(light_control.roi_size_right)
            airtest_method.key_event('^a')
            airtest_method.key_event('{BACKSPACE}')
            airtest_method.input_text(size2)
            airtest_method.key_event('{ENTER}')

    def setting_displacement(size1,size2):
        '''自定义ROI-位移设置'''
        if not airtest_method.check_exit(light_control.roi_displacement_left,'FALSE',10) :
            assert False,'找不到大小左边的编辑框'
        else:
            airtest_method.touch_button(light_control.roi_displacement_left)
            airtest_method.key_event('^a')
            airtest_method.key_event('{BACKSPACE}')
            airtest_method.input_text(size1)
            airtest_method.key_event('{ENTER}')

        if not airtest_method.check_exit(light_control.roi_displacement_right,'FALSE',10) :
            assert False,'找不到大小右边的编辑框'
        else:
            airtest_method.touch_button(light_control.roi_displacement_right)
            airtest_method.key_event('^a')
            airtest_method.key_event('{BACKSPACE}')
            airtest_method.input_text(size2)
            airtest_method.key_event('{ENTER}')

    def change_ROI_mode():
        '''切换roi模式'''
        if not airtest_method.check_exit(light_control.roi_mode_switching,'FALSE',10) :
            assert False,'找不到模式切换框'
        else:
            airtest_method.touch_button(light_control.roi_mode_switching)
            airtest_method.touch_button(light_control.proportional_splitting)

    def splitting_number(size1,size2):
            '''比例切分ROI-数量设置'''
            #设置行数
            airtest_method.click_coordinate_point((1663,285))
            airtest_method.key_event('^a')
            airtest_method.key_event('{BACKSPACE}')
            airtest_method.input_text(size1)
            airtest_method.key_event('{ENTER}')

            #设置列数
            airtest_method.click_coordinate_point((1821,285))
            airtest_method.key_event('^a')
            airtest_method.key_event('{BACKSPACE}')
            airtest_method.input_text(size2)
            airtest_method.key_event('{ENTER}')

    def splitting_size(size1,size2):
        '''比例切分ROI-大小设置'''
        #设置宽度
        airtest_method.click_coordinate_point((1663,360))
        airtest_method.key_event('^a')
        airtest_method.key_event('{BACKSPACE}')
        airtest_method.input_text(size1)
        airtest_method.key_event('{ENTER}')

        #设置高度
        airtest_method.click_coordinate_point((1821,360))
        airtest_method.key_event('^a')
        airtest_method.key_event('{BACKSPACE}')
        airtest_method.input_text(size2)
        airtest_method.key_event('{ENTER}')
    def splitting_interval(size1,size2):
            '''比例切分ROI-间隔设置'''
            #设置宽度间隔
            airtest_method.click_coordinate_point((1663,440))
            airtest_method.key_event('^a')
            airtest_method.key_event('{BACKSPACE}')
            airtest_method.input_text(size1)
            airtest_method.key_event('{ENTER}')

            #设置高度间隔
            airtest_method.click_coordinate_point((1821,440))
            airtest_method.key_event('^a')
            airtest_method.key_event('{BACKSPACE}')
            airtest_method.input_text(size2)
            airtest_method.key_event('{ENTER}')
    def splitting_displacement(size1,size2):
        '''比例切分ROI-偏移设置'''
        #设置X轴偏移
        airtest_method.click_coordinate_point((1663,517))
        airtest_method.key_event('^a')
        airtest_method.key_event('{BACKSPACE}')
        airtest_method.input_text(size1)
        airtest_method.key_event('{ENTER}')

        #设置Y轴偏移
        airtest_method.click_coordinate_point((1821,517))
        airtest_method.key_event('^a')
        airtest_method.key_event('{BACKSPACE}')
        airtest_method.input_text(size2)
        airtest_method.key_event('{ENTER}')

    def add_rapid_module():
        '''新建快速定位模块'''
        if not airtest_method.check_exit(light_control.rapid_module,'FALSE',10) :
            assert False,'找不到快速定位模块'
        else:
            airtest_method.touch_button(light_control.rapid_module)

    def add_template(template_name,points):
        '''新增模版'''
        if not airtest_method.check_exit(light_control.add_template,'FALSE',10) :
            assert False,'找不到添加模版按钮'
        else:
            airtest_method.touch_button(light_control.add_template)
        if not airtest_method.check_exit(light_control.edit_name,'FALSE',10):
            assert False,'找不到名称编辑框'
        else:
            airtest_method.touch_button(light_control.edit_name)
            airtest_method.input_text(template_name)
            airtest_method.key_event('{ENTER}')
        airtest_method.click_coordinate_point(points)
    def rapid_single_test():
        '''快速定位单张测试'''
        if not airtest_method.check_exit(light_control.single_test,'FALSE',10) :
            assert False,'找不到单张测试按钮'
        else:
            airtest_method.touch_button(light_control.single_test)
            airtest_method.operate_sleep(3.0)

    def rapid_full_test():
        '''快速定位全量测试'''
        if not airtest_method.check_exit(light_control.full_test,'FALSE',10) :
            assert False,'找不到全量测试按钮'
        else:
            airtest_method.touch_button(light_control.full_test)
            airtest_method.operate_sleep(10.0)
            airtest_method.touch_button(light_control.training_okbutton)
            airtest_method.key_event("^s") #保存结果

    def set_filter_parameter(number,points):
        '''调整参数'''
        airtest_method.click_coordinate_point(points)
        if not airtest_method.check_exit(light_control.filter_parameter,'FALSE',10) :
            assert False,'找不到过滤参数配置'
        else:
            airtest_method.touch_button(light_control.filter_parameter)
        if not airtest_method.check_exit(light_control.max_target,'FALSE',10) :
            assert False,'找不到最大目标数'
        else:
            airtest_method.touch_button(light_control.max_target)
            airtest_method.key_event("^a")
            airtest_method.key_event('{BACKSPACE}')
            airtest_method.input_text(number)
            airtest_method.touch_button(light_control.training_okbutton)  

    def update_to_post_module():
        '''更新数据到后置模块'''
        if not airtest_method.check_exit(light_control.update_to_post_module,'FALSE',10) :
            assert False,'找不到更新按钮'
        else:
            airtest_method.touch_button(light_control.update_to_post_module)







        
        



        
        
    