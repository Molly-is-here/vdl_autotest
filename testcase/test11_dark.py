import pytest
import allure
from common.handle_log import do_log
from pages.management_page import management
from elements.elements_path import save_path
from pages.data_page import data
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from pages.infering_page import infering
from common.Airtest_method import airtest_method
from elements.public_control import dark_control

color = 'dark'

def add_pipelines_module(path1,path2):
    '''添加串联模块'''
    data.project_flow(color)
    airtest_method.operate_sleep(2.0)
    airtest_method.touch_button(dark_control.data_source)
    airtest_method.touch_button(dark_control.seg_module)
    data.project_flow(color)
    mark.import_label(path1,color)
    mark.auto_divide(color)
    training.model_training(color)
    training.add_card(color)
    training.set_study('2',color)
    training.cut_benchsize(color)
    training.star_training(color)
    assess.model_assess(color)
    assess.assess_success(color)
    data.project_flow(color)
    airtest_method.touch_button(dark_control.add_module)
    airtest_method.touch_button(dark_control.seg_module)
    data.project_flow(color)
    mark.import_label(path2,color)
    mark.auto_divide(color)
    training.model_training(color)
    training.add_card(color)
    training.set_study('2',color)
    training.cut_benchsize(color)
    training.star_training(color)
    assess.model_assess(color)
    assess.assess_success(color)
    
@allure.feature('深色版本demo')
@allure.title('跑单模型方案')
@pytest.mark.smoke
def test_run_module():   
    with allure.step(f'点击新建方案按钮'):
        management.create_project(color)
        do_log.info('成功点击新建方案按钮,用例执行成功')
    with allure.step(f'创建方案'):
        project_name = '深色版本单模型方案'
        management.input_name(project_name,color)
        management.create_success(color)
        do_log.info('成功创建方案,用例执行成功')
    with allure.step(f'导入图像+标注'):
        file_path = save_path.dataset_path + '\分类算法\\02_猫狗分类'
        data.add_image(file_path,color)
        data.add_label(file_path,color)
        do_log.info('标注导入成功,用例执行成功')
    with allure.step(f'切到图像标注页面自动划分'):
        mark.image_label(color)
        mark.auto_divide(color)
        do_log.info('自动划分成功,用例执行成功')
    with allure.step(f'切到模型训练页面进行训练'):
        training.model_training(color)
        training.add_card(color)
        training.set_study('2',color)
        training.cut_benchsize(color)
        training.star_training(color)
        do_log.info('成功开启训练,用例执行成功')
    with allure.step(f'切到模型评估页面开始评估'):
        assess.model_assess(color)
        assess.assess_success(color)
        do_log.info('评估完成,用例执行成功')
        airtest_method.operate_sleep(10.0)
    with allure.step(f'切到模型推理页面开始推理'):
        infering.model_infering(color)
        dataset = r'D:\ly\VDL_autotest\VDL_autotest\elements'  
        infering.images_input(dataset,'images',color) 
        infering.begin_infering(color)
        infering.review_infering(color)
        airtest_method.key_event("^w") #关闭软件

@allure.title('跑串联方案')
@pytest.mark.smoke
def test_run_pipelines():
    with allure.step(f'点击新建方案按钮'):
        management.create_project(color)
        do_log.info('成功点击新建方案按钮,用例执行成功')
    with allure.step(f'创建方案'):
        project_name = '深色版本串联方案'
        management.input_name(project_name,color)
        management.choice_project_type(color)
        management.create_success(color)
        do_log.info('成功创建串联方案,用例执行成功')
    with allure.step(f'导入图像'):
        file_path = r'C:\Users\user\Desktop\串联测试数据集\串联auto_test\分割-分割\images'
        data.add_image(file_path,color)
        do_log.info('图像导入成功,用例执行成功')
    with allure.step(f'新建方案流程'):
        path1 = r"C:\Users\user\Desktop\串联测试数据集\串联auto_test\分割-分割\labels1"
        path2 = r"C:\Users\user\Desktop\串联测试数据集\串联auto_test\分割-分割\labels2"
        add_pipelines_module(path1,path2)
        
        
    
    
        
    

    