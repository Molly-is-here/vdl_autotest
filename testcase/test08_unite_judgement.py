__author__ = "yunliu"
import pytest
import allure
from pages.management_page import management
from pages.data_page import data
from pages.assess_page import assess
from pages.judgement_page import judgement
from pages.infering_page import infering
from common.Airtest_method import airtest_method
from elements.public_control import light_control
from elements.pipelines import *
from common.handle_log import do_log

color = 'light'
@allure.feature('综合判定页面')
@allure.title('打开串联方案')
@pytest.mark.smoke
def test_open_pipelinespro():
    with allure.step(f'打开串联方案'):
        path = r"D:\ly\VDL_projects\串联方案"
        management.open_project(path)
        management.click_project()
    do_log.info('打开串联方案成功,用例执行成功')

@allure.title('切换至综合判定页面')
@pytest.mark.smoke
def test_judgement():
    with allure.step(f'点击方案流程'):
        data.project_flow(color)
    with allure.step(f'切换至综合判定'):
        judgement.judgement_page()
    do_log.info('成功切换至综合判定页面')

@allure.title('使用GPU-ONNX推理')
@pytest.mark.smoke
def test_GPU_ONNX_infering():
    with allure.step(f'导入图像'):
        dataset = r'D:\ly\VDL_projects\串联方案'
        infering.images_input(dataset,'sources',color)
        do_log.info('图像导入成功')
    with allure.step(f'开始推理'):
        judgement.judgement_infering()
    with allure.step(f'判断是否推理成功'):
        judgement.judgement_done()
        do_log.info('综合判定推理结束')

@allure.title('使用CPU推理')
@pytest.mark.smoke
def test_CPU_infering():
    if not airtest_method.check_exit(light_control.judgement_infering_button,'FALSE'):      
        assert False,'找不到开始推理按钮'
    else: 
        with allure.step(f'点击解锁按钮'):
            infering.unlock_infering()
        with allure.step(f'点击设备类型列表'):
            infering.infering_device_type()
        with allure.step(f'选择CPU设备'):
            infering.infering_device_CPU()
        with allure.step(f'开始推理'):
            judgement.judgement_infering()
        with allure.step(f'判断是否推理成功'):
            judgement.judgement_done()
            do_log.info('CPU推理完成,用例执行成功') 

@allure.title('批量推理')
@pytest.mark.smoke
def test_batch_infering():
    if not airtest_method.check_exit(light_control.judgement_infering_button,'FALSE'):      
        assert False,'找不到开始推理按钮'
    else:         
        with allure.step(f'点击解锁按钮'):
            infering.unlock_infering()
        with allure.step(f'开启批量推理'):
            judgement.advanced_batch_infering(3)
        with allure.step(f'开始推理'):
                judgement.judgement_infering()
        with allure.step(f'判断是否推理成功'):
            judgement.judgement_done()
            do_log.info('批量推理完成,用例执行成功')

@allure.title('使用GPU-TRT推理')
@pytest.mark.smoke
def test_GPU_TRT_infering():
    if not airtest_method.check_exit(light_control.judgement_infering_button,'FALSE'):      
        assert False,'找不到开始推理按钮'
    else:         
        with allure.step(f'点击解锁按钮'):
            infering.unlock_infering()
        with allure.step(f'高级配置进行trt设置'):
            judgement.advanced_trt_acceleration()
        with allure.step(f'开始推理'):
            judgement.judgement_infering()
        with allure.step(f'判断是否推理成功'):
            judgement.judgement_done()
            do_log.info('GPU-TRT推理完成,用例执行成功') 

@allure.title('导出渲染图')
@pytest.mark.smoke
def test_export_rendering_image():
    with allure.step(f'筛选图片'):
        judgement.select_image('Image_1.png')
    with allure.step(f'点击导出渲染图按钮'):
        judgement.export_rendering_image()
    do_log.info('导出渲染图成功,用例执行成功')
    
