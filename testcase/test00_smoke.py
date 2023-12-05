__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from pages.data_page import data
from pages.management_page import management
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from elements.public_control import control
from common.handle_log import do_log
from common.Airtest_method import airtest_method
from common.Base_method import search_file
import pytest
import allure
import os

auto_setup(__file__)

# @allure.title('五类算法冒烟')
# @pytest.mark.smoke
# def test_algorithm_smoke():
for item in save_path.project_list:
    #根据传入的item判断算法类型，找到相应的数据集
    if item ==save_path.seg:
        dataset = save_path.seg_dataset
        name = 'SEG'
    if item == save_path.cls:
        dataset = save_path.cls_dataset
        name = 'CLS'
    if item == save_path.det:
        dataset = save_path.det_dataset
        name = 'DET'
    if item == save_path.ocr:
        dataset = save_path.ocr_dataset
        name = 'OCR'
    if item == save_path.uad:
        dataset = save_path.uad_dataset
        name = 'UAD'
    if item == save_path.seqocr:
        dataset = save_path.seqocr_dataset
        name = 'SEQ'

current_dir = os.getcwd()
model_selection = [control.high_power,control.low_power]
color_mode = [0,control.gray_image]  #0为默认
scaling_selection = [control.equal_size,control.zidingyi_size]
input_size = ['512']

@allure.title('seq OCR算法冒烟')
@pytest.mark.smoke
def test_seq_OCR_smoke():      
        if name == 'SEQ':        #seq OCR算法仅有高性能模型类型                     
            for color in color_mode:
                with allure.step(f'{name}算法冒烟,使用{color}训练模型'):
                    for file in search_file.get_file(dataset):
                        management.create_project()       
                        project_name = management.input_name(name)  
                        management.create_model(item)

                        '''数据管理页面'''
                        file_path = str(os.path.join(dataset,file))
                        data.add_file(file_path)

                        '''图像标注页面'''
                        mark.image_label()
                        mark.auto_divide()

                        '''模型训练页面'''  
                        training.model_training()
                        training.add_card()
                        training.color_mode(color)

                        training.set_study()
                        training.star_training()

                        '''模型评估页面'''
                        assess.model_assess()
                        assess.assess_success()

                        '''调用SDK'''
                        assess.more_button()
                        assess.export_SDK(current_dir)
                        assess.unzip_SDK()
                        assess.copy_SDK_dll()
                        assess.run_SDK(file_path,project_name)

                        # '''导出模型'''
                        # assess.more_button()
                        # assess.export_model()

                        '''导出报告'''
                        assess.export_report()
                            
                        with allure.step(f'关闭方案'):
                            '''关闭方案'''
                            assess.template_file()
                            assess.template_close()

#         if name == 'UAD':  #无监督算法有三种模型类型
#             model_selection = [control.modelB,control.modelA_low_power,control.modelA_high_power]
#             for file in search_file.get_file(dataset):
#                 for type in model_selection:
#                     with allure.step(f'{name}算法冒烟'):
#                         '''方案管理页面'''
#                         management.create_project()       
#                         project_name = management.input_name(name)  
#                         management.create_model(item)

#                         '''数据管理页面'''
#                         file_path = str(os.path.join(dataset,file))
#                         data.add_file(file_path)

#                         '''图像标注页面'''
#                         mark.image_label()
#                         mark.auto_divide()

#                         '''模型训练页面'''  
#                         training.model_training()
#                         training.add_card()
#                         training.uad_choice_model()
#                         airtest_method.touch_button(type) #选择模型类型
#                         if not airtest_method.check_exit(type,'FALSE',5) :      
#                             assert False,'模型类型切换失败'
#                         else:
#                             do_log.info("模型切换成功")
#                         training.star_training()

#                         '''模型评估页面'''
#                         assess.model_assess()
#                         if not airtest_method.check_exit(control.infering_finished,'FALSE',360000) :
#                             assert False,'评估未完成'
#                         else:
#                             airtest_method.operate_sleep()

#                         '''调用SDK'''
#                         assess.more_button()
#                         assess.export_SDK(current_dir)
#                         assess.unzip_SDK()
#                         assess.copy_SDK_dll()
#                         assess.run_SDK(file_path,project_name)

#                         # '''导出模型'''
#                         # assess.more_button()
#                         # assess.export_model()

#                         '''导出报告'''
#                         assess.export_report()

#                         with allure.step(f'关闭方案'):    
#                             '''关闭方案'''
#                             assess.template_file()
#                             assess.template_close()
#         if name == 'OCR' or name == 'SEG' or name == 'DET' or name == 'CLS':
#             model_selection = [control.low_power,control.high_power]      #模型类型：高精度/低功耗   
#             for file in search_file.get_file(dataset):   
#                 for type in model_selection:
#                     with allure.step(f'{name}算法冒烟'):
#                         '''方案管理页面'''
#                         management.create_project()       
#                         project_name = management.input_name(name)  
#                         management.create_model(item)

#                         '''数据管理页面'''
#                         file_path = str(os.path.join(dataset,file))
#                         data.add_file(file_path)

#                         '''图像标注页面'''
#                         mark.image_label()
#                         mark.auto_divide()

#                         '''模型训练页面'''  
#                         training.model_training()

#                         training.add_card()
#                         training.choice_model()
#                         airtest_method.touch_button(type) #选择模型类型
#                         if not airtest_method.check_exit(type,'FALSE',5) :      
#                             assert False,'模型类型切换失败'
#                         else:
#                             do_log.info("模型切换成功")

#                         training.set_study()                            
#                         training.star_training()

#                         '''模型评估页面'''
#                         assess.model_assess()
#                         if not airtest_method.check_exit(control.infering_finished,'FALSE',360000) :
#                             assert False,'评估未完成'
#                         else:
#                             airtest_method.operate_sleep()

#                         '''调用SDK'''
#                         assess.more_button()
#                         assess.export_SDK(current_dir)
#                         assess.unzip_SDK()
#                         assess.copy_SDK_dll()
#                         assess.run_SDK(file_path,project_name)

#                         # '''导出模型'''
#                         # assess.more_button()
#                         # assess.export_model()

#                         '''导出报告'''
#                         assess.export_report()

#                         with allure.step(f'关闭方案'):    
#                             '''关闭方案'''
#                             assess.template_file()
#                             assess.template_close()

# if name == 'DET' or name == 'CLS':
#     model_selection = [control.low_power,control.high_power]      #模型类型：高精度/低功耗   
#     for file in search_file.get_file(dataset):   
#         for type in model_selection:
#             with allure.step(f'{name}算法冒烟'):
#                 '''方案管理页面'''
#                 management.create_project()       
#                 project_name = management.input_name(name)  
#                 management.create_model(item)

#                 '''数据管理页面'''
#                 file_path = str(os.path.join(dataset,file))
#                 data.add_file(file_path)

#                 '''图像标注页面'''
#                 mark.image_label()
#                 mark.auto_divide()

#                 '''模型训练页面'''  
#                 training.model_training()

#                 training.add_card()
#                 training.choice_model()
#                 airtest_method.touch_button(type) #选择模型类型
#                 if not airtest_method.check_exit(type,'FALSE',5) :      
#                     assert False,'模型类型切换失败'
#                 else:
#                     do_log.info("模型切换成功")

#                 training.set_study()                            
#                 training.star_training()

#                 '''模型评估页面'''
#                 assess.model_assess()
#                 if not airtest_method.check_exit(control.infering_finished,'FALSE',360000) :
#                     assert False,'评估未完成'
#                 else:
#                     airtest_method.operate_sleep()

#                 '''调用SDK'''
#                 assess.more_button()
#                 assess.export_SDK(current_dir)
#                 assess.unzip_SDK()
#                 assess.copy_SDK_dll()
#                 assess.run_SDK(file_path,project_name)

#                 # '''导出模型'''
#                 # assess.more_button()
#                 # assess.export_model()

#                 '''导出报告'''
#                 assess.export_report()

#                 with allure.step(f'关闭方案'):    
#                     '''关闭方案'''
#                     assess.template_file()
#                     assess.template_close()

@allure.title('退出软件')
@pytest.mark.smoke
def test_quit():
    with allure.step(f'点击文件按钮'): 
       assess.template_file()
    with allure.step(f'点击退出按钮'):
        assess.template_quit()       