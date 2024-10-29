from elements.public_control import light_control
from elements.elements_path import save_path
from common.Airtest_method import airtest_method 
from common.Base_method import search_file
from pages.open_sofrware import open_Software
import os
import zipfile
import subprocess
from elements.public_control import get_button_from_string

class assess():  
    def model_assess(color):
        '''切换至模型评估页面
        color light:浅色主题 dark:深色主题
        '''
        model_assess_element = get_button_from_string(f"{color}_control.model_assess")
        if not airtest_method.check_exit(model_assess_element,'FALSE') :
            assert False,'找不到模型评估tab按钮'
        else:
            airtest_method.touch_button(model_assess_element)
    
    def assess_success(color):       
        '''判断是否评估完成
        color light:浅色主题 dark:深色主题
        ''' 
        infering_finished = get_button_from_string(f"{color}_control.infering_finished")
        if airtest_method.check_exit(infering_finished,'FALSE',360000) :
            airtest_method.operate_sleep(5.0)
        else:
            assert False,'评估出现异常'
            

    def assess_done():       
        '''通过后处理参数配置判断评估是否完成''' 
        if not airtest_method.check_exit(light_control.process_setting,'FALSE',360000) :
            assert False,'评估未完成'  
  
    def more_button():
         '''点击更多按钮'''
         airtest_method.touch_button(light_control.more_button)
         airtest_method.operate_sleep()
   
    def export_model():
        '''导出模型'''
        airtest_method.touch_button(light_control.export_model)
        airtest_method.operate_sleep()

        airtest_method.touch_button(light_control.file_name)
        airtest_method.operate_sleep()

        airtest_method.touch_button(light_control.edit_box)
        airtest_method.operate_sleep()

        #输入指定路径
        current_dir = os.getcwd()
        airtest_method.input_text(current_dir)
        airtest_method.key_event('{ENTER}')
        airtest_method.touch_button(light_control.choice_button)

        airtest_method.touch_button(light_control.export_button)
        airtest_method.operate_sleep(30.0)
        for i in range(2):
            airtest_method.touch_button(light_control.training_okbutton)
            airtest_method.operate_sleep()

    def export_SDK(path):
        '''导出SDK'''
        check_path = os.path.join(path,'export_SDK')
        search_file.check_exists(check_path)
        os.system('mkdir export_SDK')
        os.chmod('export_SDK', 0o777)
        airtest_method.touch_button(light_control.export_model)

        airtest_method.touch_button(light_control.file_name)
        airtest_method.operate_sleep()

        airtest_method.touch_button(light_control.edit_box)
        airtest_method.operate_sleep()
        airtest_method.input_text(check_path)
        airtest_method.key_event('{ENTER}')

        airtest_method.touch_button(light_control.choice_button)
        
        current_dir = os.path.join(os.getcwd(),'export_SDK')
        airtest_method.input_text(current_dir)
        
        if not airtest_method.check_exit(light_control.export_SDK,'FALSE',10) :
            assert False,'未找到打开SDK开关'
        else:
            airtest_method.touch_button(light_control.export_SDK)
            airtest_method.touch_button(light_control.export_button)
            airtest_method.operate_sleep(60.0)
            for i in range(2):
                airtest_method.touch_button(light_control.training_okbutton)
                airtest_method.operate_sleep()

    def unzip_SDK():
        '''解压SDK压缩包'''
        current_dir = os.path.join( os.getcwd(),'export_SDK') 
        Total_file = search_file.get_file(current_dir)  #SDK+模型压缩包
        # 打开压缩包
        with zipfile.ZipFile(os.path.join( current_dir,' '.join(Total_file)), 'r') as zip_ref:
            # 解压所有文件到指定目录
            zip_ref.extractall(current_dir)
        SDK_file = search_file.get_file(os.path.join(current_dir,'sdk'))  #解压SDK压缩包
        with zipfile.ZipFile(os.path.join(current_dir,'sdk',' '.join(SDK_file)), 'r') as zip_ref:
            # 解压所有文件到指定目录
            zip_ref.extractall(current_dir)
        zip_ref.close()

    def copy_SDK_dll():
        '''复制SDK运行需要的dll文件'''
        current_dir = os.path.join(os.getcwd(),'export_SDK') 
        search_file.copy_files(save_path.SDK_exe_path,current_dir)   # 拷贝exe

        opencv_path = os.path.join(current_dir, 'vimo-inference-win64-cpp', 'opencv', 'x64', 'vc15', 'bin','opencv_world420.dll')  # opencv依赖路径
        search_file.copy_files(opencv_path, current_dir)  # 拷贝opencv依赖

        bin_path = os.path.join(current_dir, 'vimo-inference-win64-cpp', 'bin')  # bin目录下依赖路径
        search_file.copy_files(bin_path, current_dir)  # 拷贝bin下的依赖
        

    def run_SDK(img_path = None,project_name = None,moduleid = '2',json_path = './'):
        '''运行SDK'''
        current_dir = os.path.join(os.getcwd(),'export_SDK') 
        vimosln_path = os.path.join(current_dir,'model.vimosln')            
        command = f'cd {current_dir} & .\\test_executor_1023_1.exe --config {vimosln_path} --images {img_path} --name {moduleid} --output {json_path}'    
        result = subprocess.run(command, shell=True, capture_output=True, text=True)        
        if result.stdout:
            output = result.stdout  # 保存输出信息
            if 'Done' in output:
                output_file_path = project_name + '.txt'  # 设置保存输出的文本文件路径
                with open(output_file_path, "w") as output_file:
                    output_file.write(output)
        else:
            assert False,'SDK调用失败'

             
    def export_report():
        '''导出报告'''
        airtest_method.touch_button(light_control.report_button)
        airtest_method.touch_button(light_control.report_name)
        airtest_method.touch_button(light_control.ok_button)
        airtest_method.operate_sleep()
        airtest_method.touch_button(light_control.export_button) 
        if not airtest_method.check_exit(light_control.report_success,'FALSE',10) :
            assert False,'报告未导出成功'
        else:
            open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
    
    def template_file():
        '''点击文件按钮'''
        if not airtest_method.check_exit(light_control.template_file,'FALSE') :
            assert False,'未找到文件按钮'
        else:          
            airtest_method.touch_button(light_control.template_file)
            airtest_method.operate_sleep(2.0)

    def template_SDK():
        '''点击导出SDK按钮'''
        if not airtest_method.check_exit(light_control.template_SDK,'FALSE') :
            assert False,'未找到导出SDK按钮'
        else:          
            airtest_method.touch_button(light_control.template_SDK)
            airtest_method.touch_button(light_control.export_button)
            airtest_method.operate_sleep(60.0)

    def template_help():
        '''点击帮助按钮'''
        if not airtest_method.check_exit(light_control.template_help,'FALSE') :
            assert False,'未找到帮助按钮'
        else:
            airtest_method.touch_button(light_control.template_help)
      
    def template_close():
        '''点击关闭按钮'''
        if not airtest_method.check_exit(light_control.template_close,'FALSE') :
            assert False,'未找到关闭按钮'
        else:
            airtest_method.touch_button(light_control.template_close)
            airtest_method.operate_sleep(10.0)
 
    def user_guild():
        '''导出软件功能手册'''
        if not airtest_method.check_exit(light_control.user_guild,'FALSE') :
            assert False,'未找到软件功能手册'
        else:
            airtest_method.touch_button(light_control.user_guild)
            if not airtest_method.check_exit(light_control.user_success,'FALSE',10) :
                assert False,'软件功能手册未导出成功'
            else:
                open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")

    def operating_guild():
        '''导出软件操作手册'''
        if not airtest_method.check_exit(light_control.operating_guild,'FALSE') :
            assert False,'未找到软件操作手册'
        else:
            airtest_method.touch_button(light_control.operating_guild)
            if not airtest_method.check_exit(light_control.user_success,'FALSE',10) :
                assert False,'软件操作手册未导出成功'
            else:
                open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")

    def SDK_guild(type):
        '''导出SDK开发手册'''
        if not airtest_method.check_exit(light_control.SDK_guild,'FALSE') :
            assert False,'未找到SDK开发手册按钮'
        else:
            airtest_method.move_to((303,63),(338,161))
            if type == 'c++':
                airtest_method.touch_button(light_control.guild_c)
                if not airtest_method.check_exit(light_control.SDK_success,'FALSE',10) :
                    assert False,'c++SDK_开发手册未导出成功'
                else:
                    open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
            if type == 'csharp':
                airtest_method.touch_button(light_control.guild_csharp)
                if not airtest_method.check_exit(light_control.SDK_success,'FALSE',10) :
                    assert False,'csharp_SDK开发手册未导出成功'
                else:
                    open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
            if type == 'python':
                airtest_method.touch_button(light_control.guild_python)
                if not airtest_method.check_exit(light_control.SDK_success,'FALSE',10) :
                    assert False,'python_SDK开发手册未导出成功'
                else:
                    open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
  
    def home():
        '''home键'''
        if not airtest_method.check_exit(light_control.home_button,'FALSE') :
            assert False,'未找到home键'
        else:
            airtest_method.touch_button(light_control.home_button)

    def change_type():
        '''切换模型类型'''
        if not airtest_method.check_exit(light_control.change_type,'FALSE') :
            assert False,'未成功切换模型类型'
        else:
            airtest_method.touch_button(light_control.change_type)
  
    def template_quit():
        '''退出'''
        if not airtest_method.check_exit(light_control.template_quit,'FALSE') :
            assert False,'未成功退出'
        else:
            airtest_method.touch_button(light_control.template_quit)