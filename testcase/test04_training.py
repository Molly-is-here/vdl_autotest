__author__ = "yunliu"
import pytest
import allure
import os
from common.Airtest_method import airtest_method
from elements.public_control import light_control
from common.handle_log import do_log
from pages.data_page import data
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from elements.elements_path import save_path

# 常量定义
COLOR = 'light'
PROJECT_NAME_FILE = 'project_name.txt'
MODEL_SELECTION = [light_control.high_power, light_control.low_power]
SCALING_SELECTION = [light_control.equal_size, light_control.zidingyi_size]
INPUT_SIZE = ['512']
TRAINING_TIMEOUT = 360000  # 训练超时时间（毫秒）
SLEEP_TIME = 2.0  # 等待时间（秒）

@allure.feature('模型训练页面')
class TestTraining:
    """模型训练页面测试类"""  
    def import_image_and_label(self):
        """导入图像和标注文件夹"""
        with allure.step('点击导入文件夹按钮'):
            file_path = os.path.join(save_path.dataset_path, '导入mask', '导入image和label')
            data.add_file(file_path)
        do_log.info('成功导入图像+标注')

    @allure.story('模型训练功能')
    @allure.title('切换至模型训练页面')
    @pytest.mark.smoke
    def test_training_page(self):
        """测试切换到模型训练页面功能"""
        with allure.step('点击模型训练tab按钮'):
            do_log.info('开始切换到模型训练页面')
            training.model_training(COLOR)
        do_log.info('模型训练页面成功切换,用例执行成功')
        
    @allure.story('训练卡片管理')
    @allure.title('新建训练小卡片')
    @pytest.mark.smoke
    def test_add_card(self):
        """测试新建训练卡片功能"""
        with allure.step('点击新的训练按钮'):
            training.add_card(COLOR)
        do_log.info('成功新建卡片,用例执行成功')

    @allure.story('训练卡片管理')
    @allure.title('重命名训练小卡片')
    @pytest.mark.smoke
    def test_rename(self):    
        """测试重命名训练卡片功能"""
        with allure.step('重命名'):
            input_name = '自動化創建的card'
            training.renamed_card(input_name, (135, 220))
        do_log.info('卡片成功重命名,用例执行成功')

    @allure.story('训练卡片管理')
    @allure.title('修改备注')
    @pytest.mark.smoke
    def test_edit_comment(self):
        """测试修改卡片备注功能"""
        with allure.step('修改备注'):
            input_comment = 'have_a_nice_day*@▽@*耶耶'
            training.edit_comment(input_comment)
        do_log.info('卡片备注成功修改,用例执行成功')

    @allure.story('训练卡片管理')
    @allure.title('复制训练小卡片')
    @pytest.mark.smoke
    def test_copy(self):
        """测试复制训练卡片功能"""
        with allure.step('点击复制按钮'):
            training.copy_card()
        do_log.info('成功复制卡片,用例执行成功')
            
    @allure.story('训练卡片管理')
    @allure.title('删除卡片')
    @pytest.mark.smoke
    def test_delete(self):  
        """测试删除训练卡片功能"""
        with allure.step('点击删除卡片按钮'):
            training.delete_card()
        do_log.info('成功删除卡片，用例执行成功')

    @allure.story('模型训练功能')
    @allure.title('设置为模板并开启训练')
    @pytest.mark.smoke
    def test_set_template(self):
        """测试设置模板并训练功能"""
        with allure.step('设置训练参数'):
            training.set_study('30', COLOR)           
            training.cut_benchsize(COLOR)
        with allure.step('训练参数设置为模板'):
            training.set_template()
        with allure.step('使用模版开启训练'):
            airtest_method.touch_button(light_control.add_card)
            airtest_method.touch_button(light_control.create_using_template)
        with allure.step('点击开始训练'):
            training.star_training(COLOR)
        with allure.step('判断是否训练成功'):
            with open(PROJECT_NAME_FILE, 'r', encoding='utf-8') as file:
                content = file.read()
                airtest_method.operate_sleep()
            path = os.path.join(save_path.project_save_path, content, "output", "4", "vimo-train.log")
            training.training_success(path, content) 
        with allure.step('判断是否评估成功'):  
            assess.model_assess(COLOR)
            if not airtest_method.check_exit(light_control.infering_finished, 'FALSE', TRAINING_TIMEOUT):
                pytest.fail('评估未完成')
            airtest_method.operate_sleep()
        do_log.info('模型训练成功，用例执行成功')

    @allure.story('自动标注功能')
    @allure.title('分割算法自动标注')
    @pytest.mark.smoke
    def test_seg_auto_marking(self):
        """测试分割算法自动标注功能"""
        with allure.step('切换回标注页面'):
            mark.image_label(COLOR)
        with allure.step('点击分割算法自动标注按钮'):
            airtest_method.key_event('{DOWN}')
            mark.auto_marking()
        do_log.info('分割算法自动标注完成')

    @allure.story('增量训练功能')
    @allure.title('增量训练')
    @pytest.mark.smoke
    def test_add_training(self):  
        """测试增量训练功能"""
        with allure.step('选择增量训练'): 
            training.model_training(COLOR)
            training.add_training()
            airtest_method.operate_sleep()
        with allure.step('返回数据管理页面'):
            data.data_management_page()
        with allure.step('通过导入文件夹导入图像+标注'):
            self.import_image_and_label()
        with allure.step('图像标注页面重新划分数据集'):
            mark.image_label(COLOR)
            mark.auto_divide(COLOR)
        with allure.step('返回模型训练页面开始增量训练'):
            training.model_training(COLOR)
        with allure.step('点击开始训练'):
            training.star_training(COLOR)
        with allure.step('确认开启增量训练'):
            airtest_method.touch_button(light_control.training_okbutton)
        with allure.step('判断是否训练成功'):
            with open(PROJECT_NAME_FILE, 'r', encoding='utf-8') as file:
                content = file.read()
                airtest_method.operate_sleep()
            path = os.path.join(save_path.project_save_path, content, "output", "5", "vimo-train.log")
            training.training_success(path, content) 
        with allure.step('判断是否评估成功'):  
            assess.model_assess(COLOR)
            if not airtest_method.check_exit(light_control.infering_finished, 'FALSE', TRAINING_TIMEOUT):
                pytest.fail('评估未完成')
            airtest_method.operate_sleep()
            do_log.info('模型增量训练成功，用例执行成功')

    @allure.story('标签管理功能')
    @allure.title('特征置为背景')
    @pytest.mark.smoke
    def test_set_background(self): 
        """测试将特征设置为背景功能"""
        with allure.step('切换回标注页面'):
            mark.image_label(COLOR)
        with allure.step('特征1置为背景'):
            mark.set_background((1701, 507))
        with allure.step('切换至模型训练页面'):
            airtest_method.operate_sleep(SLEEP_TIME)
            training.model_training(COLOR)
        with allure.step('使用模版开启训练'):
            airtest_method.touch_button(light_control.add_card)
            airtest_method.touch_button(light_control.create_using_template)
            training.renamed_card('特征1置为背景', (135, 220))
        with allure.step('点击开始训练'):
            training.star_training(COLOR)
        with allure.step('判断是否训练成功'):
            with open(PROJECT_NAME_FILE, 'r', encoding='utf-8') as file:
                content = file.read()
            path = os.path.join(save_path.project_save_path, content, "output", "6", "vimo-train.log")
            training.training_success(path, content) 
        with allure.step('判断是否评估成功'):  
            training.review_assess()
            if not airtest_method.check_exit(light_control.infering_finished, 'FALSE', TRAINING_TIMEOUT):
                pytest.fail('评估未完成')
            airtest_method.operate_sleep()
        do_log.info('模型训练成功，用例执行成功')

    @allure.story('标签管理功能')
    @allure.title('标签硬合并')
    @pytest.mark.smoke
    def test_hard_merge_label(self):
        """测试标签硬合并功能"""
        with allure.step('切换回标注页面'):
            mark.image_label(COLOR)
        with allure.step('点击标签合并'):
            mark.hard_merge_label((1623, 557), '3')
        with allure.step('切换至模型训练页面'):
            airtest_method.operate_sleep(SLEEP_TIME)
            training.model_training(COLOR)
        with allure.step('使用模版开启训练'):
            airtest_method.touch_button(light_control.add_card)
            airtest_method.touch_button(light_control.create_using_template)
            training.renamed_card('特征2标签硬合并', (135, 220))
        with allure.step('点击开始训练'):
            training.star_training(COLOR)
        with allure.step('判断是否训练成功'):
            with open(PROJECT_NAME_FILE, 'r', encoding='utf-8') as file:
                content = file.read()
            path = os.path.join(save_path.project_save_path, content, "output", "7", "vimo-train.log")
            training.training_success(path, content) 
        with allure.step('判断是否评估成功'):  
            training.review_assess()
            if not airtest_method.check_exit(light_control.infering_finished, 'FALSE', TRAINING_TIMEOUT):
                pytest.fail('评估未完成')
            airtest_method.operate_sleep()
        do_log.info('模型训练成功，用例执行成功')

    @allure.story('标签管理功能')
    @allure.title('标签软合并')
    @pytest.mark.smoke
    def test_soft_merge_label(self):
        """测试标签软合并功能"""
        with allure.step('切换回标注页面'):
            mark.image_label(COLOR)
        with allure.step('标签3软合并至标签4'):
            mark.soft_merge_label((1688, 560), (1688, 605))
        with allure.step('切换至模型训练页面'):
            airtest_method.operate_sleep(SLEEP_TIME)
            training.model_training(COLOR)
        with allure.step('使用模版开启训练'):
            airtest_method.touch_button(light_control.add_card)
            airtest_method.touch_button(light_control.create_using_template)
            training.renamed_card('特征3软合并至特征4', (135, 220))
        with allure.step('点击开始训练'):
            training.star_training(COLOR)
        with allure.step('判断是否训练成功'):
            with open(PROJECT_NAME_FILE, 'r', encoding='utf-8') as file:
                content = file.read()
            path = os.path.join(save_path.project_save_path, content, "output", "8", "vimo-train.log")
            training.training_success(path, content) 
        with allure.step('判断是否评估成功'):  
            training.review_assess()
            if not airtest_method.check_exit(light_control.infering_finished, 'FALSE', TRAINING_TIMEOUT):
                pytest.fail('评估未完成')
            airtest_method.operate_sleep()
        do_log.info('模型训练成功，用例执行成功')

    @allure.story('标签管理功能')
    @allure.title('ignore标签')
    @pytest.mark.smoke
    def test_ignore_label(self):
        """测试将标签设置为ignore功能"""
        with allure.step('切换回标注页面'):
            mark.image_label(COLOR)
        with allure.step('把标签3移动至ignore'):
            mark.soft_merge_label((1706, 606), (1717, 464))
        with allure.step('切换至模型训练页面'):
            airtest_method.operate_sleep(SLEEP_TIME)
            training.model_training(COLOR)
        with allure.step('使用模版开启训练'):
            airtest_method.touch_button(light_control.add_card)
            airtest_method.touch_button(light_control.create_using_template)
            training.renamed_card('特征3软合并至ignore', (135, 220))
        with allure.step('点击开始训练'):
            training.star_training(COLOR)
        with allure.step('判断是否训练成功'):
            with open(PROJECT_NAME_FILE, 'r', encoding='utf-8') as file:
                content = file.read()
            path = os.path.join(save_path.project_save_path, content, "output", "9", "vimo-train.log")
            training.training_success(path, content) 
        with allure.step('判断是否评估成功'):  
            training.review_assess()
            if not airtest_method.check_exit(light_control.infering_finished, 'FALSE', TRAINING_TIMEOUT):
                pytest.fail('评估未完成')
            airtest_method.operate_sleep()
        do_log.info('模型训练成功，用例执行成功')
    
    
    









    













