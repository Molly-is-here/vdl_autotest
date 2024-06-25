import pytest
import allure
from pages.marking_page import mark
from common.handle_log import do_log

@allure.feature('图像标注页面')
@allure.title('切换至图像标注页面')
@pytest.mark.smoke
def test_image_label():
    with allure.step(f'点击图像标注tab按钮'):
        mark.image_label()  
    do_log.info('图像标注页面成功切换,用例执行成功')

@allure.title('数据划分')
@pytest.mark.smoke
def test_auto_divide():
    with allure.step(f'点击数据划分按钮'):
        mark.auto_divide()
    do_log.info('自动划分成功,用例执行成功')
