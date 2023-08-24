import pytest
from common.Airtest_method import airtest_method
from elements.public_control import control
from common.handle_log import do_log
from pages.infering_page import infering

@pytest.mark.smoke
def test_model_infering():
    infering.model_infering()
    do_log.info('切换至模型推理页面,用例执行成功')

@pytest.mark.smoke
def test_images_input():
    dataset = 'C:\\Users\\yunli\\Documents\\1中文繁體A-B_[c]\\'
    infering.images_input(dataset,'sources')
    do_log.info('图像导入成功,用例执行成功')

@pytest.mark.smoke
def test_begin_infering():
    infering.begin_infering()
    do_log.info('点击开始推理,用例执行成功')

@pytest.mark.smoke
def test_review_infering():
    infering.review_infering()
    do_log.info('推理完成,用例执行成功')   