__author__ = "yunliu"
import pytest
import allure
from pages.marking_page import mark
from common.handle_log import do_log

# 常量定义
COLOR = 'light'

@allure.feature('图像标注页面')
class TestLabel:
    """图像标注页面测试类"""

    @allure.story('页面导航功能')
    @allure.title('切换至图像标注页面')
    @pytest.mark.smoke
    def test_image_label(self):
        """测试切换到图像标注页面功能"""
        with allure.step('点击图像标注tab按钮'):
            mark.image_label(COLOR)  
        do_log.info('图像标注页面成功切换,用例执行成功')

    @allure.story('数据管理功能')
    @allure.title('数据划分')
    @pytest.mark.smoke
    def test_auto_divide(self):
        """测试自动数据划分功能"""
        with allure.step('点击数据划分按钮'):
            mark.auto_divide(COLOR)
        do_log.info('自动划分成功,用例执行成功')
