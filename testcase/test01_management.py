__author__ = "yunliu"
import pytest
import allure
import os
from pages.management_page import management
from common.Airtest_method import airtest_method
from elements.public_control import light_control
from common.handle_log import do_log
from tools.ocr import ocr_region

# 常量定义
COLOR = 'light'
PROJECT_NAME_FILE = 'project_name.txt'

@pytest.fixture(scope="module")
def setup_teardown():
    """测试前置和后置处理"""
    # 前置处理
    yield
    # 后置处理
    if os.path.exists(PROJECT_NAME_FILE):
        os.remove(PROJECT_NAME_FILE)

@allure.feature('方案管理页面')
class TestManagement:
    """方案管理页面测试类"""
    @allure.story('方案创建功能')
    @allure.title('点击新建方案')
    @pytest.mark.smoke
    def test_create_proj(self):   
        """测试新建方案按钮功能"""
        with allure.step('点击新建方案按钮'):
            management.create_project(COLOR)
        do_log.info('成功点击新建方案按钮,用例执行成功')

    @allure.story('方案创建功能')
    @allure.title('编辑框输入不同字符创建方案')
    @pytest.mark.parametrize('project_name,expected_result', [ 
        ('1', False)
    ])
    @pytest.mark.smoke
    def test_input_name(self, project_name: str, expected_result: bool):
        """测试输入字符的异常情况"""
        with allure.step(f'输入项目名称: {project_name}'):
            management.input_name(project_name, COLOR)
        with allure.step('点击创建按钮'):
            management.create_success(COLOR)
        with allure.step('校验验证结果'):
            airtest_method.hover((993, 353))
            has_error = ocr_region((887,300,1106,337),lang="ch")
            do_log.info(f'ocr_region结果: {has_error[0]["text"].strip()}')
            if has_error[0]['text'].strip() == '方案名称至少包含2个字符！':
                do_log.error(f'字符长度输入校验失败: {project_name}')
                allure.attach(f'字符长度输入校验失败: {project_name}', 
                            name="异常情况", 
                            attachment_type=allure.attachment_type.TEXT)
            else:
                assert has_error[0]['text'].strip() == (not expected_result), f'项目名称验证结果不符合预期: {project_name}'


    @allure.story('方案创建功能')
    @allure.title('创建新方案流程')
    @pytest.mark.smoke
    def test_create_model(self):
        """测试创建新方案流程"""
        project_name = 'AutoTest'
        with allure.step(f'方案名称输入: {project_name}'):
            airtest_method.touch_button(light_control.input_textbox)
            airtest_method.key_event('{BACKSPACE}')
            project_name = management.input_name(project_name, COLOR)
            with open(PROJECT_NAME_FILE, 'w', encoding='utf-8') as file:
                file.write(project_name)
        
        with allure.step('选择分割算法'):       
            if not airtest_method.check_exit(light_control.seg_item, 'FALSE', 3):
                pytest.fail('找不到分割算法控件')
            airtest_method.touch_button(light_control.seg_item)    
        
        with allure.step('点击创建按钮'):
            management.create_success(COLOR)
        do_log.info(f'方案成功新建: {project_name},用例执行成功')

    @allure.story('方案筛选功能')
    @allure.title('方案管理页面筛选框组合筛选')
    @pytest.mark.parametrize('search_text', ['Auto'])
    @pytest.mark.smoke
    def test_search_project(self, search_text: str):
        """测试方案筛选功能"""
        with allure.step('点击home键返回方案管理页面'):
            management.home()    
        with allure.step(f'使用关键词筛选: {search_text}'):
            management.mixed_filtering(search_text) 
        do_log.info(f'成功使用关键词 {search_text} 筛选出方案,用例执行成功')

    @allure.story('方案编辑功能')
    @allure.title('右键编辑方案')
    @pytest.mark.parametrize('edit_text', ['o*￣▽￣*o hihi嗨嗨123'])
    @pytest.mark.smoke
    def test_right_click_toedit(self, edit_text: str):
        """测试右键编辑功能"""
        with allure.step(f'鼠标右键进行编辑: {edit_text}'):
            management.right_click_toedit(edit_text)
        do_log.info(f'右键编辑添加备注成功: {edit_text},用例执行成功')

    @allure.story('方案关闭功能')
    @allure.title('右键关闭方案')
    @pytest.mark.smoke
    def test_closed_project(self):
        """测试右键关闭方案功能"""
        with allure.step('右键关闭方案'):
            management.right_click_toclosed()
            airtest_method.operate_sleep(3)
        do_log.info('成功关闭方案,用例执行成功')

    @allure.story('方案打开功能')
    @allure.title('双击打开方案')
    @pytest.mark.smoke
    def test_opened_project(self):
        """测试双击打开方案功能"""
        with allure.step('双击打开方案'):
            management.double_click_toopened()
        do_log.info('成功打开方案,用例执行成功')





            

       


        



