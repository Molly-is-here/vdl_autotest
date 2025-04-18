__author__ = "yunliu"
import pytest
import allure
import os
from elements.elements_path import save_path
from pages.data_page import data
from common.handle_log import do_log

# 常量定义
COLOR = 'light'

@allure.feature('数据管理页面')
class TestData:
    """数据管理页面测试类"""

    @allure.story('标签管理功能')
    @allure.title('添加标签')
    @pytest.mark.skip('导入图片时再新增标签')
    def test_add_tag(self, content: str):   
        """添加标签"""
        with allure.step(f'添加标签: {content}'):
            data.add_tag(content)
        do_log.info('成功添加标签,用例执行成功')

    @allure.story('数据导入功能')
    @allure.title('通过下划线导入图像')
    @pytest.mark.smoke
    def test_add_image_underscore(self):    
        """测试下划线导入图像功能"""
        with allure.step('点击下划线导入图像'):
            file_path = os.path.join(save_path.dataset_path, '导入mask', 'images')
            data.add_image_underscore(file_path)  
        with allure.step('添加标签'):
            self.test_add_tag('自动化标签')
        do_log.info('成功导入图像,用例执行成功')

    @allure.story('数据导入功能')
    @allure.title('导入图像')
    @pytest.mark.smoke
    def test_add_image(self):   
        """测试导入图像功能"""
        with allure.step('点击导入图像按钮'):
            file_path = os.path.join(save_path.dataset_path, '导入mask', 'images')
            data.add_image(file_path, COLOR)
        do_log.info('成功导入图像,用例执行成功')
            
    @allure.story('数据导入功能')
    @allure.title('导入标注')
    @pytest.mark.smoke
    def test_add_label(self):
        """测试导入标注功能"""
        with allure.step('点击导入标注按钮'):
            file_path = os.path.join(save_path.dataset_path, '导入mask', '64个mask')
            data.add_label(file_path, COLOR)
        do_log.info('成功导入标注,用例执行成功')

    @allure.story('数据导入功能')
    @allure.title('导入图像+标注')
    @pytest.mark.skip("导入图像+标注放到增量训练过程")
    def test_add_file(self):
        """测试导入图像和标注文件夹功能"""
        with allure.step('点击导入文件夹按钮'):
            file_path = os.path.join(save_path.dataset_path, '导入mask', '导入image和label')
            data.add_file(file_path)
        do_log.info('成功导入图像+标注,用例执行成功')
    
    @allure.story('数据筛选功能')
    @allure.title('数据管理页面筛选框组合筛选')
    @pytest.mark.smoke
    def test_search_image(self):
        """测试数据筛选功能"""
        with allure.step('混合筛选'):
            data.mixed_filtering('0')
        do_log.info('组合筛选生效,用例执行成功')








