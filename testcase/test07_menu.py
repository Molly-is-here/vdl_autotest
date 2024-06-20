import pytest
import allure
from common.Airtest_method import airtest_method
from elements.public_control import control
from pages.assess_page import assess
from common.handle_log import do_log


@allure.feature('菜单栏')
@allure.title('关闭方案')
@pytest.mark.smoke
def test_template_close():
    with allure.step(f'点击文件按钮'):
        assess.template_file()
    with allure.step(f'点击关闭方案'):
        assess.template_close()
        airtest_method.operate_sleep()
    do_log.info('关闭方案成功，用例执行成功')

@allure.title('导出SDK')
@pytest.mark.smoke
def test_template_SDK():
    with allure.step(f'点击文件按钮'):
        assess.template_file()
    with allure.step(f'导出SDK'):
        assess.template_SDK()
    do_log.info('导出SDK成功，用例执行成功')

@allure.title('导出软件功能手册')
@pytest.mark.smoke
def test_user_guild():
    with allure.step(f'点击帮助按钮'):
        assess.template_help()
    with allure.step(f'导出软件功能手册'):
        assess.user_guild()
    do_log.info('软件功能手册导出成功，用例执行成功')

@allure.title('导出软件操作手册')
@pytest.mark.smoke
def test_operating_guild():
    with allure.step(f'点击帮助按钮'):
        assess.template_help()
    with allure.step(f'导出软件操作手册'):
        assess.operating_guild()
    do_log.info('软件操作手册导出成功，用例执行成功')

@allure.title('导出软件使用SDK开发手册')
@pytest.mark.smoke
def test_SDK_guild():
    with allure.step(f'点击帮助按钮'):
        assess.template_help()
    with allure.step(f'导出C++ SDK开发手册'):
        assess.SDK_guild('c++')
    with allure.step(f'导出Csharp SDK开发手册'):
        assess.SDK_guild('csharp')
    do_log.info('SDK开发手册导出成功，用例执行成功')