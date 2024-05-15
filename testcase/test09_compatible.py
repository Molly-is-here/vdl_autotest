__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from pages.management_page import management
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from elements.public_control import control
from common.Airtest_method import airtest_method
from tools.compatible_html import create_html_file
from pathlib import Path
import pytest
import allure

auto_setup(__file__)

@allure.title('六类算法对比测试')
@pytest.mark.smoke
def test_compatible_smoke():
   for item in save_path.project_list:
        dataset_list = []
        #根据传入的item判断算法类型，找到相应的数据集        
        if item ==save_path.seg:
            name = 'SEG'
            folder_path = Path(save_path.compare_project[2])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[2],folder_name) 
                    dataset_list.append(dataset)   
        if item == save_path.cls:
            name = 'CLS'
            folder_path = Path(save_path.compare_project[0])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[0],folder_name) 
                    dataset_list.append(dataset)   
        if item == save_path.det:
            name = 'DET'
            folder_path = Path(save_path.compare_project[1])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[1],folder_name)
                    dataset_list.append(dataset)
        if item == save_path.ocr:
            name = 'OCR'
            folder_path = Path(save_path.compare_project[3])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[3],folder_name) 
                    dataset_list.append(dataset)   
        if item == save_path.uad:
            name = 'UAD'
            folder_path = Path(save_path.compare_project[4])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[4],folder_name) 
                    dataset_list.append(dataset)  
        if item == save_path.seqocr:
            name = 'SEQOCR'
            folder_path = Path(save_path.compare_project[5])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[5],folder_name) 
                    dataset_list.append(dataset)  

        for project_path in dataset_list:
            dataset_name = os.path.basename(project_path)
            with allure.step(f'当前运行{dataset_name}方案'):
                '''方案管理页面'''
                management.open_project(project_path)
                management.click_project()

                '''图像标注页面'''
                mark.image_label()

                '''模型训练页面'''
                training.model_training()
                if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'SEG' or name == 'SEQOCR': 
                    training.add_card()
                    training.set_study()
                    training.mouse_move()
                    training.zidingyi_button()
                    # training.cut_benchsize()
                else:
                    training.add_card()

                training.star_training()    #开始训练
                training.training_success(dataset_name)    #判断是否训练完成

                '''模型评估页面'''
                assess.model_assess()
                if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'SEG' or name == 'SEQOCR':
                    assess.assess_done() 
                else:
                    if not airtest_method.check_exit(control.sensitive_area,'FALSE',360000) :
                        assert False,'评估未完成'

                airtest_method.operate_sleep(10.0)
                ct_screenshot = os.path.join(save_path.base_path, f"{dataset_name}评估完成.png") 
                airtest_method.screenshot(ct_screenshot)
                create_html_file("V0.9.0",dataset_name,ct_screenshot)


                '''HOME键返回方案管理页面'''
                assess.home()
