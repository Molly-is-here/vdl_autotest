import pytest
import allure
from common.Airtest_method import airtest_method
from elements.public_control import control
from pages.infering_page import infering
from common.handle_log import do_log


@allure.feature('模型推理页面')
@allure.title('切换至模型推理页面')
@pytest.mark.smoke
def test_model_infering():
    with allure.step(f'点击模型推理tab按钮'):
        infering.model_infering()
        do_log.info('切换至模型推理页面,用例执行成功')

@allure.title('导入图像')
@pytest.mark.smoke
def test_images_input():
    with allure.step(f'导入图像'):
        dataset = r'D:\ly\VDL_autotest\VDL_autotest\elements'  
        infering.images_input(dataset,'images')    
        do_log.info('图像导入成功,用例执行成功')

@allure.title('使用GPU-ONNX推理')
@pytest.mark.smoke
def test_GPU_ONNX_infering():
    with allure.step(f'点击开始推理按钮'):
        infering.begin_infering()
    with allure.step(f'判断推理是否完成'):
        infering.review_infering()
        do_log.info('GPU-ONNX推理完成,用例执行成功') 

@allure.title('使用GPU-TRT推理')
@pytest.mark.smoke 
def test_GPU_TRT_infering():
    if not airtest_method.check_exit(control.begin_infering,'FALSE'):      
        assert False,'找不到开始推理按钮'
    else:         
        with allure.step(f'点击解锁按钮'):
            infering.unlock_infering()
        with allure.step(f'点击模式选择列表'):
            infering.infering_pattern_choice()
        with allure.step(f'选择TRT模式'):
            infering.infering_pattern_TRT()
        with allure.step(f'点击开始推理按钮'):
            infering.begin_infering()
        with allure.step(f'判断推理是否完成'):
            infering.review_infering()
            do_log.info('GPU-TRT推理完成,用例执行成功') 

@allure.title('使用CPU推理')
@pytest.mark.smoke 
def test_CPU_infering():
    if not airtest_method.check_exit(control.begin_infering,'FALSE'):      
        assert False,'找不到开始推理按钮'
    else: 
        with allure.step(f'点击解锁按钮'):
            infering.unlock_infering()
        with allure.step(f'点击设备类型列表'):
            infering.infering_device_type()
        with allure.step(f'选择CPU设备'):
            infering.infering_device_CPU()
        with allure.step(f'点击开始推理按钮'):
            infering.begin_infering()
        with allure.step(f'判断推理是否完成'):
            infering.review_infering()
            do_log.info('CPU推理完成,用例执行成功') 
        