__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from pages.management_page import management
from pages.data_page import data
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from elements.public_control import light_control
from common.Airtest_method import airtest_method
from pages.open_sofrware import open_Software
from tools.docqq import *
from pathlib import Path
import pytest
import allure

color = 'light'
learning_times  = '1'
@allure.title('缺陷生成功能测试')
@pytest.mark.smoke
def test_generation_page():
    with allure.step(f'导入缺陷生成预置模型'):
        assess.import_generation_model()
    with allure.step(f'创建缺陷生成方案'):
        management.create_project(color)
        management.input_name('缺陷生成lalala',color)
        management.create_model(save_path.generation)
    with allure.step(f'导入数据集'):
        data.data_management_page()
        data.add_file(save_path.generation_dataset)
    with allure.step(f'划分为训练集'):
        mark.image_label(color)
        mark.train_set()
    with allure.step(f'切换到训练页面'):
        training.model_training(color)
        training.add_card(color)
        training.generation_set_study(learning_times)                         
        training.star_training(color)
        airtest_method.operate_sleep(5.0)
        training.stop_training()
               
    