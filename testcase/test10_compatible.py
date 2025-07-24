from airtest.core.api import *
from common.Airtest_method import airtest_method
from common.handle_log import do_log
from elements.elements_path import save_path
from elements.public_control import light_control
from pages.management_page import management
from pages.training_page import training
from pages.assess_page import assess
from tools.monitoring import get_training_utilization
from tools.docqq import run
from pathlib import Path
import pytest
import allure
import threading
import os

# 配置表：算法类型及其参数定义
ALGORITHM_CONFIG = {
    "CLS": {"path_index": 0, "need_models": True, "model_list": "default", "screenshot": ["类别级别"]},  
    "OCR": {"path_index": 3, "need_models": True, "model_list": "default", "screenshot": ["图像级别", "字符级别"]},
    "SEQOCR": {"path_index": 5, "need_models": True, "model_list": [light_control.high_power], "screenshot": ["图像级别", "内容级别", "类别级别"]},
    "UAD": {"path_index": 4, "need_models": True, "model_list": "uad", "screenshot": ["项目级别"], "show_types": [light_control.uad_cls, light_control.uad_seg]},
    "UADOCV": {"path_index": 6, "need_models": True, "model_list": "default", "screenshot": ["字符级别", "类别级别"]},
    "CLSOCV": {"path_index": 7, "need_models": True, "model_list": "default", "screenshot": ["字符级别", "类别级别"]},
    "DET": {"path_index": 1, "need_models": True, "model_list": "default", "screenshot": ["图像级别", "类别级别"]},
    "SEG": {"path_index": 2, "need_models": True, "model_list": "default", "screenshot": ["图像级别", "类别级别", "像素级别"]},
}

model_selection = [light_control.high_power, light_control.low_power]
UADmodel_selection = [light_control.modelB, light_control.modelA_low_power, light_control.modelA_high_power]
LEARNING_TIMES = '30'
color = 'light'

@allure.title('八类算法对比测试')
@pytest.mark.smoke
def test_compatible_smoke():
    for name, config in ALGORITHM_CONFIG.items():
        path_index = config["path_index"]
        screenshot_types = config["screenshot"]
        model_list_key = config.get("model_list")
        show_types = config.get("show_types", [None])

        dataset_list = get_dataset_list(save_path.compare_project[path_index])

        for project_path in dataset_list:
            dataset_name = os.path.basename(project_path)
            with allure.step(f'当前运行{dataset_name}方案'):
                management.open_project(project_path)
                management.click_project()
                training.model_training(color)

                for show_type in show_types:

                    # 根据配置获取对应模型列表
                    if model_list_key == "default":
                        model_list = model_selection
                    elif model_list_key == "uad":
                        model_list = UADmodel_selection
                    elif isinstance(model_list_key, list):
                        model_list = model_list_key
                    else:
                        model_list = []

                    for model_type in model_list:
                        output_type = get_output_type(model_type, show_type)

                        # 执行训练及监控，绘图在run_training里主线程调用
                        status = [0]  # 用于线程间共享状态，0表示监控线程运行中，1表示退出信号
                        event = threading.Event()  # 用于线程同步通知

                        run_training(dataset_name, project_path, name, show_type, model_type, output_type, status, event)
                        post_flow(name, dataset_name, output_type, screenshot_types)

                airtest_method.key_event("^w")
                airtest_method.operate_sleep()

def get_dataset_list(folder_path):
    '''获取数据集列表'''
    folder_path = Path(folder_path)
    return [str(entry) for entry in folder_path.iterdir() if entry.is_dir()]

def get_output_type(model_type, show_type=None):
    '''根据不同模型类型，输出类型名称'''
    base = ''
    if model_type == light_control.high_power:
        base = '高精度'
    elif model_type == light_control.low_power:
        base = '低功耗'
    elif model_type == light_control.modelA_low_power:
        base = '模型A-低功耗'
    elif model_type == light_control.modelA_high_power:
        base = '模型A-高精度'
    elif model_type == light_control.modelB:
        base = '模型B'

    if show_type == light_control.uad_cls:
        return f'无监督分类_{base}'
    elif show_type == light_control.uad_seg:
        return f'无监督分割_{base}'
    return base

def run_training(dataset_name, project_path, name, show_type, model_type, output_type, status, event):
    '''
    运行训练流程并监控资源使用：
    - 启动监控线程采集资源使用数据（Excel）
    - 训练执行
    - 通知监控线程停止
    - 主线程等待监控线程结束
    - 主线程调用绘图函数绘制资源使用曲线图
    '''

    training.model_training(color)

    if name == "UAD":
        training.add_card(color)
        training.uad_moudle_type(show_type)
        training.uad_choice_model(model_type)
    else:
        if model_type:
            training.add_card(color)
            training.choice_model(model_type)

    # 启动资源监控线程，传入文件名、状态标志、事件对象
    monitor_thread = threading.Thread(
        target=get_training_utilization,
        args=(f"{dataset_name}_{output_type}", status, event)
    )

    airtest_method.operate_sleep()
    monitor_thread.start()

    training.set_all_study(name, LEARNING_TIMES, color)
    training.star_training(color)

    output_dir = os.path.join(save_path.project_save_path, project_path, "output")
    training_dirs = [d for d in os.listdir(output_dir) if d.isdigit()]
    latest_training = max(training_dirs, key=int)

    if name in ["CLSOCV", "UADOCV"]:
        log_path = os.path.join(output_dir, latest_training, name.lower().replace("ocv", ""), "vimo-train.log")
    else:
        log_path = os.path.join(output_dir, latest_training, "vimo-train.log")

    training.training_success(log_path, project_path)

    # 通知监控线程退出
    status[0] = 1
    event.set()

    # 主线程等待监控线程结束，超时5秒
    monitor_thread.join(timeout=5.0)
    if monitor_thread.is_alive():
        do_log.warning("监控线程未正常退出，可能存在资源泄漏风险。")
    else:
        do_log.info(f"{dataset_name}监控线程成功结束")

    # 在主线程调用绘图函数，避免绘图库多线程问题
    try:
        plot_file = f"{dataset_name}_{output_type}.xlsx"
        from tools.monitoring import plot_resource_usage  # 延迟导入避免循环依赖
        plot_resource_usage(plot_file)
    except Exception as e:
        do_log.error(f"绘图失败: {e}")

def post_flow(name, dataset_name, output_type, screenshot_types):
    '''获取训练时长并截图，获取评估结果并截图'''

    training_screenshot = os.path.join(save_path.base_path, f"{dataset_name}_{output_type}训练时长.jpg")
    airtest_method.operate_sleep(2.0)
    airtest_method.screenshot(training_screenshot)
    screenshot_images = [training_screenshot]

    assess.model_assess(color)
    assess.assess_success(color)
    if name in ['CLS', 'DET', 'OCR', 'SEG', 'SEQOCR', 'UADOCV', 'CLSOCV', 'UAD']:
        assess.assess_done()
        do_log.info(f"{dataset_name}_{output_type}_评估完成")
    else:
        if not airtest_method.check_exit(light_control.sensitive_area, 'FALSE', 360000):
            assert False, f"{dataset_name}_{output_type}_评估失败"
    airtest_method.operate_sleep(15.0)

    screen_shot_by_type(dataset_name, output_type, screenshot_images, screenshot_types)

def screen_shot_by_type(dataset_name, output_type, screenshot_images, screenshot_types):
    '''截图，并将结果写入腾讯文档'''

    button_map = {
        "图像级别": None,
        "类别级别": light_control.type_image,
        "像素级别": light_control.pixel_image,
        "字符级别": light_control.ocr_image,
        "内容级别": light_control.content_image,
        "项目级别": None
    }

    for shot_type in screenshot_types:
        if button_map[shot_type]:
            airtest_method.touch_button(button_map[shot_type])

        shot_path = os.path.join(save_path.base_path, f"{dataset_name}_{output_type}_{shot_type}.jpg")
        if shot_path not in screenshot_images:
            airtest_method.screenshot(shot_path)
            screenshot_images.append(shot_path)

        do_log.info(f"截图已保存：{dataset_name}_{output_type}_{shot_type}")

    run("https://docs.qq.com/sheet/DY3VIak9uVkRYaXpm?u=7f2950a20b1040d3bd13eae7fcb0cd81&no_promotion=1&tab=BB08J2",
        ["", "V1.7.2", dataset_name, output_type],
        screenshot_images)
