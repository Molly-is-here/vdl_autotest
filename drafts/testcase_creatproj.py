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
        #open_Software.open_sofeware(r".\VDL.exe")
        #open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
        #open_Software.click_maximize() 
        '''开启线程，监控性能''' 
          
        
        # header = ['图片名称','训练时长/s','评估时长/s','总CT时间/s']  #设置表头
        # with open('CT时间记录.csv', 'a', newline='') as f:
        #         writer = csv.writer(f)
        #         writer.writerow(header)#将表头写入表格


        for i in range(1):
            for item in save_path.project_list:
            #根据传入的item判断算法类型，找到相应的数据集
                if item ==save_path.seg:
                    dataset = save_path.seg_project
                    name = 'SEG'
                if item == save_path.cls:
                    dataset = save_path.cls_project
                    name = 'CLS'
                if item == save_path.det:
                    dataset = save_path.det_project
                    name = 'DET'
                if item == save_path.ocr:
                    dataset = save_path.ocr_project
                    name = 'OCR'
                if item == save_path.uad:
                    dataset = save_path.uad_project
                    name = 'UAD'
           
                for file in search_file.get_file(dataset):                  

                    '''方案管理页面'''
                    management.create_project()
                    project_name = management.input_name(name)  
                    management.create_model(item)

                    '''数据管理页面'''
                    data.add_file(dataset,file)
                    #data.finish_button()

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
                                       
                    '''训练时长监控'''
                    training_start_time = time.time()
                    '''开启线程，监控资源使用情况'''
                    training.star_training()  
                    event = threading.Event()
                    status = [0]
                    t = threading.Thread(target=get_training_utilization, args=(project_name,status,event)) 
                    t.start()                                                        
                    training.review_assess()  
                    status[0] = 1
                    event.set()    
                    t.join()         
                    training_end_time = time.time()
                    training_spend_time = int(training_end_time - training_start_time)  #训练时长
                    
                    
                    '''模型评估页面'''
                    #assess.model_assess()
                    '''评估时长监控'''
                    # assess_start_time = time.time()
                    # status = assess.assess_success() 
                    # assess_end_time = time.time()
                    # assess_spend_time = int(assess_end_time - assess_start_time) #评估时长                 

                    # '''将时长记录至表格'''
                    num = i
                    # screenshot_1 =  file + '_' + str(num)
                    # ct_time = training_spend_time + assess_spend_time
                    # with open('CT时间记录.csv', 'a', newline='') as f:
                    #     writer = csv.writer(f)
                    #     writer.writerow([screenshot_1,training_spend_time,assess_spend_time,ct_time])

                    '''导出模型'''
                    assess.more_button()
                    assess.export_model()
                    screenshot_name =  file + '_' + str(num) + '.png'  #将当前评估结果截图
                    airtest_method.screenshot(screenshot_name)

                    '''导出报告'''
                    # assess.export_report()
                    # airtest_method.operate_sleep(10.0)
                    # open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
                    '''关闭方案'''
                    assess.template_file()
                    assess.template_close()
                    # assess.home()  #返回home键
            return True

if __name__ == "__main__":
     testcase01()
