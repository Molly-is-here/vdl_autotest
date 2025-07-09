__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from common.Airtest_method import airtest_method 
from pages.management_page import management
from tools.monitoring import *
from tools.create_html import create_html_file
import threading
from PIL import Image
from VDL_autotest.tools.ocr import ocr_organize
from pages.infering_page import infering
from elements.public_control import light_control

auto_setup(__file__)
def testcase02():
    for item in save_path.project_list:
        #根据传入的item判断算法类型，找到相应的数据集
        if item ==save_path.seg:
            dataset = save_path.seg_project
            name = 'SEG_infer'
        if item == save_path.cls:
            dataset = save_path.cls_project
            name = 'CLS_infer'
        if item == save_path.det:
            dataset = save_path.det_project
            name = 'DET_infer'
        if item == save_path.ocr:
            dataset = save_path.ocr_project
            name = 'OCR_infer'
        if item == save_path.uad:
            dataset = save_path.uad_project
            name = 'UAD_infer'
                            
        '''方案管理页面'''
        management.open_project(dataset)
        management.click_project()

        '''模型推理页面'''
        infering.model_infering()

        '''导入图片'''
        file = 'sources'
        infering.images_input(dataset,file)   

        '''开始推理'''
        infering.begin_infering()
        event = threading.Event()
        status = [0]
        t = threading.Thread(target=get_infer_utilization, args=(name,status,event,save_path.base_path)) 
        t.start() 
        infering.review_infering()
        status[0] = 1
        event.set()    
        t.join() 
        

        '''关闭方案'''
        airtest_method.operate_sleep()
        airtest_method.touch_button(light_control.home_button)
        # assess.template_file()
        # assess.template_close()

if __name__ == "__main__":
     testcase02()
