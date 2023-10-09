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
from tools.monitoring import *
from common.Base_method import search_file

auto_setup(__file__)

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

    if name == 'OCR':        #OCR算法仅有高性能模型类型
        for file in search_file.get_file(dataset):
            management.create_project()       
            management.input_name(name)  
            management.create_model(item)
            do_log.info(f'成功创建{name}方案,用例执行成功')

            '''数据管理页面'''
            data.add_file(dataset,file)
            do_log.info('成功上传数据集,用例执行成功')

            '''图像标注页面'''
            mark.image_label()
            mark.auto_divide()
            do_log.info('成功划分数据集,用例执行成功')

            '''模型训练页面'''  
            training.model_training()
            training.add_card()
            training.set_study()
            training.star_training()

            '''模型评估页面'''
            assess.model_assess()
            assess.assess_success() 

            '''导出模型'''
            assess.more_button()
            assess.export_model()

            '''导出报告'''
            # assess.export_report()
            # airtest_method.operate_sleep(5.0)
            # open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
                
            '''点击home页面切换方案'''
            airtest_method.touch_button(control.home_button)
            do_log.info(f'{type}训练成功，用例执行成功')


    model_selection = [control.low_power,control.high_power]      #模型类型：高精度/低功耗     
    for file in search_file.get_file(dataset):   
        for type in model_selection:
            '''方案管理页面'''
            management.create_project()       
            management.input_name(name)  
            management.create_model(item)
            do_log.info(f'成功创建{name}方案,用例执行成功')

            '''数据管理页面'''
            data.add_file(dataset,file)
            do_log.info('成功上传数据集,用例执行成功')

            '''图像标注页面'''
            mark.image_label()
            mark.auto_divide()
            do_log.info('成功划分数据集,用例执行成功')

            '''模型训练页面'''  
            training.model_training()

            training.add_card()
            training.choice_model()
            airtest_method.touch_button(type) #选择模型类型
            if not airtest_method.check_exit(type,'FALSE',5) : 
                do_log.error('模型类型切换失败，用例执行失败')       
                assert False,'模型类型切换失败'
            do_log.info('成功切换模型类型,用例执行成功')

            if name == 'CLS' or name == 'DET' or name == 'SEG':   #分类/检测/分割可以设置学习次数
                training.set_study()

            training.star_training()

            '''模型评估页面'''
            assess.model_assess()
            assess.assess_success() 

            '''导出模型'''
            assess.more_button()
            assess.export_model()

            '''导出报告'''
            # assess.export_report()
            # airtest_method.operate_sleep(5.0)
            # open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
                
            '''点击home页面切换方案'''
            airtest_method.touch_button(control.home_button)
            do_log.info(f'{type}训练成功，用例执行成功')

            