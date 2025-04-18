__author__ = "yunliu"
import pytest
import allure
import os
from common.handle_log import do_log
from pages.assess_page import assess

# 常量定义
COLOR = 'light'

@allure.feature('模型评估页面')
class TestEvaluate:
    """模型评估页面测试类"""

    @allure.story('页面导航')
    @allure.title('切换至模型评估页面')
    @pytest.mark.smoke
    def test_assess_page(self):
        """测试切换到模型评估页面功能"""
        with allure.step('点击模型评估tab按钮'):
            do_log.info('开始切换到模型评估页面')
            assess.model_assess(COLOR)
            do_log.info('模型评估页面成功切换,用例执行成功')

    @allure.story('模型导出')
    @allure.title('导出模型')
    @pytest.mark.smoke
    def test_export_model(self):
        """测试导出模型功能"""
        with allure.step('等待评估完成'):
            do_log.info('开始等待评估完成...')
            assess.assess_success(COLOR)
        
        with allure.step('点击更多按钮'):
            assess.more_button()
        
        with allure.step('选择导出模型'):
            assess.export_model()
            do_log.info('模型成功导出,用例执行成功')

    @allure.story('报告导出')
    @allure.title('导出报告')
    @pytest.mark.smoke
    def test_export_report(self):
        """测试导出报告功能"""
        with allure.step('点击导出报告按钮'):
            assess.export_report()
            do_log.info('报告成功导出,用例执行成功')

