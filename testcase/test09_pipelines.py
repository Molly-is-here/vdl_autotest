__author__ = "yunliu"
import pytest
import allure
from pages.management_page import management
from pages.data_page import data
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from common.Airtest_method import airtest_method
from elements.public_control import label_control
from elements.pipelines import *
from common.handle_log import do_log
from enum import Enum

cls_pipelines = [cls_seq, cls_det, cls_seg]
det_pipelines = [det_OCR]
seg_pipellines = [seg_seq, seg_OCR, seg_seg, seg_det]
seq_pipelines = [seq_seg, seq_ocr]
uad_pipelines = [uad_det, uad_seg1, uad_seg2]
roi_pipelines = [roi_OCR,roi_seg]
rapid_pipelines = [rapid_det, rapid_OCR, rapid_seg]
LEARNING_TIMES = '2'
COLOR = 'light'
static_path = os.path.join(save_path.base_path, 'static')

class ModuleType(Enum):
    PRE = 1
    POST = 2

@allure.feature('串联方案测试')
def create_proj(name):
    """创建方案"""
    # 创建方案并输入名称
    management.create_project(COLOR)
    management.input_name(name, COLOR)
    # 选择串并联方案类型
    management.choice_project_type(COLOR)  
    # 点击创建按钮
    management.create_success(COLOR)
    do_log.info('方案成功新建,用例执行成功')

def create_module_and_import_label(type, file_path, module_type, module):
    """创建模块并导入标注
    
    Args:
        type: 模块类型
        file_path: 文件路径
        module_type: 模块类型 (ModuleType.PRE 或 ModuleType.POST)
        module: 模块对象
    """
    data.project_flow(COLOR)
    data.add_module(module)
    
    # 快速定位模块的前置模块不需要导入标注
    if (type == rapid_det or type == rapid_seg or type == rapid_OCR or 
        type == roi_seg or type == roi_OCR) and module_type == ModuleType.PRE:
        data.project_flow(COLOR)
        return
        
    # 其他情况需要导入标注
    mark.image_label(COLOR)  # 点击图像标注按钮关闭方案流程画布
    label_path = os.path.join(file_path, f'labels{module_type.value}')
    mark.import_label(label_path, COLOR)
    do_log.info(f'{"前置" if module_type == ModuleType.PRE else "后置"}模块标注{label_path}导入成功')

def close_project():
    """关闭方案"""         
    assess.template_file()
    assess.template_close()
    airtest_method.operate_sleep(10.0)

def pre_train_and_assess_done(type, LEARNING_TIMES):
    """前置模块训练评估完成"""
    mark.auto_divide(COLOR)
    training.model_training(COLOR)
    training.add_card(COLOR)
    if type == seq_seg or type == seq_ocr:
        training.seq_set_study(LEARNING_TIMES)
        training.cut_benchsize(COLOR)
    elif type == uad_det or type == uad_seg1 or type == uad_seg2:
        pass
    else:
        training.set_study(LEARNING_TIMES, COLOR)
        training.cut_benchsize(COLOR)

    training.star_training(COLOR)
    assess.model_assess(COLOR)
    assess.assess_success(COLOR) 

def post_train_and_assess_done(type, LEARNING_TIMES):
    """后置模块训练评估完成"""
    mark.auto_divide(COLOR)
    training.model_training(COLOR)
    training.add_card(COLOR)
    if type == seg_seq or type == cls_seq:
        training.seq_set_study(LEARNING_TIMES)
    else:
        training.set_study(LEARNING_TIMES, COLOR)
    training.cut_benchsize(COLOR)
    training.star_training(COLOR)
    assess.model_assess(COLOR)
    assess.assess_success(COLOR) 

def dynamic_selection(mask_operation):
    """添加屏蔽区域"""
    # 动态正选
    if mask_operation == 'Normal':
        airtest_method.touch_button(label_control.masking_area)
        airtest_method.touch_button(label_control.dynamic_selection)
    # 动态反选
    elif mask_operation == 'Inverted':
        airtest_method.touch_button(label_control.masking_area)
        airtest_method.touch_button(label_control.dynamic_deselection)

def painting_area(template_name, points, v1, v2, v3, number):
    """绘制基准图像"""
    for i in range(len(template_name)):
        data.add_template(template_name[i], points[i])
        do_log.info(f'v1:{v1[i]}, v2:{v2[i]}, v3:{v3[i]}')
        mark.rapid_rectangle_marking(v1[i], v2[i], v3[i])
        data.rapid_single_test()
        data.set_filter_parameter(number, points[i])
        data.rapid_full_test()
        do_log.info(f'模板绘制成功')

def proportional_splitting(sizes):
    """比例划分ROI模块"""
    try:
        data.change_ROI_mode()
        data.splitting_number(sizes[0], sizes[1])
        data.splitting_size(sizes[2], sizes[3])
        data.splitting_interval(sizes[4], sizes[5])
        data.splitting_displacement(sizes[6], sizes[7])
    except Exception as e:
        do_log.error(f"ROI参数设置失败: {str(e)}")
        raise

def process_pipeline(name, file_path, type, pre_module, post_module, 
                    template_name=None, points=None, v1=None, v2=None, v3=None, 
                    number=None, sizes=None):
    """处理单个pipeline流程"""
    create_proj(name)
    do_log.info(f"当前创建的pipelines为{name}")
    data.add_file(file_path)
    do_log.info(f'成功导入{name}数据集')
    # 创建前置模块并导入标注
    create_module_and_import_label(type, file_path, ModuleType.PRE, pre_module)
    if type == rapid_det or type == rapid_seg or type == rapid_OCR:
        painting_area(template_name, points, v1, v2, v3, number)
    elif type == roi_seg or type == roi_OCR:
        proportional_splitting(sizes)
    else:
        pre_train_and_assess_done(type, LEARNING_TIMES)
    # 添加后置模块并导入标注
    create_module_and_import_label(type, file_path, ModuleType.POST, post_module)
    if type == seg_seg:
        dynamic_selection('Inverted')    
    post_train_and_assess_done(type, LEARNING_TIMES) 
    close_project()

def zidingyi_roi_module(sizes):
    """自定义ROI模块"""
    # sizes = ['92.93', '40.47', '-0.32', '-13.22', '-0.52', '11.71']
    data.setting_size(sizes[0], sizes[1])
    data.setting_displacement(sizes[2], sizes[3])
    # 新增ROI
    data.add_roi()
    data.setting_size(sizes[0], sizes[1])
    data.setting_displacement(sizes[4], sizes[5])
    do_log.info('自定义ROI设置成功')

# @allure.title('文件夹导入快速定位串联数据集')
# @pytest.mark.smoke
# def test_rapid_pipelines():
#     """快速定位模版串联pipelines"""
#     for pipelines in rapid_pipelines: 
#         do_log.info(f"Processing pipeline: {pipelines.name}")
#         do_log.info(f"Points: {pipelines.points}")
#         if pipelines == rapid_OCR:
#             template_name = ['auto_match_1', 'auto_match_2']
#             template_points = [(1844, 314), (1844, 358)]
#             v1 = [pipelines.points[0][0], pipelines.points[1][0]]
#             v2 = [pipelines.points[0][1], pipelines.points[1][1]]
#             v3 = [pipelines.points[0][2], pipelines.points[1][2]]
#             process_pipeline(
#                 name=pipelines.name,
#                 file_path=pipelines.file_path,
#                 type=pipelines,
#                 pre_module=pipelines.pre_module,
#                 post_module=pipelines.post_module,
#                 template_name=template_name,
#                 points=template_points,
#                 v1=v1,
#                 v2=v2,
#                 v3=v3,
#                 number=pipelines.number
#             )
#         else:
#             template_name = ['auto_match']
#             template_points = [(1844, 314)]
#             # 对于单个模板，将points转换为列表形式
#             v1 = [pipelines.points[0]]
#             v2 = [pipelines.points[1]]
#             v3 = [pipelines.points[2]]
#             process_pipeline(
#                 name=pipelines.name,
#                 file_path=pipelines.file_path,
#                 type=pipelines,
#                 pre_module=pipelines.pre_module,
#                 post_module=pipelines.post_module,
#                 template_name=template_name,
#                 points=template_points,
#                 v1=v1,
#                 v2=v2,
#                 v3=v3,
#                 number=pipelines.number
#             )

# @allure.title('文件夹导入分割串联数据集')
# @pytest.mark.smoke
# def test_seg_pipelines():
#     """分割模块串联pipelines测试"""
#     for pipelines in seg_pipellines: 
#         process_pipeline(
#             name=pipelines.name,
#             file_path=pipelines.file_path,
#             type=pipelines,
#             pre_module=pipelines.pre_module,
#             post_module=pipelines.post_module
#         )
            
# @allure.title('文件夹导入检测串联数据集')
# @pytest.mark.smoke
# def test_det_pipelines():
#     """检测模块串联pipelines测试"""
#     for pipelines in det_pipelines: 
#         process_pipeline(
#             name=pipelines.name,
#             file_path=pipelines.file_path,
#             type=pipelines,
#             pre_module=pipelines.pre_module,
#             post_module=pipelines.post_module
#         )

# @allure.title('文件夹导入分类串联数据集')
# @pytest.mark.smoke
# def test_cls_pipelines():
#     """分类模块串联pipelines测试"""
#     for pipelines in cls_pipelines: 
#         process_pipeline(
#             name=pipelines.name,
#             file_path=pipelines.file_path,
#             type=pipelines,
#             pre_module=pipelines.pre_module,
#             post_module=pipelines.post_module
#         )

# @allure.title('文件夹导入字符串串联数据集')
# @pytest.mark.smoke
# def test_seq_pipelines():
#     """字符串模块串联pipelines测试"""
#     for pipelines in seq_pipelines: 
#         process_pipeline(
#             name=pipelines.name,
#             file_path=pipelines.file_path,
#             type=pipelines,
#             pre_module=pipelines.pre_module,
#             post_module=pipelines.post_module
#         )

# @allure.title('文件夹导入无监督串联数据集')
# @pytest.mark.smoke
# def test_uad_pipelines():
#     """无监督模块串联pipelines测试"""
#     for pipelines in uad_pipelines: 
#         process_pipeline(
#             name=pipelines.name,
#             file_path=pipelines.file_path,
#             type=pipelines,
#             pre_module=pipelines.pre_module,
#             post_module=pipelines.post_module
#         )

@allure.title('文件夹导入ROI串联数据集')
@pytest.mark.smoke
def test_roi_pipelines():
    """ROI模块串联pipelines测试"""
    for pipelines in roi_pipelines: 
        # zidingyi_sizes = ['95.65', '48.08', '0.31', '-21.61', '0.87', '17.56']
        splitting_sizes = ['1', '2', '47.66', '99.00', '0.00', '2.00', '-24.83', '0.49']
        process_pipeline(
            name=pipelines.name,
            file_path=pipelines.file_path,
            type=pipelines,
            pre_module=pipelines.pre_module,
            post_module=pipelines.post_module,
            sizes=splitting_sizes
        )
@allure.title('关闭方案')
@pytest.mark.smoke
def test_close_project():
    """关闭方案"""
    close_project()