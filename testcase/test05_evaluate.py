import pytest
import allure
import os
from common.Airtest_method import airtest_method
from common.handle_log import do_log
from elements.public_control import control
from pages.assess_page import assess

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

@allure.title('导出SDK')
@pytest.mark.smoke
def test_export_SDK():  
    assess.assess_success()
    airtest_method.touch_button(control.new_card)
    with allure.step(f'点击更多按钮'):
        assess.more_button()
    with allure.step(f'导出模型+SDK'):
        current_dir = os.getcwd()
        assess.export_SDK(current_dir)
        do_log.info('SDK成功导出,用例执行成功')

@allure.title('运行SDK')
@pytest.mark.smoke
def test_run_SDK():
    with allure.step(f'解压SDK'):
        assess.unzip_SDK()
    with allure.step(f'复制SDK运行的依赖文件'):
        assess.copy_SDK_dll()
    with allure.step(f'调用SDK开始推理'):
        dataset = r'D:\ly\VDL_autotest\VDL_autotest\elements\images'
        assess.run_SDK(dataset,'SDKdemo')

@allure.title('导出报告')
@pytest.mark.smoke
def test_export_report():
    with allure.step(f'点击导出报告按钮'):
        assess.export_report()
        do_log.info('报告成功导出,用例执行成功')

