from elements.public_control import control
import os
from common.Airtest_method import airtest_method 
from pages.open_sofrware import open_Software

class assess():  
    def model_assess():
        '''切换至模型评估页面'''
        if not airtest_method.check_exit(control.model_assess,'FALSE') :
            assert False,'找不到模型评估tab按钮'
        else:
            airtest_method.touch_button(control.model_assess)
    
    def assess_success():       
        '''判断是否评估完成''' 
        if not airtest_method.check_exit(control.report_button,'FALSE',360000) :
            assert False,'评估未完成'
        else:
            airtest_method.operate_sleep()
  
    def more_button():
         '''点击更多按钮'''
         airtest_method.touch_button(control.more_button)
         airtest_method.operate_sleep()
   
    def export_model():
        '''导出模型'''
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
     
    def export_report():
        '''导出报告'''
        airtest_method.touch_button(control.report_button)
        airtest_method.touch_button(control.report_name)
        airtest_method.touch_button(control.ok_button)
        airtest_method.operate_sleep()
        #airtest_method.touch_button(control.add_parameter)
        airtest_method.touch_button(control.export_button) 
        if not airtest_method.check_exit(control.report_success,'FALSE',10) :
            assert False,'报告未导出成功'
        else:
            open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
    
    def template_file():
        '''点击文件按钮'''
        if not airtest_method.check_exit(control.template_file,'FALSE') :
            assert False,'未找到文件按钮'
        else:
            airtest_method.touch_button(control.template_file)
 
    def template_help():
        '''点击帮助按钮'''
        if not airtest_method.check_exit(control.template_help,'FALSE') :
            assert False,'未找到帮助按钮'
        else:
            airtest_method.touch_button(control.template_help)
      
    def template_close():
        '''点击关闭按钮'''
        if not airtest_method.check_exit(control.template_close,'FALSE') :
            assert False,'未找到关闭按钮'
        else:
            airtest_method.touch_button(control.template_close)
 
    def user_guild():
        '''导出软件功能手册'''
        if not airtest_method.check_exit(control.user_guild,'FALSE') :
            assert False,'未找到软件功能手册'
        else:
            airtest_method.touch_button(control.user_guild)
            if not airtest_method.check_exit(control.user_success,'FALSE',10) :
                assert False,'软件功能手册未导出成功'
            else:
                open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")

    def operating_guild():
        '''导出软件操作手册'''
        if not airtest_method.check_exit(control.operating_guild,'FALSE') :
            assert False,'未找到软件操作手册'
        else:
            airtest_method.touch_button(control.operating_guild)
            if not airtest_method.check_exit(control.user_success,'FALSE',10) :
                assert False,'软件操作手册未导出成功'
            else:
                open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")

    def SDK_guild():
        '''导出SDK开发手册'''
        if not airtest_method.check_exit(control.SDK_guild,'FALSE') :
            assert False,'未找到SDK开发手册按钮'
        else:
            airtest_method.touch_button(control.SDK_guild)
            if not airtest_method.check_exit(control.SDK_success,'FALSE',10) :
                assert False,'SDK开发手册未导出成功'
            else:
                open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
  
    def home():
        '''home键'''
        if not airtest_method.check_exit(control.home_button,'FALSE') :
            assert False,'未找到home键'
        else:
            airtest_method.touch_button(control.home_button)

    def change_type():
        '''切换模型类型'''
        if not airtest_method.check_exit(control.change_type,'FALSE') :
            assert False,'未成功切换模型类型'
        else:
            airtest_method.touch_button(control.change_type)
  
    def template_quit():
        '''退出'''
        if not airtest_method.check_exit(control.template_quit,'FALSE') :
            assert False,'未成功退出'
        else:
            airtest_method.touch_button(control.template_quit)