__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from pages.data_page import data
from pages.management_page import management
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from elements.public_control import light_control
from common.handle_log import do_log
from common.Base_method import search_file
from itertools import product
import pytest
import allure
import os
import random

auto_setup(__file__)
LEARNING_TIMES = '1'
COLOR = 'light'
TRAIN_MODE = 'smoke'

def check_dataset_path(dataset_path):
    """检查数据集路径是否存在"""
    if not os.path.exists(dataset_path):
        do_log.error(f"Dataset path does not exist: {dataset_path}")
        return False
    return True

# 算法类型映射字典
ALGORITHM_MAP = {
    save_path.seg: {'dataset': save_path.seg_dataset, 'name': 'SEG'},
    save_path.cls: {'dataset': save_path.cls_dataset, 'name': 'CLS'},
    save_path.det: {'dataset': save_path.det_dataset, 'name': 'DET'},
    save_path.ocr: {'dataset': save_path.ocr_dataset, 'name': 'OCR'},
    save_path.uad: {'dataset': save_path.uad_dataset, 'name': 'UAD'},
    save_path.seqocr: {'dataset': save_path.seqocr_dataset, 'name': 'SEQ'},
    save_path.clsocv: {'dataset': save_path.clsocv_dataset, 'name': 'CLSOCV'},
    save_path.uadocv: {'dataset': save_path.uadocv_dataset, 'name': 'UADOCV'}
}

def create_project_setup(project_name, project_path, file_path):
    """创建项目并完成基础设置
    Args:
        project_name: 项目名称，如'CLSOCV'
        project_path: 项目类型图片路径，如save_path.clsocv
        file_path: 文件路径
    Returns:
        project_name: 实际创建的项目名称
    """
    # 方案管理页面
    management.create_project(COLOR)
    project_name = management.input_name(project_name, COLOR)
    management.create_model(project_path)

    # 数据管理页面
    data.add_file(file_path)

    # 图像标注页面
    mark.image_label(COLOR)
    mark.auto_divide(COLOR)
    
    return project_name


def train_and_assess_project(project_name, file_path, params_list=None, special_params=None, name=None):
    """训练和评估项目
    Args:
        project_name: 项目名称
        file_path: 文件路径
        params_list: 参数列表
        special_params: 特殊参数
        name: 算法类型标识，如'CLSOCV'
    """   
    try:
        # 模型训练页面
        training.model_training(COLOR)
        training.add_card(COLOR)
        
        if params_list:
            training.choice_model(params_list[0][0])
            training.image_scaling(params_list[0][1])
            training.color_mode(params_list[0][2])
        
        if special_params:
            if 'study_times' in special_params:
                training.set_study(special_params['study_times'], COLOR)
            if 'uad_module' in special_params:
                training.uad_moudle_type(special_params['uad_module'])
            if 'uad_model' in special_params:
                training.uad_choice_model(special_params['uad_model'])        
            if 'seq_study' in special_params:
                training.seq_set_study(special_params['seq_study'])
            if 'ocv_study' in special_params:
                training.ocv_set_study(special_params['ocv_study'])

        training.star_training(COLOR)
        
        # 动态构建训练日志路径
        output_dir = os.path.join(save_path.project_save_path, project_name, "output")
        if not os.path.exists(output_dir):
            do_log.error(f"Output directory does not exist: {output_dir}")
            return
            
        # 获取最新的训练目录
        training_dirs = [d for d in os.listdir(output_dir) if d.isdigit()]
        if not training_dirs:
            do_log.error(f"No training directories found in: {output_dir}")
            return
            
        latest_training = max(training_dirs, key=int)
        
        # 根据项目类型构建不同的日志路径
        if name == 'CLSOCV':
            path = os.path.join(output_dir, latest_training, "cls", "vimo-train.log")
        elif name == 'UADOCV':
            path = os.path.join(output_dir, latest_training, "uad", "vimo-train.log")
        else:
            path = os.path.join(output_dir, latest_training, "vimo-train.log")
            
        training.training_success(path, project_name)
        # training.review_assess()

        # 模型评估页面
        assess.model_assess(COLOR)
        assess.assess_done()

        # 调用SDK
        assess.more_button()
        assess.export_SDK(os.getcwd())
        assess.unzip_SDK()
        assess.copy_SDK_dll()
        assess.run_SDK(file_path, project_name)
        
    except Exception as e:
        do_log.error(f"Error during training and assessment: {str(e)}")
        # 不抛出异常，让循环继续
        return

def close_project():
    # 关闭方案
    # assess.template_file()
    assess.template_close()

@allure.title('八类算法冒烟')
@pytest.mark.smoke
def test_algorithm_smoke():
    for item in save_path.project_list:
        algo_info = ALGORITHM_MAP[item]
        name = algo_info['name']
        dataset = algo_info['dataset']
        
        # 检查数据集路径是否存在
        if not check_dataset_path(dataset):
            do_log.error(f"Skipping {name} algorithm test due to missing dataset path")
            continue
            
        current_dir = os.getcwd()
        model_selection = [light_control.high_power, light_control.low_power]
        color_mode = [0, light_control.gray_image]
        scaling_selection = [0, light_control.equal_size, light_control.zidingyi_size]

        if name == 'SEQ':
            with allure.step(f'{name}算法冒烟'):
                for file in search_file.get_file(dataset):
                    current_file_path = str(os.path.join(dataset, file))
                    project_name = create_project_setup(name, save_path.seqocr, current_file_path)
                    # 循环参数组合
                    count = min(len(scaling_selection), len(color_mode))
                    for i in range(count):
                        params_list = [(light_control.high_power, scaling_selection[i], color_mode[i])]
                        train_and_assess_project(project_name, current_file_path, params_list, 
                                              {'seq_study': LEARNING_TIMES}, name)
                    assess.home()

        elif name == 'UAD':
            show_type = [light_control.uad_cls,light_control.uad_seg]
            UADmodel_selection = [light_control.modelB, light_control.modelA_low_power, 
                                light_control.modelA_high_power]
            for file in search_file.get_file(dataset):
                current_file_path = str(os.path.join(dataset, file))
                project_name = create_project_setup(name, save_path.uad, current_file_path)
                # 遍历每个模块类型和模型类型的组合
                for module in show_type:
                    for model_type in UADmodel_selection:
                        with allure.step(f'{name}算法冒烟'):
                            train_and_assess_project(project_name, current_file_path, None,
                                                  {'uad_model': model_type,
                                                   'uad_module': module}, name)
                assess.home()

        elif name == 'OCR':
            for file in search_file.get_file(dataset):
                current_file_path = str(os.path.join(dataset, file))
                project_name = create_project_setup(name, save_path.ocr, current_file_path)
                with allure.step(f'{name}算法冒烟'):
                    #随机训练参数组合
                    all_combinations = list(product(model_selection, scaling_selection, color_mode))
                    #冒烟测试只跑3组
                    if TRAIN_MODE == 'smoke':
                        selected_combinations = random.sample(all_combinations, min(3, len(all_combinations)))
                    else:
                        selected_combinations = all_combinations
                    do_log.info(f"{name}选择的训练参数为: {selected_combinations}")

                    for params in selected_combinations:
                        params_list = [params]
                        train_and_assess_project(project_name, current_file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)
                    assess.home()

        elif name == 'CLS':
            do_log.info(f"Files in dataset '{dataset}': {search_file.get_file(dataset)}")
            for file in search_file.get_file(dataset):
                current_file_path = str(os.path.join(dataset, file))
                project_name = create_project_setup(name, save_path.cls, current_file_path)
                with allure.step(f'{name}算法冒烟'):
                    #随机训练参数组合
                    all_combinations = list(product(model_selection, scaling_selection, color_mode))
                    #冒烟测试只跑3组
                    if TRAIN_MODE == 'smoke':
                        selected_combinations = random.sample(all_combinations, min(3, len(all_combinations)))
                    else:
                        selected_combinations = all_combinations
                    do_log.info(f"{name}选择的训练参数为: {selected_combinations}")

                    for params in selected_combinations:
                        params_list = [params]
                        train_and_assess_project(project_name, current_file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)
                    assess.home()


        elif name == 'DET':
            DET_scaling_selection = [0, light_control.equal_size]
            for file in search_file.get_file(dataset):
                current_file_path = str(os.path.join(dataset, file))
                project_name = create_project_setup(name, save_path.det, current_file_path)
                with allure.step(f'{name}算法冒烟'):
                    #随机训练参数组合
                    all_combinations = list(product(model_selection, DET_scaling_selection, color_mode))
                    #冒烟测试只跑3组
                    if TRAIN_MODE == 'smoke':
                        selected_combinations = random.sample(all_combinations, min(3, len(all_combinations)))
                    else:
                        selected_combinations = all_combinations
                    do_log.info(f"{name}选择的训练参数为: {selected_combinations}")

                    for params in selected_combinations:
                        params_list = [params]
                        train_and_assess_project(project_name, current_file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)
                    assess.home()

        elif name == 'SEG':
            for file in search_file.get_file(dataset):
                current_file_path = str(os.path.join(dataset, file))
                project_name = create_project_setup(name, save_path.seg, current_file_path)
                with allure.step(f'{name}算法冒烟'):
                    #随机训练参数组合
                    all_combinations = list(product(model_selection, scaling_selection, color_mode))
                    #冒烟测试只跑3组
                    if TRAIN_MODE == 'smoke':
                        selected_combinations = random.sample(all_combinations, min(3, len(all_combinations)))
                    else:
                        selected_combinations = all_combinations
                    do_log.info(f"{name}选择的训练参数为: {selected_combinations}")

                    for params in selected_combinations:
                        params_list = [params]
                        train_and_assess_project(project_name, current_file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)
                    assess.home()

        elif name == 'CLSOCV':
            for file in search_file.get_file(dataset):
                current_file_path = str(os.path.join(dataset, file))
                project_name = create_project_setup(name, save_path.clsocv, current_file_path)
                with allure.step(f'{name}算法冒烟'):
                    #随机训练参数组合
                    all_combinations = list(product(model_selection, scaling_selection, color_mode))
                    #冒烟测试只跑3组
                    if TRAIN_MODE == 'smoke':
                        selected_combinations = random.sample(all_combinations, min(3, len(all_combinations)))
                    else:
                        selected_combinations = all_combinations
                    do_log.info(f"{name}选择的训练参数为: {selected_combinations}")

                    for params in selected_combinations:
                        params_list = [params]
                        train_and_assess_project(project_name, current_file_path, params_list,
                                              {'ocv_study': LEARNING_TIMES}, name)
                    assess.home()

        elif name == 'UADOCV':
            for file in search_file.get_file(dataset):
                current_file_path = str(os.path.join(dataset, file))
                project_name = create_project_setup(name, save_path.uadocv, current_file_path)
                with allure.step(f'{name}算法冒烟'):
                    #随机训练参数组合
                    all_combinations = list(product(model_selection, scaling_selection, color_mode))
                    #冒烟测试只跑3组
                    if TRAIN_MODE == 'smoke':
                        selected_combinations = random.sample(all_combinations, min(3, len(all_combinations)))
                    else:
                        selected_combinations = all_combinations
                    do_log.info(f"{name}选择的训练参数为: {selected_combinations}")

                    for params in selected_combinations:
                        params_list = [params]
                        train_and_assess_project(project_name, current_file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)
                    assess.home()
            
