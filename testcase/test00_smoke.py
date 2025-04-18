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
from tools.radom_character import radom_Name
import pytest
import allure
import os

auto_setup(__file__)
LEARNING_TIMES = '10'
COLOR = 'light'

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

def create_and_train_project(project_name, project_path, dataset, file_path, params_list=None, special_params=None, name=None):
    """创建项目并进行训练评估的通用流程
    Args:
        project_name: 项目名称，如'CLSOCV'
        project_path: 项目类型图片路径，如save_path.clsocv
        dataset: 数据集路径
        file_path: 文件路径
        params_list: 参数列表
        special_params: 特殊参数
        name: 算法类型标识，如'CLSOCV'
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
            training.uad_moudle_type()
        if 'uad_model' in special_params:
            training.uad_choice_model(special_params['uad_model'])
        if 'seq_study' in special_params:
            training.seq_set_study(special_params['seq_study'])
        if 'ocv_study' in special_params:
            training.ocv_set_study(special_params['ocv_study'])

    training.star_training(COLOR)
    
    # 根据项目类型构建不同的日志路径
    if name == 'CLSOCV':
        path = os.path.join(save_path.project_save_path, project_name, "output", "2", "cls", "vimo-train.log")
    elif name == 'UADOCV':
        path = os.path.join(save_path.project_save_path, project_name, "output", "2", "uad", "vimo-train.log")
    else:
        path = os.path.join(save_path.project_save_path, project_name, "output", "2", "vimo-train.log")
        
    training.training_success(path, project_name)

    # 模型评估页面
    assess.model_assess(COLOR)
    assess.assess_success(COLOR)

    # 调用SDK
    assess.more_button()
    assess.export_SDK(os.getcwd())
    assess.unzip_SDK()
    assess.copy_SDK_dll()
    assess.run_SDK(file_path, project_name)

    # 关闭方案
    assess.template_file()
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
                count = min(len(scaling_selection), len(color_mode))
                for i in range(count):
                    params_list = radom_Name.get_params(scaling_selection, color_mode)
                    for file in search_file.get_file(dataset):
                        file_path = str(os.path.join(dataset, file))
                        create_and_train_project(name, save_path.seqocr, dataset, file_path, params_list, 
                                              {'seq_study': LEARNING_TIMES}, name)

        elif name == 'UAD':
            show_type = [light_control.uad_seg, light_control.uad_cls]
            for file in search_file.get_file(dataset):
                for module in show_type:
                    UADmodel_selection = [light_control.modelB, light_control.modelA_low_power, 
                                        light_control.modelA_high_power]
                    for model_type in UADmodel_selection:
                        with allure.step(f'{name}算法冒烟'):
                            file_path = str(os.path.join(dataset, file))
                            create_and_train_project(name, save_path.uad, dataset, file_path, None,
                                                  {'uad_module': module == light_control.uad_seg,
                                                   'uad_model': model_type}, name)

        elif name == 'OCR':
            for file in search_file.get_file(dataset):
                with allure.step(f'{name}算法冒烟'):
                    count = min(len(model_selection), len(scaling_selection), len(color_mode))
                    for i in range(count):
                        params_list = radom_Name.get_params(model_selection, scaling_selection, color_mode)
                        file_path = str(os.path.join(dataset, file))
                        create_and_train_project(name, save_path.ocr, dataset, file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)

        elif name == 'CLS':
            for file in search_file.get_file(dataset):
                with allure.step(f'{name}算法冒烟'):
                    count = min(len(model_selection), len(scaling_selection), len(color_mode))
                    for i in range(count):
                        params_list = radom_Name.get_params(model_selection, scaling_selection, color_mode)
                        file_path = str(os.path.join(dataset, file))
                        create_and_train_project(name, save_path.cls, dataset, file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)

        elif name == 'DET':
            DET_scaling_selection = [0, light_control.equal_size]
            for file in search_file.get_file(dataset):
                with allure.step(f'{name}算法冒烟'):
                    count = min(len(model_selection), len(DET_scaling_selection), len(color_mode))
                    for i in range(count):
                        params_list = radom_Name.get_params(model_selection, DET_scaling_selection, color_mode)
                        file_path = str(os.path.join(dataset, file))
                        create_and_train_project(name, save_path.det, dataset, file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)

        elif name == 'SEG':
            for file in search_file.get_file(dataset):
                with allure.step(f'{name}算法冒烟'):
                    count = min(len(model_selection), len(scaling_selection), len(color_mode))
                    for i in range(count):
                        params_list = radom_Name.get_params(model_selection, scaling_selection, color_mode)
                        file_path = str(os.path.join(dataset, file))
                        create_and_train_project(name, save_path.seg, dataset, file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)

        elif name == 'CLSOCV':
            for file in search_file.get_file(dataset):
                with allure.step(f'{name}算法冒烟'):
                    count = min(len(model_selection), len(scaling_selection), len(color_mode))
                    for i in range(count):
                        params_list = radom_Name.get_params(model_selection, scaling_selection, color_mode)
                        file_path = str(os.path.join(dataset, file))
                        create_and_train_project(name, save_path.clsocv, dataset, file_path, params_list,
                                              {'ocv_study': LEARNING_TIMES}, name)

        elif name == 'UADOCV':
            for file in search_file.get_file(dataset):
                with allure.step(f'{name}算法冒烟'):
                    count = min(len(model_selection), len(scaling_selection), len(color_mode))
                    for i in range(count):
                        params_list = radom_Name.get_params(model_selection, scaling_selection, color_mode)
                        file_path = str(os.path.join(dataset, file))
                        create_and_train_project(name, save_path.uadocv, dataset, file_path, params_list,
                                              {'study_times': LEARNING_TIMES}, name)
            
