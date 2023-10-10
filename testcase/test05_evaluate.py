import pytest
import allure
from common.Airtest_method import airtest_method
from elements.public_control import control
from common.handle_log import do_log
from pages.assess_page import assess
from pages.open_sofrware import open_Software

@allure.feature('模型评估页面')
@allure.title('切换至模型评估页面')
@pytest.mark.smoke
def test_assess_page():
    with allure.step(f'点击模型评估tab按钮'):
        assess.model_assess()
        do_log.info('模型评估页面成功切换,用例执行成功')

@allure.title('导出模型')
@pytest.mark.smoke
def test_export_model():  
    assess.assess_success()
    airtest_method.touch_button(control.new_card)
    with allure.step(f'点击更多按钮'):
        assess.more_button()
    with allure.step(f'选择导出模型'):
        assess.export_model()
        do_log.info('模型成功导出,用例执行成功')

@allure.title('导出报告')
@pytest.mark.smoke
def test_export_report():
    with allure.step(f'点击导出报告按钮'):
        assess.export_report()
        airtest_method.operate_sleep(5.0)
    with allure.step(f'导出报告后返回mainwindow'):
        open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
        do_log.info('报告成功导出,用例执行成功')

