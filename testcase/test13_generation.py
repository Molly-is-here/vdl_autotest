__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from pages.management_page import management
from pages.data_page import data
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from common.Airtest_method import airtest_method
from tools.docqq import *
import pytest
import allure

# 常量定义
COLOR = 'light'
LEARNING_TIMES = '1'
PROJECT_NAME = '缺陷生成测试'

def setup_generation_project():
    """设置缺陷生成项目的基础配置"""
    # 导入预置模型
    assess.import_generation_model()
    
    # 创建项目
    management.create_project(COLOR)
    management.input_name(PROJECT_NAME, COLOR)
    management.create_model(save_path.generation)
    
    # 导入数据集
    data.data_management_page()
    data.add_file(save_path.generation_dataset)
    
    # 标注和划分训练集
    mark.image_label(COLOR)
    mark.train_set()

def train_generation_model():
    """训练缺陷生成模型"""
    training.model_training(COLOR)
    training.add_card(COLOR)
    training.generation_set_study(LEARNING_TIMES)
    training.star_training(COLOR)
    airtest_method.operate_sleep(5.0)
    training.stop_training()

@allure.title('缺陷生成功能测试')
@pytest.mark.smoke
def test_generation_page():
    """测试缺陷生成功能的完整流程"""
    with allure.step('设置缺陷生成项目'):
        setup_generation_project()
    
    with allure.step('训练缺陷生成模型'):
        train_generation_model()
               
    