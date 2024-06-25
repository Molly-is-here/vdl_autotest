# -*- encoding=utf8 -*-
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
import threading
auto_setup(__file__)

def testcase01():
        
        for i in range(1):
            for item in save_path.project_list:
                #根据传入的item判断算法类型，找到相应的数据集
                if item ==save_path.seg:
                    dataset = save_path.seg_dataset
                    name = '分割'
                if item == save_path.cls:
                    dataset = save_path.cls_dataset
                    name = '分类'
                if item == save_path.det:
                    dataset = save_path.det_dataset
                    name = '检测'
                if item == save_path.ocr:
                    dataset = save_path.ocr_dataset
                    name = 'OCR'
           
                for file in search_file.get_file(dataset):                  

                    '''方案管理页面'''
                    management.create_project()
                    management.input_name(name)  
                    management.create_model(item)

                    '''数据管理页面'''
                    data.add_file(dataset,file)

                    '''图像标注页面'''
                    mark.image_label()
                    mark.auto_divide()

                    '''模型训练页面'''
                    training.model_training()
                    training.add_card()
                    training.set_study()
                    training.mouse_move()
                    training.zidingyi_button()             
                    training.cut_benchsize()
                                       
                    '''开始训练'''
                    training.star_training()                                                  
                    training.review_assess()    

                    '''模型评估页面'''
                    #assess.model_assess()
                    assess.assess_success()                

                    '''导出模型'''
                    assess.more_button()
                    assess.export_model()

                    '''导出报告'''
                    assess.export_report()
                    airtest_method.operate_sleep(5.0)
                    open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
                    assess.template_file()
                    assess.template_close()
                    assess.home()  #返回home键
            return True

if __name__ == "__main__":
     testcase01()
