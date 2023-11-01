__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from pages.management_page import management
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from elements.public_control import control
from common.handle_log import do_log
from common.Airtest_method import airtest_method
import pytest
import allure

auto_setup(__file__)

@allure.title('五类算法兼容性测试')
@pytest.mark.smoke
def test_compatible_smoke():
   for item in save_path.project_list:
        #根据传入的item判断算法类型，找到相应的数据集
        if item ==save_path.seg:
            dataset = save_path.seg_project
            name = 'SEG'
        if item == save_path.cls:
            dataset = save_path.cls_project
            name = 'CLS'
        if item == save_path.det:
            dataset = save_path.det_project
            name = 'DET'
        if item == save_path.ocr:
            dataset = save_path.ocr_project
            name = 'OCR'
        if item == save_path.uad:
            dataset = save_path.uad_project
            name = 'UAD'

        with allure.step(f'当前运行{name}算法方案'):
            '''方案管理页面'''
            management.open_project(dataset)
            management.click_project()

            '''图像标注页面'''
            mark.image_label()

            '''模型训练页面'''
            training.model_training()
            if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'SEG': 
                training.add_card()
                training.set_study()
                training.mouse_move()
                training.zidingyi_button()
                training.cut_benchsize()
            else:
                training.add_card()

            training.star_training()    #开始训练
            training.review_assess(name)    #判断是否训练完成

            '''模型评估页面'''
            assess.model_assess()
            if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'SEG':
                assess.assess_success() 
            else:
                if not airtest_method.check_exit(control.confusion_matrix,'FALSE',360000) :
                    assert False,'评估未完成'
                else:
                    airtest_method.operate_sleep()

            '''HOME键返回方案管理页面'''
            assess.home()
