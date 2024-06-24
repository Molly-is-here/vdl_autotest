import pytest
import allure
from common.Airtest_method import airtest_method
from elements.public_control import control
from elements.elements_path import save_path
from pages.data_page import data
from common.handle_log import do_log

@allure.feature('数据管理页面')

@allure.title('添加标签')
@pytest.mark.skip('导入图片时再新增标签')
def test_add_tag(content):   
    '''添加标签''' 
    with allure.step(f'添加标签'):
        data.add_tag(content)
        do_log.info('成功添加标签,用例执行成功')

@allure.title('通过下划线导入图像')
@pytest.mark.smoke
def test_add_image_underscore():    
    with allure.step(f'点击下划线导入图像'):
        file_path = save_path.dataset_path + '\导入mask\images'
        data.add_image_underscore(file_path)  
    with allure.step(f'添加标签'):
        test_add_tag('自动化标签')
    do_log.info('成功导入图像,用例执行成功')

@allure.title('导入图像')
@pytest.mark.smoke
def test_add_image():   
    '''导入图像''' 
    with allure.step(f'点击导入图像按钮'):
        file_path = save_path.dataset_path + '\导入mask\images'
        data.add_image(file_path)
    # with allure.step(f'添加标签'):
    #     test_add_tag('第2批自动化标签')
    do_log.info('成功导入图像,用例执行成功')
            
@allure.title('导入标注')
@pytest.mark.smoke
def test_add_label():
    '''导入标注'''   
    with allure.step(f'点击导入标注按钮'):
            file_path = save_path.dataset_path + '\导入mask\\64个mask'
            data.add_label(file_path)
            do_log.info('成功导入标注,用例执行成功')

@allure.title('导入图像+标注')
@pytest.mark.skip("导入图像+标注放到增量训练过程")
def test_add_file():
    '''导入文件夹'''   
    with allure.step(f'点击导入文件夹按钮'):
        file_path = save_path.dataset_path + '\导入mask\导入image和label'
        data.add_file(file_path)
        do_log.info('成功导入图像+标注,用例执行成功')
    
@allure.title('数据管理页面筛选框组合筛选')
@pytest.mark.smoke
def test_search_image():
    with allure.step(f'搜索框输入关键字'):
        airtest_method.touch_button(control.manage_input)
        project_name = '0'
        airtest_method.input_text(project_name)
    with allure.step(f'筛选列表筛选是否标注条件'):
        airtest_method.touch_button(control.manage_search)
        airtest_method.touch_button(control.finish_labeled)
        airtest_method.touch_button(control.add_file)
        if not airtest_method.check_exit(control.add_image_underscore,'TRUE',5) :
            assert False,'组合筛选无效'
        else:           
            do_log.info('组合筛选生效,用例执行成功')
            airtest_method.operate_sleep()
           








