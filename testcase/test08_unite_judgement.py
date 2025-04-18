__author__ = "yunliu"
import pytest
import allure
from pages.management_page import management
from pages.data_page import data
from pages.judgement_page import judgement
from pages.infering_page import infering
from common.Airtest_method import airtest_method
from elements.public_control import light_control
from elements.pipelines import *
from common.handle_log import do_log

# 常量定义
COLOR = 'light'
PROJECT_PATH = r"D:\ly\VDL_projects\串联方案"
BATCH_SIZE = 3
IMAGE_NAME = 'Image_1.png'

@allure.feature('综合判定页面')
class TestUniteJudgement:
    """综合判定页面测试类"""

    @allure.story('基础功能')
    @allure.title('打开串联方案')
    @pytest.mark.smoke
    def test_open_pipelinespro(self):
        """测试打开串联方案功能"""
        with allure.step('打开串联方案'):
            management.open_project(PROJECT_PATH)
            management.click_project()
        do_log.info('打开串联方案成功，用例执行成功')

    @allure.story('基础功能')
    @allure.title('切换至综合判定页面')
    @pytest.mark.smoke
    def test_judgement(self):
        """测试切换至综合判定页面功能"""
        with allure.step('点击方案流程'):
            data.project_flow(COLOR)
        with allure.step('切换至综合判定'):
            judgement.judgement_page()
        do_log.info('成功切换至综合判定页面')

    @allure.story('推理功能')
    @allure.title('使用GPU-ONNX推理')
    @pytest.mark.smoke
    def test_GPU_ONNX_infering(self):
        """测试GPU-ONNX推理功能"""
        with allure.step('导入图像'):
            infering.images_input(PROJECT_PATH, 'sources', COLOR)
            do_log.info('图像导入成功')
        with allure.step('开始推理'):
            judgement.judgement_infering()
        with allure.step('判断是否推理成功'):
            judgement.judgement_done()
            do_log.info('综合判定推理结束')

    @allure.story('推理功能')
    @allure.title('使用CPU推理')
    @pytest.mark.smoke
    def test_CPU_infering(self):
        """测试CPU推理功能"""
        if not airtest_method.check_exit(light_control.judgement_infering_button, 'FALSE'):
            pytest.fail('找不到开始推理按钮')
            
        with allure.step('点击解锁按钮'):
            infering.unlock_infering()
        with allure.step('点击设备类型列表'):
            infering.infering_device_type()
        with allure.step('选择CPU设备'):
            infering.infering_device_CPU()
        with allure.step('开始推理'):
            judgement.judgement_infering()
        with allure.step('判断是否推理成功'):
            judgement.judgement_done()
            do_log.info('CPU推理完成，用例执行成功')

    @allure.story('推理功能')
    @allure.title('批量推理')
    @pytest.mark.smoke
    def test_batch_infering(self):
        """测试批量推理功能"""
        if not airtest_method.check_exit(light_control.judgement_infering_button, 'FALSE'):
            pytest.fail('找不到开始推理按钮')
            
        with allure.step('点击解锁按钮'):
            infering.unlock_infering()
        with allure.step('开启批量推理'):
            judgement.advanced_batch_infering(BATCH_SIZE)
        with allure.step('开始推理'):
            judgement.judgement_infering()
        with allure.step('判断是否推理成功'):
            judgement.judgement_done()
            do_log.info('批量推理完成，用例执行成功')

    @allure.story('推理功能')
    @allure.title('使用GPU-TRT推理')
    @pytest.mark.smoke
    def test_GPU_TRT_infering(self):
        """测试GPU-TRT推理功能"""
        if not airtest_method.check_exit(light_control.judgement_infering_button, 'FALSE'):
            pytest.fail('找不到开始推理按钮')
            
        with allure.step('点击解锁按钮'):
            infering.unlock_infering()
        with allure.step('高级配置进行trt设置'):
            judgement.advanced_trt_acceleration()
        with allure.step('开始推理'):
            judgement.judgement_infering()
        with allure.step('判断是否推理成功'):
            judgement.judgement_done()
            do_log.info('GPU-TRT推理完成，用例执行成功')

    @allure.story('导出功能')
    @allure.title('导出渲染图')
    @pytest.mark.smoke
    def test_export_rendering_image(self):
        """测试导出渲染图功能"""
        with allure.step('筛选图片'):
            judgement.select_image(IMAGE_NAME)
        with allure.step('点击导出渲染图按钮'):
            judgement.export_rendering_image()
        do_log.info('导出渲染图成功，用例执行成功')
        with allure.step('关闭方案'):
            airtest_method.key_event('^w')
    
