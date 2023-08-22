import pytest
from common.Airtest_method import airtest_method
from elements.public_control import control
from common.handle_log import do_log

@pytest.mark.smoke
def test_data_page():
    airtest_method.touch_button(control.image_label)
    if not airtest_method.check_exit(control.auto_divide,'FALSE') :
        do_log.error('图像标注页面切换失败，用例执行失败')
        assert False,'找不到图像标注页面'
    else:
        airtest_method.touch_button(control.auto_divide)
        do_log.info('图像标注页面成功切换,用例执行成功')
        do_log.info('自动划分成功,用例执行成功')
