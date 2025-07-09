__author__ = "yunliu"
import pytest
import allure
from common.Airtest_method import airtest_method
from elements.public_control import light_control
from pages.infering_page import infering
from common.handle_log import do_log

# 常量定义
COLOR = 'light'
BATCH_SIZE = 3

@allure.feature('模型推理页面')
class TestInfer:
    """模型推理页面测试类"""

    @allure.story('页面导航')
    @allure.title('切换至模型推理页面')
    @pytest.mark.smoke
    def test_model_infering(self):
        """测试切换到模型推理页面功能"""
        with allure.step('点击模型推理tab按钮'):
            infering.model_infering(COLOR)
        do_log.info('切换至模型推理页面,用例执行成功')

    @allure.story('数据导入')
    @allure.title('导入图像')
    @pytest.mark.smoke
    def test_images_input(self):
        """测试导入图像功能"""
        with allure.step('导入图像'):
            dataset = r'D:\ly\VDL_autotest\elements'
            infering.images_input(dataset, 'images', COLOR)
        do_log.info('图像导入成功,用例执行成功')

    @allure.story('推理功能')
    @allure.title('使用GPU-ONNX推理')
    @pytest.mark.smoke
    def test_GPU_ONNX_infering(self):
        """测试GPU-ONNX推理功能"""
        with allure.step('点击开始推理按钮'):
            infering.begin_infering(COLOR)
        with allure.step('判断推理是否完成'):
            infering.review_infering(COLOR)
        do_log.info('GPU-ONNX推理完成,用例执行成功')

    @allure.story('结果导出')
    @allure.title('导出渲染图')
    @pytest.mark.smoke
    def test_export_rendering_image(self):
        """测试导出渲染图功能"""
        with allure.step('点击图像搜索框'):
            infering.images_searching("10")
        with allure.step('点击导出渲染图按钮'):
            infering.export_rendering_image()
        do_log.info('导出渲染图成功,用例执行成功')

    @allure.story('推理功能')
    @allure.title('批量推理')
    @pytest.mark.smoke
    def test_batch_infering(self):
        """测试批量推理功能"""
        infering.review_infering(COLOR)
        if not airtest_method.check_exit(light_control.return_infering, 'FALSE'):
            pytest.fail('找不到开始推理按钮')
        
        with allure.step('点击解锁按钮'):
            infering.unlock_infering()
        with allure.step('开启批量推理'):
            infering.batch_infering(BATCH_SIZE)
            infering.return_infering()
        do_log.info('批量推理完成,用例执行成功')

    @allure.story('推理功能')
    @allure.title('使用GPU-FP32-TRT推理')
    @pytest.mark.smoke
    def test_GPU_fp32_infering(self):
        """测试GPU-FP32-TRT推理功能"""
        infering.review_infering(COLOR)
        if not airtest_method.check_exit(light_control.return_infering, 'FALSE'):
            pytest.fail('找不到开始推理按钮')
        
        with allure.step('点击解锁按钮'):
            infering.unlock_infering()
        with allure.step('点击模式选择列表'):
            infering.infering_pattern_choice()
        with allure.step('选择TRT-FP32模式'):
            infering.infering_FP32_TRT()
            infering.batch_infering(BATCH_SIZE)
        with allure.step('点击重新推理按钮'):
            infering.return_infering()
        with allure.step('判断推理是否完成'):
            infering.review_infering(COLOR)
        do_log.info('GPU-FP32推理完成,用例执行成功')

    @allure.story('推理功能')
    @allure.title('使用GPU-FP16-TRT推理')
    @pytest.mark.smoke
    def test_GPU_fp16_infering(self):
        """测试GPU-FP16-TRT推理功能"""
        infering.review_infering(COLOR)
        if not airtest_method.check_exit(light_control.return_infering, 'FALSE'):
            pytest.fail('找不到开始推理按钮')
        
        with allure.step('点击解锁按钮'):
            infering.unlock_infering()
        with allure.step('点击模式选择列表'):
            infering.infering_pattern_choice()
        with allure.step('选择TRT-FP16模式'):
            infering.infering_FP16_TRT()
            infering.batch_infering(BATCH_SIZE)
        with allure.step('点击重新推理按钮'):
            infering.return_infering()
        with allure.step('判断推理是否完成'):
            infering.review_infering(COLOR)
        do_log.info('GPU-FP16推理完成,用例执行成功')

    @allure.story('推理功能')
    @allure.title('使用CPU推理')
    @pytest.mark.smoke
    def test_CPU_infering(self):
        """测试CPU推理功能"""
        infering.review_infering(COLOR)
        if not airtest_method.check_exit(light_control.return_infering, 'FALSE'):
            pytest.fail('找不到开始推理按钮')
        
        with allure.step('点击解锁按钮'):
            infering.unlock_infering()
        with allure.step('点击设备类型列表'):
            infering.infering_device_type()
        with allure.step('选择CPU设备'):
            infering.infering_device_CPU()
        with allure.step('点击重新推理按钮'):
            infering.return_infering()
        with allure.step('判断推理是否完成'):
            infering.review_infering(COLOR)
        do_log.info('CPU推理完成,用例执行成功')
        