__author__ = "yunliu"
from airtest.core.api import *
from elements.elements_path import save_path
from pages.management_page import management
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from elements.public_control import light_control
from common.Airtest_method import airtest_method
from pages.open_sofrware import open_Software
from tools.docqq import *
from pathlib import Path
import pytest
import allure

auto_setup(__file__)
learning_times = '30'
color = 'light'

@allure.title('八类算法对比测试')
@pytest.mark.smoke
def test_compatible_smoke():
   for item in save_path.project_list:
        dataset_list = []
        #根据传入的item判断算法类型，找到相应的数据集        
        if item ==save_path.seg:
            name = 'SEG'
            folder_path = Path(save_path.compare_project[2])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[2],folder_name) 
                    dataset_list.append(dataset)   
        if item == save_path.cls:
            name = 'CLS'
            folder_path = Path(save_path.compare_project[0])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[0],folder_name) 
                    dataset_list.append(dataset)   
        if item == save_path.det:
            name = 'DET'
            folder_path = Path(save_path.compare_project[1])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[1],folder_name)
                    dataset_list.append(dataset)
        if item == save_path.ocr:
            name = 'OCR'
            folder_path = Path(save_path.compare_project[3])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[3],folder_name) 
                    dataset_list.append(dataset)   
        if item == save_path.uad:
            name = 'UAD'
            folder_path = Path(save_path.compare_project[4])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[4],folder_name) 
                    dataset_list.append(dataset)  
        if item == save_path.seqocr:
            name = 'SEQOCR'
            folder_path = Path(save_path.compare_project[5])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[5],folder_name) 
                    dataset_list.append(dataset)  
        if item == save_path.uadocv:
            name = 'UADOCV'
            folder_path = Path(save_path.compare_project[6])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[6],folder_name) 
                    dataset_list.append(dataset)
        if item == save_path.clsocv:
            name = 'CLSOCV'
            folder_path = Path(save_path.compare_project[7])
            for entry in folder_path.iterdir():
                if entry.is_dir():
                    folder_name = entry.name
                    dataset = os.path.join(save_path.compare_project[7],folder_name) 
                    dataset_list.append(dataset)

        for project_path in dataset_list:
            dataset_name = os.path.basename(project_path)
            with allure.step(f'当前运行{dataset_name}方案'):
                '''方案管理页面'''
                management.open_project(project_path)
                management.click_project()

                '''图像标注页面'''
                mark.image_label(color)

                # '''模型训练页面'''
                training.model_training(color)
                if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'SEG' or name == 'SEQOCR': 
                    training.add_card(color)
                    if name == 'SEQOCR':
                        training.seq_set_study(learning_times)
                    else:
                        training.set_study(learning_times,color)
                    training.cut_benchsize(color)
                else:
                    if name == 'UAD' or name == 'UADOCV' or name == 'CLSOCV':
                        training.add_card(color) 
                    if name == 'UADOCV':
                        training.set_study(learning_times,color)
                    if name == 'CLSOCV':
                        training.ocv_set_study(learning_times)
                
                training.star_training(color)    #开始训练
                
                '''模型评估页面'''
                assess.model_assess(color)
                assess.assess_success(color)
                if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'SEG' or name == 'SEQOCR' or name == 'UADOCV' or name == 'CLSOCV':
                    assess.assess_done() 
                else:
                    if not airtest_method.check_exit(light_control.sensitive_area,'FALSE',360000) :
                        assert False,'评估未完成'

                airtest_method.operate_sleep(15.0)

                screenshot_images = []
                if name == 'SEG':
                    image_screenshot = os.path.join(save_path.base_path, f"{dataset_name}图像级别.jpg")
                    airtest_method.screenshot(image_screenshot)
                    screenshot_images.append(image_screenshot)
                    
                    #类别级别截图
                    airtest_method.touch_button(light_control.type_image)
                    type_screenshot = os.path.join(save_path.base_path, f"{dataset_name}类别级别.jpg")
                    airtest_method.screenshot(type_screenshot)
                    screenshot_images.append(type_screenshot)
                    
                    #像素级别截图
                    airtest_method.touch_button(light_control.pixel_image)
                    pixel_screenshot = os.path.join(save_path.base_path, f"{dataset_name}像素级别.jpg")
                    airtest_method.screenshot(pixel_screenshot)
                    screenshot_images.append(pixel_screenshot)

                if name == 'DET':
                    image_screenshot = os.path.join(save_path.base_path, f"{dataset_name}图像级别.jpg")
                    airtest_method.screenshot(image_screenshot)
                    screenshot_images.append(image_screenshot)

                    #类别级别截图
                    airtest_method.touch_button(light_control.type_image)
                    type_screenshot = os.path.join(save_path.base_path, f"{dataset_name}类别级别.jpg")
                    airtest_method.screenshot(type_screenshot)
                    screenshot_images.append(type_screenshot)

                if name == 'OCR':
                    image_screenshot = os.path.join(save_path.base_path, f"{dataset_name}图像级别.jpg")
                    airtest_method.screenshot(image_screenshot)
                    screenshot_images.append(image_screenshot)

                    #字符级别截图
                    airtest_method.touch_button(light_control.ocr_image)
                    ocr_screenshot = os.path.join(save_path.base_path, f"{dataset_name}字符级别.jpg")
                    airtest_method.screenshot(ocr_screenshot)

                    screenshot_images.append(ocr_screenshot)

                if name == 'SEQOCR':
                    image_screenshot = os.path.join(save_path.base_path, f"{dataset_name}图像级别.jpg")
                    airtest_method.screenshot(image_screenshot)
                    screenshot_images.append(image_screenshot)

                    #内容级别截图
                    airtest_method.touch_button(light_control.content_image)
                    content_screenshot = os.path.join(save_path.base_path, f"{dataset_name}内容级别.jpg")
                    airtest_method.screenshot(content_screenshot)
                    screenshot_images.append(content_screenshot)

                    #类别级别截图
                    airtest_method.touch_button(light_control.type_image)
                    type_screenshot = os.path.join(save_path.base_path, f"{dataset_name}类别级别.jpg")
                    airtest_method.screenshot(type_screenshot)
                    screenshot_images.append(type_screenshot)

                if name == 'UAD':
                    project_screenshot = os.path.join(save_path.base_path, f"{dataset_name}项目级别.jpg")
                    airtest_method.screenshot(project_screenshot)
                    screenshot_images.append(project_screenshot)

                    # #切换为类别级别
                    # airtest_method.touch_button(light_control.change_type_image)
                    # change_type_image = os.path.join(save_path.base_path, f"{dataset_name}类别级别.jpg")
                    # airtest_method.screenshot(change_type_image)
                    # screenshot_images.append(change_type_image)

                if name == 'CLS':
                    type_screenshot = os.path.join(save_path.base_path, f"{dataset_name}类别级别.jpg")
                    airtest_method.screenshot(type_screenshot)
                    screenshot_images.append(type_screenshot)

                if name == 'UADOCV' or name == 'CLSOCV':
                    #字符级别截图
                    airtest_method.touch_button(light_control.ocr_image)
                    ocr_screenshot = os.path.join(save_path.base_path, f"{dataset_name}字符级别.jpg")
                    airtest_method.screenshot(ocr_screenshot)
                    screenshot_images.append(ocr_screenshot)
                    airtest_method.operate_sleep()

                    airtest_method.touch_button(light_control.type_image)
                    type_screenshot = os.path.join(save_path.base_path, f"{dataset_name}类别级别.jpg")
                    airtest_method.screenshot(type_screenshot)
                    screenshot_images.append(type_screenshot)

                ct_screenshot = os.path.join(save_path.base_path, f"{dataset_name}评估完成.png") 
                airtest_method.screenshot(ct_screenshot)
                # create_html_file("V0.9.0",dataset_name,screenshot_images)
                content = ["","V1.4.0.5",dataset_name]
                run("https://docs.qq.com/sheet/DY2ZHWnFlQXplWUFv?tab=2vwj28&_t=1726731212102&u=46f694f1d02b448b9de7e4eb8e458757",content,screenshot_images)
                
                '''HOME键返回方案管理页面'''
                open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
                airtest_method.key_event("^w")  #关闭当前窗口
                airtest_method.operate_sleep()
