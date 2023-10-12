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

@allure.title('导出软件使用手册')
@pytest.mark.smoke
def test_user_guild():
    with allure.step(f'点击帮助按钮'):
        assess.template_help()
    with allure.step(f'导出软件使用手册'):
        assess.user_guild()

@allure.title('导出软件使用SDK开发手册')
@pytest.mark.smoke
def test_SDK_guild():
    with allure.step(f'点击帮助按钮'):
        assess.template_help()
    with allure.step(f'导出SDK开发手册'):
        assess.SDK_guild()