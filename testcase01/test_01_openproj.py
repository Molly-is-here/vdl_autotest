__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from common.Airtest_method import airtest_method 
from pages.open_sofrware import open_Software
from pages.management_page import management
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from tools.monitoring import *
from tools.create_html import create_html_file
import threading
from PIL import Image
from tools.ocr_identify import ocr_organize

auto_setup(__file__)

def testcase01():

    # header = ['图片名称','训练时长/s','评估时长/s','总CT时间/s']  #设置表头
    # with open('testcase02_CT时间记录.csv', 'a', newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(header)#将表头写入表格
       
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
                         
        '''方案管理页面'''
        management.open_project(dataset)
        management.click_project()

        '''图像标注页面'''
        mark.image_label()

        '''模型训练页面''' 
        train_count = 0                  
        while train_count < 1:
            train_count += 1
            training.model_training()
            if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'SEG': 
                training.add_card()
                training.set_study()
                training.mouse_move()
                training.zidingyi_button()
                training.cut_benchsize()
            else:
                training.add_card()

            '''训练时长监控'''
            training_start_time = time.time()
            '''开启线程，监控资源使用情况'''
            training.star_training()  
            event = threading.Event()
            status = [0]
            t = threading.Thread(target=get_training_utilization, args=(name,status,event)) 
            t.start()                                                        
            training.review_assess(name)  
            status[0] = 1
            event.set()    
            t.join()         
            training_end_time = time.time()
            training_spend_time = int(training_end_time - training_start_time - 10)  #训练时长

            '''模型评估页面'''
            '''评估时长监控'''
            assess_start_time = time.time()
            status = assess.assess_success() 
            assess_end_time = time.time()
            assess_spend_time = int(assess_end_time - assess_start_time -1) #评估时长 

            ct_time = training_spend_time + assess_spend_time  #总CT时间

            #current_dir = os.getcwd()
            '''图片存储路径'''
            static_path = os.path.join(save_path.base_path, 'static')
            file_name = f"{name}_{train_count}"
            detail_screenshot = os.path.join(static_path, f"{file_name}.png")
            Accuracy_image = os.path.join(static_path, f"{file_name}_Accuracy.png")
            Recall_image = os.path.join(static_path, f"{file_name}_Recall.png")
            mIOU_image = os.path.join(static_path, f"{file_name}_mIOU.png")
            ocr_character = []

            if name == 'UAD':
                assess.change_type()

            airtest_method.screenshot(detail_screenshot)   #全屏截图 
            detail_image =  os.path.join(save_path().base_path,detail_screenshot)  #指定路径
            region_image = Image.open(detail_image)

            if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'UAD':                       
                Accuracy_screenshot = region_image.crop((1488,156,1686,244)) #精确率截图
                Accuracy_screenshot.save(Accuracy_image)

                Recall_screenshot = region_image.crop((1705,158,1903,245)) #召回率截图
                Recall_screenshot.save(Recall_image)

                create_html_file(name,Accuracy_image,Recall_image,mIOU_image,detail_image,train_count,name,training_spend_time,assess_spend_time,ct_time)
                ocr_character = [Accuracy_image,Recall_image]
                ocr_content = ocr_organize(ocr_character)
            else:
                Accuracy_screenshot = region_image.crop((1488,158,1612,245)) #精确率截图 
                Accuracy_screenshot.save(Accuracy_image)

                Recall_screenshot = region_image.crop((1632,158,1758,245)) #召回率截图
                Recall_screenshot.save(Recall_image)

                mIOU_screenshot = region_image.crop((1777,158,1901,245)) #mIOU截图
                mIOU_screenshot.save(mIOU_image)

                create_html_file(name,Accuracy_image,Recall_image,mIOU_image,detail_image,train_count,name,training_spend_time,assess_spend_time,ct_time)
                ocr_character = [Accuracy_image,Recall_image,mIOU_image]
                ocr_content = ocr_organize(ocr_character)    

            '''将内容记录至表格'''
            content = {}
            if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'UAD':
                content = {
                    '训练CT时间：' : training_spend_time,
                    '精确率：' : ocr_content[0],
                    '召回率：' :ocr_content[1]
                }
            else:
                 content = {
                    '训练CT时间：' : training_spend_time,
                    '精确率：' : ocr_content[0],
                    '召回率：' :ocr_content[1],
                    'mIOU: ' : ocr_content[2]
                }
            screenshot_1 =  name + '_' + str(train_count)
            csv_name = name + '.csv'
            with open(csv_name, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([content])

        '''导出模型'''
        assess.more_button()
        assess.export_model()

        '''导出报告'''
        assess.export_report()
        airtest_method.operate_sleep(10.0)
        open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
           
        '''关闭方案'''
        # airtest_method.operate_sleep()
        # airtest_method.touch_button(control.home_button)
        assess.template_file()
        assess.template_close()
                    

if __name__ == "__main__":
     testcase01()