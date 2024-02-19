import pytest
import allure
from common.Airtest_method import airtest_method
from elements.public_control import control
from common.handle_log import do_log

@allure.feature('图像标注页面')
@allure.title('切换至图像标注页面')
@pytest.mark.smoke
def test_data_page():
    with allure.step(f'点击图像标注tab按钮'):
        if not airtest_method.check_exit(control.image_label,'FALSE') :
            assert False,'找不到图像标注tab按钮'
        else:
            airtest_method.touch_button(control.image_label)
            airtest_method.operate_sleep(2.0)
            do_log.info('图像标注页面成功切换,用例执行成功')

@allure.title('数据划分')
@pytest.mark.smoke
def test_auto_divide():
    with allure.step(f'点击数据划分按钮'):
        if not airtest_method.check_exit(control.auto_divide,'FALSE') :
            assert False,'找不到数据划分按钮'
        else:
            airtest_method.touch_button(control.auto_divide)
            do_log.info('自动划分成功,用例执行成功')
