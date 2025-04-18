__author__ = "yunliu"
import pytest
import allure
import os
from common.Airtest_method import airtest_method
from pages.assess_page import assess
from common.handle_log import do_log

# 常量定义
SETTING_FILE = r"D:\ViMo-Deeplearning\setting.ini"
# 高级设置参数
ADVANCED_SETTINGS = {
    'Worker': 4,
    'AutoMLIter': 0.6,
    'MaxDetect': 20
}

@allure.feature('菜单栏')
class TestMenu:
    """菜单栏测试类"""

    @allure.story('文件操作')
    @allure.title('关闭方案')
    @pytest.mark.smoke
    def test_template_close(self):
        """测试关闭方案功能"""
        airtest_method.operate_sleep(5.0)
        with allure.step('点击文件按钮'):
            assess.template_file()
        with allure.step('点击关闭方案'):
            assess.template_close()
            airtest_method.operate_sleep()
        do_log.info('关闭方案成功，用例执行成功')

    @allure.story('文件操作')
    @allure.title('导出SDK')
    @pytest.mark.smoke
    def test_template_SDK(self):
        """测试导出SDK功能"""
        with allure.step('点击文件按钮'):
            assess.template_file()
        with allure.step('导出SDK'):
            assess.template_SDK()
        do_log.info('导出SDK成功，用例执行成功')

    @allure.story('设置功能')
    @allure.title('高级设置')
    def test_template_advanced(self):
        """测试高级设置功能"""
        with allure.step('点击设置按钮'):
            assess.template_setting()
        with allure.step('点击高级设置'):
            assess.template_advanced(
                ADVANCED_SETTINGS['Worker'],
                ADVANCED_SETTINGS['AutoMLIter'],
                ADVANCED_SETTINGS['MaxDetect']
            )
        with allure.step('校验高级设置是否生效'):
            self._verify_advanced_settings()
            assess.template_setting()
        do_log.info('高级设置生效，用例执行成功')

    def _verify_advanced_settings(self):
        """验证高级设置是否生效"""
        try:
            if not os.path.exists(SETTING_FILE):
                do_log.error(f'设置文件不存在: {SETTING_FILE}')
                pytest.fail(f'设置文件不存在: {SETTING_FILE}')

            with open(SETTING_FILE, 'r', encoding='utf-8') as file:
                settings = file.read()
                
                # 检查每个设置项
                for key, value in ADVANCED_SETTINGS.items():
                    # 构建可能的设置格式
                    possible_formats = [
                        f'{key}={value}',  # 标准格式
                        f'{key} = {value}',  # 带空格的格式
                        f'{key.capitalize()}={value}',  # 首字母大写
                        f'{key.upper()}={value}'  # 全大写
                    ]
                    
                    # 检查是否匹配任一格式
                    if not any(format_str in settings for format_str in possible_formats):
                        error_msg = f'高级设置未生效: {key}={value}'
                        do_log.error(error_msg)
                        pytest.fail(error_msg)
                        
                do_log.info('所有高级设置验证通过')
                
        except UnicodeDecodeError:
            error_msg = f'设置文件编码错误: {SETTING_FILE}'
            do_log.error(error_msg)
            pytest.fail(error_msg)
        except Exception as e:
            error_msg = f'验证高级设置时发生错误: {str(e)}'
            do_log.error(error_msg)
            pytest.fail(error_msg)

    @allure.story('帮助功能')
    @allure.title('导出软件功能手册')
    @pytest.mark.smoke
    def test_user_guild(self):
        """测试导出软件功能手册功能"""
        with allure.step('点击帮助按钮'):
            assess.template_help()
        with allure.step('导出软件功能手册'):
            assess.user_guild()
        do_log.info('软件功能手册导出成功，用例执行成功')

    @allure.story('帮助功能')
    @allure.title('导出软件操作手册')
    @pytest.mark.smoke
    def test_operating_guild(self):
        """测试导出软件操作手册功能"""
        with allure.step('点击帮助按钮'):
            assess.template_help()
        with allure.step('导出软件操作手册'):
            assess.operating_guild()
        do_log.info('软件操作手册导出成功，用例执行成功')

    @allure.story('帮助功能')
    @allure.title('导出软件使用SDK开发手册')
    @pytest.mark.smoke
    def test_SDK_guild(self):
        """测试导出SDK开发手册功能"""
        with allure.step('点击帮助按钮'):
            assess.template_help()
        with allure.step('导出C++ SDK开发手册'):
            assess.SDK_guild('c++')
        with allure.step('导出Csharp SDK开发手册'):
            assess.SDK_guild('csharp')
        with allure.step('导出Python SDK开发手册'):
            assess.SDK_guild('python')
            assess.template_help()
        do_log.info('SDK开发手册导出成功，用例执行成功')

    