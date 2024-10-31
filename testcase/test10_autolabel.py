__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from pages.data_page import data
from pages.management_page import management
from pages.marking_page import mark
from pages.assess_page import assess
from common.handle_log import do_log
from common.Base_method import search_file
import pytest
import allure
import os

auto_setup(__file__)
current_dir = os.getcwd()
color = 'light'

# @allure.title('检测算法自动标注')
# @pytest.mark.smoke
# def test_det_autolabel():  
#     name = 'DET自动标注'  #方案名称
#     item = save_path.det  #方案类型
#     dataset = save_path.det_dataset  #数据集

#     for file in search_file.get_file(dataset):
#         '''方案管理页面'''
#         management.create_project(color)       
#         management.input_name(name,color)  
#         management.create_model(item)

#         '''数据管理页面'''
#         file_path = str(os.path.join(dataset,file))
#         data.add_image(file_path,color)  #添加图像

#         '''图像标注页面'''
#         mark.image_label(color)
#         with allure.step(f'绘制矩形标注'):
#             mark.add_label('自动矩形标注')  #创建标签
#             mark.rectangle_marking((873,400),(973,500))  #绘制矩形标注
#             do_log.info('成功绘制矩形标注')

#         with allure.step(f'合格样本'):
#             mark.acceptable_sample()  #合格样本标注
#             do_log.info('成功标注合格样本')

#         '''关闭方案'''  
#         assess.template_file()
#         assess.template_close()

# @allure.title('分割算法自动标注')
# @pytest.mark.smoke
# def test_seg_autolabel():  
#     name = 'SEG自动标注'  #方案名称
#     item = save_path.seg  #方案类型
#     dataset = save_path.seg_dataset  #数据集

#     for file in search_file.get_file(dataset):
#         '''方案管理页面'''
#         management.create_project(color)       
#         management.input_name(name,color)  
#         management.create_model(item)

#         '''数据管理页面'''
#         file_path = str(os.path.join(dataset,file))
#         data.add_image(file_path,color)  #添加图像

#         '''图像标注页面'''
#         mark.image_label(color)
#         with allure.step(f'绘制多边形标注'):
#             mark.add_label('自动多边形标注')  #创建标签
#             mark.polygon_marking((837,285),(823,348),(891,335))  #多边形标注
#             do_log.info('成功绘制多边形标注')

#         with allure.step(f'绘制折线标注'):
#             mark.add_label('自动折线标注')  #创建标签
#             mark.polyline_marking((946,756),(1011,813),(960,880))  #折线标注
#             do_log.info('成功绘制折线标注')

#         with allure.step(f'绘制屏蔽区域'):
#             mark.masking_area((1056,554),(1013,669),(1120,670))  #屏蔽区域
#             do_log.info('成功绘制屏蔽区域')

#         with allure.step(f'AI标注'):
#             mark.add_label('自动AI标注')  #创建标签
#             mark.AI_marking((814,459),(1058,702),(937,579))  #AI标注区域
#             do_log.info('成功绘制AI标注')

#         with allure.step(f'笔形标注'):
#             mark.add_label('自动笔形标注')  #创建标签
#             mark.pen_marking((821,783),(987,765))  #笔形标注
#             do_log.info('成功绘制笔形标注')

#         with allure.step(f'合格样本'):
#             mark.acceptable_sample()  #合格样本标注
#             do_log.info('成功标注合格样本')

#         '''关闭方案'''  
#         assess.template_file()
#         assess.template_close()

# @allure.title('OCR算法自动标注')
# @pytest.mark.smoke
# def test_OCR_autolabel():  
#     name = 'OCR自动标注'  #方案名称
#     item = save_path.ocr  #方案类型
#     dataset = save_path.ocr_dataset  #数据集

#     for file in search_file.get_file(dataset):
#         '''方案管理页面'''
#         management.create_project(color)       
#         management.input_name(name,color)  
#         management.create_model(item)

#         '''数据管理页面'''
#         file_path = str(os.path.join(dataset,file))
#         data.add_image(file_path,color)  #添加图像

#         '''图像标注页面'''
#         mark.image_label(color)
#         with allure.step(f'绘制矩形标注'):
#             mark.add_label('0')  #创建标签
#             mark.rectangle_marking((689,421),(826,633))  #绘制矩形标注
#             do_log.info('成功绘制矩形标注')

#         with allure.step(f'自动标注'):
#             mark.auto_marking()  #自动标注
#             do_log.info('自动标注完成')

#         '''关闭方案'''  
#         assess.template_file()
#         assess.template_close()

# @allure.title('seq_OCR算法自动标注')
# @pytest.mark.smoke
# def test_seqOCR_autolabel():  
#     name = 'SEQ_OCR自动标注'  #方案名称
#     item = save_path.seqocr  #方案类型
#     dataset = save_path.seqocr_dataset  #数据集

#     for file in search_file.get_file(dataset):
#         '''方案管理页面'''
#         management.create_project(color)       
#         management.input_name(name,color)  
#         management.create_model(item)

#         '''数据管理页面'''
#         file_path = str(os.path.join(dataset,file))
#         data.add_image(file_path,color)  #添加图像

#         '''图像标注页面'''
#         mark.image_label(color)
#         with allure.step(f'绘制矩形标注'):
#             mark.add_label('自动矩形标注')  #创建标签
#             mark.seq_rectangle_marking((1053,616),(964,546),(1003,497))  #矩形标注
#             do_log.info('矩形标注完成')

#         with allure.step(f'绘制环形标注'):
#             mark.add_label('自动环形标注')  #创建标签
#             mark.seq_circle_marking((750,389),(942,376),(1117,560),(953,461))  #环形标注
#             do_log.info('环形标注完成')

#         with allure.step(f'自动标注'):
#             mark.auto_marking()  #自动标注
#             do_log.info('自动标注完成')

#         '''关闭方案'''  
#         assess.template_file()
#         assess.template_close()

@allure.title('分类算法自动标注')
@pytest.mark.smoke
def test_cls_autolabel():  
    name = 'CLS自动标注'  #方案名称
    item = save_path.cls  #方案类型
    dataset = save_path.cls_dataset  #数据集

    for file in search_file.get_file(dataset):
        '''方案管理页面'''
        management.create_project(color)       
        management.input_name(name,color)  
        management.create_model(item)

        '''数据管理页面'''
        file_path = str(os.path.join(dataset,file))
        data.add_image(file_path,color)  #添加图像

        '''图像标注页面'''
        mark.image_label(color)
        with allure.step(f'添加标注'):
            mark.add_label('自动标签')  #创建标签
            mark.add_marking()

        with allure.step(f'合格样本'):
            mark.acceptable_sample()  #合格样本标注
            do_log.info('成功标注合格样本')

        '''关闭方案'''  
        assess.template_file()
        assess.template_close()

@allure.title('无监督算法自动标注')
@pytest.mark.smoke
def test_uad_autolabel():  
    name = 'UAD自动标注'  #方案名称
    item = save_path.uad  #方案类型
    dataset = save_path.uad_dataset  #数据集

    for file in search_file.get_file(dataset):
        '''方案管理页面'''
        management.create_project(color)       
        management.input_name(name,color)  
        management.create_model(item)

        '''数据管理页面'''
        file_path = str(os.path.join(dataset,file))
        data.add_image(file_path,color)  #添加图像

        '''图像标注页面'''
        mark.image_label(color)
        with allure.step(f'OK样本'):
            mark.acceptable_sample()  #OK样本标注
            do_log.info('成功标注OK样本')

        with allure.step(f'NG样本'):
            mark.NG_sample()  #NG样本标注
            do_log.info('成功标注NG样本')

        '''关闭方案'''  
        assess.template_file()
        assess.template_close()
        
        

