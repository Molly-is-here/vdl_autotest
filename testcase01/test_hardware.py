__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from common.Base_method import search_file
from common.Airtest_method import airtest_method 
from pages.open_sofrware import open_Software
from pages.management_page import management
from pages.data_page import data
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from tools.monitoring import *
from tools.create_html import create_html_file
import threading
from PIL import Image
from tools.ocr_identify import ocr_organize
from elements.public_control import control
from pages.infering_page import infering

auto_setup(__file__)
input_size = ['512','1024','1500','2048','2500']

def testcase03():
    for item in save_path.project_list:
        #根据传入的item判断算法类型，找到相应的数据集
        if item ==save_path.seg:
            dataset = save_path.seg_project
            name = 'SEG_Results'
        if item == save_path.cls:
            dataset = save_path.cls_project
            name = 'CLS_Results'
        if item == save_path.det:
            dataset = save_path.det_project
            name = 'DET_Results'
        if item == save_path.ocr:
            dataset = save_path.ocr_project
            name = 'OCR_Results'
        if item == save_path.uad:
            dataset = save_path.uad_project
            name = 'UAD_Results'

        '''方案管理页面'''
        management.open_project(dataset)
        management.click_project()

        '''图像标注页面'''
        mark.image_label()

        '''模型训练页面'''
        training.model_training()

        '''设置训练参数'''
        if name == 'CLS_Results' or name == 'OCR_Results' or name == 'SEG_Results':  #分类/OCR/分割需要自定义图片尺寸&学习次数
            training.add_card()
            training.image_scaling(control.image_scaling) #图像缩放
            airtest_method.operate_sleep()
            airtest_method.touch_button(control.zidingyi_size)

            for size in input_size:
                file_name = name + '_' + size
                airtest_method.touch_button(control.zidingyi_edit_box1) #第一个编辑框
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                airtest_method.input_text(size)

                airtest_method.touch_button(control.zidingyi_edit_box2) #第二个编辑框
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                airtest_method.input_text(size)

                training.set_study() #设置学习次数

                '''开启线程，监控资源使用情况'''
                training.star_training()  
                event = threading.Event()
                status = [0]
                t1 = threading.Thread(target=get_training_utilization, args=(file_name,status,event)) 
                t1.start()                                                        
                training.review_assess()  
                status[0] = 1
                event.set()    
                t1.join()  

                '''模型推理页面'''
                infering.model_infering()

                '''导入图片'''
                file = 'sources'
                infering.images_input(dataset,file)   

                '''开始推理'''
                infering.begin_infering()
                event = threading.Event()
                status = [0]
                t2 = threading.Thread(target=get_infer_utilization, args=(file_name,status,event,save_path.base_path)) 
                t2.start() 
                infering.review_infering()
                status[0] = 1
                event.set()    
                t2.join() 

        elif name == 'UAD_Results':  #无监督算法需要自定义图片尺寸
            training.add_card()
            training.image_scaling(control.uad_image_scaling) #图像缩放
            airtest_method.operate_sleep()
            airtest_method.touch_button(control.zidingyi_size)

            for size in input_size:
                file_name = name + '_' + size
                airtest_method.touch_button(control.zidingyi_edit_box1) #第一个编辑框
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                airtest_method.input_text(size)

                airtest_method.touch_button(control.zidingyi_edit_box2) #第二个编辑框
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                keyevent("{BACKSPACE}")
                airtest_method.input_text(size)

                '''开启线程，监控资源使用情况'''
                training.star_training()  
                event = threading.Event()
                status = [0]
                t1 = threading.Thread(target=get_training_utilization, args=(file_name,status,event)) 
                t1.start()                                                        
                training.review_assess()  
                status[0] = 1
                event.set()    
                t1.join()   

                '''等待模型推理完成'''
                assess.assess_success()
               
                '''开始推理'''
                infering.begin_infering()
                event = threading.Event()
                status = [0]
                t2 = threading.Thread(target=get_infer_utilization, args=(file_name,status,event,save_path.base_path)) 
                t2.start() 
                infering.review_infering()
                status[0] = 1
                event.set()    
                t2.join() 



