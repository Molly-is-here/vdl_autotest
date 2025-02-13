__author__ = "yunliu"
import pytest
import allure
from common.Airtest_method import airtest_method
from elements.public_control import light_control
from common.handle_log import do_log
from pages.data_page import data
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from test02_data import test_add_file
from airtest.core.api import *
from elements.elements_path import save_path

model_selection = [light_control.high_power,light_control.low_power]
scaling_selection = [light_control.equal_size,light_control.zidingyi_size]
input_size = ['512']
color = 'light'
@allure.feature('模型训练页面')
@allure.title('切换至模型训练页面')
@pytest.mark.smoke
def test_training_page():
    with allure.step(f'点击模型训练tab按钮'):
        training.model_training(color)
    do_log.info('模型训练页面成功切换,用例执行成功')

@allure.title('新建训练小卡片') 
@pytest.mark.smoke
def test_add_card():
    with allure.step(f'点击新的训练按钮'):
        training.add_card(color)
    do_log.info('成功新建卡片,用例执行成功')

@allure.title('重命名训练小卡片') 
@pytest.mark.smoke
def test_rename():    
    with allure.step(f'重命名'):
        input_name = '自動化創建的card'
        training.renamed_card(input_name,(135,220))
    do_log.info('卡片成功重命名,用例执行成功')

@allure.title('修改备注') 
@pytest.mark.smoke
def test_edit_comment():
    with allure.step(f'修改备注'):
        input_comment = 'have_a_nice_day*@▽@*耶耶'
        training.edit_comment(input_comment)
    do_log.info('卡片备注成功修改,用例执行成功')

@allure.title('复制训练小卡片') 
@pytest.mark.smoke
def test_copy():
    with allure.step(f'点击复制按钮'):
        training.copy_card()
    do_log.info('成功复制卡片,用例执行成功')
        
@allure.title('删除卡片') 
@pytest.mark.smoke
def test_delete():  
    with allure.step(f'点击删除卡片按钮'):
        training.delete_card()
    do_log.info('成功删除卡片，用例执行成功')

@allure.title('设置为模板并开启训练')                
@pytest.mark.smoke
def test_set_template():
    with allure.step(f'先设置训练参数'):
        training.set_study('30',color)           
        training.cut_benchsize(color)
    with allure.step(f'训练参数设置为模板'):
        training.set_template()
    with allure.step(f'使用模版开启训练'):
        airtest_method.touch_button(light_control.add_card)
        airtest_method.touch_button(light_control.create_using_template)
    with allure.step(f'点击开始训练'):
        training.star_training(color)
    with allure.step(f'判断是否训练成功'):
        with open('project_name.txt', 'r') as file:
            content = file.read()
        path = os.path.join(save_path.project_save_path, content, "output", "4", "vimo-train.log")
        training.training_success(path,content) 
    with allure.step(f'判断是否评估成功'):  
        assess.model_assess(color)
        if not airtest_method.check_exit(light_control.infering_finished,'FALSE',360000) :
            assert False,'评估未完成'
        else:
            airtest_method.operate_sleep()
    do_log.info('模型训练成功，用例执行成功')

@allure.title('分割算法自动标注')   
@pytest.mark.smoke
def test_seg_auto_marking():
    with allure.step(f'切换回标注页面'):
        mark.image_label(color)
    with allure.step(f'点击分割算法自动标注按钮'):
        airtest_method.key_event('{DOWN}')
        mark.auto_marking()
    do_log.info('分割算法自动标注完成')

@allure.title('增量训练')   
@pytest.mark.smoke
def test_add_training():  
    with allure.step(f'选择增量训练'): 
        training.model_training(color)
        training.add_training()
        airtest_method.operate_sleep()
    with allure.step(f'返回数据管理页面'):
        data.data_management_page()
    with allure.step(f'通过导入文件夹导入图像+标注'):
        test_add_file()
    with allure.step(f'图像标注页面重新划分数据集'):
        mark.image_label(color)
        mark.auto_divide(color)
    with allure.step(f'返回模型训练页面开始增量训练'):
        training.model_training(color)
    with allure.step(f'点击开始训练'):
        training.star_training(color)
    with allure.step(f'确认开启增量训练'):
        airtest_method.touch_button(light_control.training_okbutton)
    with allure.step(f'判断是否训练成功'):
        with open('project_name.txt', 'r') as file:
            content = file.read()
            airtest_method.operate_sleep()
        path = os.path.join(save_path.project_save_path, content, "output", "5", "vimo-train.log")
        training.training_success(path,content) 
    with allure.step(f'判断是否评估成功'):  
        assess.model_assess(color)
        if not airtest_method.check_exit(light_control.infering_finished,'FALSE',360000) :
            assert False,'评估未完成'
        else:
            airtest_method.operate_sleep()
            do_log.info('模型增量训练成功，用例执行成功')

@allure.title('特征置为背景')
@pytest.mark.smoke
def test_set_background(): 
    with allure.step(f'切换回标注页面'):
        mark.image_label(color)
    with allure.step(f'特征1置为背景'):
        mark.set_background((1701,507))
    with allure.step(f'切换至模型训练页面'):
        airtest_method.operate_sleep(2.0)
        training.model_training(color)
    with allure.step(f'使用模版开启训练'):
        airtest_method.touch_button(light_control.add_card)
        airtest_method.touch_button(light_control.create_using_template)
        training.renamed_card('特征1置为背景',(135,220))
    with allure.step(f'点击开始训练'):
        training.star_training(color)
    with allure.step(f'判断是否训练成功'):
        with open('project_name.txt', 'r') as file:
            content = file.read()
        path = os.path.join(save_path.project_save_path, content, "output", "6", "vimo-train.log")
        training.training_success(path,content) 
    with allure.step(f'判断是否评估成功'):  
        training.review_assess()
        if not airtest_method.check_exit(light_control.infering_finished,'FALSE',360000) :
            assert False,'评估未完成'
        else:
            airtest_method.operate_sleep()
    do_log.info('模型训练成功，用例执行成功')

@allure.title('标签硬合并')
@pytest.mark.smoke
def test_hard_merge_label():
    with allure.step(f'切换回标注页面'):
        mark.image_label(color)
    with allure.step(f'点击标签合并'):
        mark.hard_merge_label((1623,557),'3')
    with allure.step(f'切换至模型训练页面'):
        airtest_method.operate_sleep(2.0)
        training.model_training(color)
    with allure.step(f'使用模版开启训练'):
        airtest_method.touch_button(light_control.add_card)
        airtest_method.touch_button(light_control.create_using_template)
        training.renamed_card('特征2标签硬合并',(135,220))
    with allure.step(f'点击开始训练'):
        training.star_training(color)
    with allure.step(f'判断是否训练成功'):
        with open('project_name.txt', 'r') as file:
            content = file.read()
        path = os.path.join(save_path.project_save_path, content, "output", "7", "vimo-train.log")
        training.training_success(path,content) 
    with allure.step(f'判断是否评估成功'):  
        training.review_assess()
        if not airtest_method.check_exit(light_control.infering_finished,'FALSE',360000) :
            assert False,'评估未完成'
        else:
            airtest_method.operate_sleep()
    do_log.info('模型训练成功，用例执行成功')

@allure.title('标签软合并')
@pytest.mark.smoke
def test_soft_merge_label():
    with allure.step(f'切换回标注页面'):
        mark.image_label(color)
    with allure.step(f'标签3软合并至标签4'):
        mark.soft_merge_label((1688,560),(1688,605))
    with allure.step(f'切换至模型训练页面'):
        airtest_method.operate_sleep(2.0)
        training.model_training(color)
    with allure.step(f'使用模版开启训练'):
        airtest_method.touch_button(light_control.add_card)
        airtest_method.touch_button(light_control.create_using_template)
        training.renamed_card('特征3软合并至特征4',(135,220))
    with allure.step(f'点击开始训练'):
        training.star_training(color)
    with allure.step(f'判断是否训练成功'):
        with open('project_name.txt', 'r') as file:
            content = file.read()
        path = os.path.join(save_path.project_save_path, content, "output", "10", "vimo-train.log")
        training.training_success(path,content) 
    with allure.step(f'判断是否评估成功'):  
        training.review_assess()
        if not airtest_method.check_exit(light_control.infering_finished,'FALSE',360000) :
            assert False,'评估未完成'
        else:
            airtest_method.operate_sleep()
    do_log.info('模型训练成功，用例执行成功')

    
    









    













