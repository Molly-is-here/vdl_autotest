import pytest
import allure
from common.Airtest_method import airtest_method
from elements.public_control import control
from elements.elements_path import save_path
from common.handle_log import do_log

@allure.feature('数据管理页面')
@allure.title('通过下划线导入图像')
@pytest.mark.smoke
def test_add_image_underscore():    
    if not airtest_method.check_exit(control.add_image_underscore,'FALSE') :
        assert False,'找不到添加图像按钮'
    else:
        with allure.step(f'点击导入图像下划线'):
            airtest_method.touch_button(control.add_image_underscore)
    airtest_method.touch_button(control.choice_file)   
    file_path = save_path.dataset_path + '\导入mask\image'
    airtest_method.input_text(file_path)
    airtest_method.touch_button(control.jump_click)
    airtest_method.touch_button(control.click_area)
    '''全选图片'''
    airtest_method.key_event("^a")
    airtest_method.touch_button(control.ok_button)
    if not airtest_method.check_exit(control.upload_label,'FALSE') :
        do_log.error('导入失败，用例执行失败')
        assert False,'找不到导入完成标志'
    else:
        with allure.step(f'点击完成按钮'):
            airtest_method.touch_button(control.upload_done)
            do_log.info('成功导入图像,用例执行成功')

@allure.title('导入图像')
@pytest.mark.smoke
def test_add_image():    
    if not airtest_method.check_exit(control.add_image,'FALSE') :
        assert False,'找不到添加图像按钮'
    else:
        with allure.step(f'点击导入图像按钮'):
            airtest_method.touch_button(control.add_image)
    airtest_method.touch_button(control.choice_file)   
    file_path = save_path.dataset_path + '\导入mask\images'
    airtest_method.input_text(file_path)
    airtest_method.touch_button(control.jump_click)
    airtest_method.touch_button(control.click_area)
    '''全选图片'''
    airtest_method.key_event("^a")
    airtest_method.touch_button(control.ok_button)
    if not airtest_method.check_exit(control.upload_label,'FALSE') :
        do_log.error('导入失败，用例执行失败')
        assert False,'找不到导入完成标志'
    else:
        with allure.step(f'点击完成按钮'):
            airtest_method.touch_button(control.upload_done)
            do_log.info('成功导入图像,用例执行成功')

@allure.title('导入标注')
@pytest.mark.smoke
def test_add_label():
    '''导入标注'''   
    if not airtest_method.check_exit(control.add_label,'FALSE',5) :
        assert False,'找不到添加标注按钮'
    else:
        with allure.step(f'点击导入标注按钮'):
            airtest_method.touch_button(control.add_label)
    airtest_method.touch_button(control.choice_file) 
    file_path = save_path.dataset_path + '\导入mask\\64个mask'
    airtest_method.input_text(file_path)
    airtest_method.touch_button(control.jump_click)
    airtest_method.touch_button(control.click_area)
    '''全选标注'''
    airtest_method.key_event("^a")
    airtest_method.touch_button(control.ok_button)

    if not airtest_method.check_exit(control.upload_label,'FALSE') :
        do_log.error('导入失败，用例执行失败')
        assert False,'找不到导入完成标志'
    else:
        with allure.step(f'点击完成按钮'):
            airtest_method.touch_button(control.upload_done)
            do_log.info('成功导入标注,用例执行成功')

@allure.title('导入图像+标注')
@pytest.mark.skip("导入图像+标注放到增量训练过程")
def test_add_file():
    '''导入图像+标注'''   
    if not airtest_method.check_exit(control.add_file,'FALSE') :
        assert False,'找不到添加文件夹按钮'
    else:
        with allure.step(f'点击导入文件夹按钮'):
            airtest_method.touch_button(control.add_file)
    airtest_method.touch_button(control.choice_file) 
    file_path = save_path.dataset_path + '\导入mask\导入image和label'
    airtest_method.input_text(file_path)
    airtest_method.touch_button(control.jump_click)
    airtest_method.touch_button(control.choice_button)

    if not airtest_method.check_exit(control.upload_label,'FALSE') :
        do_log.error('导入失败，用例执行失败')
        assert False,'找不到导入完成标志'
    else:
        with allure.step(f'点击完成按钮'):
            airtest_method.touch_button(control.upload_done)
            do_log.info('成功导入图像+标注,用例执行成功')
    
@allure.title('数据管理页面筛选框组合筛选')
@pytest.mark.smoke
def test_search_image():
    with allure.step(f'搜索框输入关键字'):
        airtest_method.touch_button(control.manage_input)
        project_name = '5'
        airtest_method.input_text(project_name)
    with allure.step(f'筛选列表筛选是否标注条件'):
        airtest_method.touch_button(control.manage_search)
        airtest_method.touch_button(control.unfinish_labeled)
        airtest_method.touch_button(control.add_file)
        if not airtest_method.check_exit(control.null_results,'TRUE',5) :
            assert False,'组合筛选无效'
        else:           
            do_log.info('组合筛选生效,用例执行成功')
           








