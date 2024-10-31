__author__ = "yunliu"
import pytest
import allure
from pages.management_page import management
from common.Airtest_method import airtest_method
from elements.public_control import light_control
from common.handle_log import do_log

color = 'light'
@allure.feature('方案管理页面')
@allure.title('点击新建方案')
@pytest.mark.smoke
def test_create_proj():   
    with allure.step(f'点击新建方案按钮'):
        management.create_project(color)
    do_log.info('成功点击新建方案按钮,用例执行成功')

@allure.title('编辑框仅输入单个字符创建方案失败')
@pytest.mark.smoke
def test_input_name():
    project_name = '1'
    with allure.step(f'输入单个字符'):
        management.input_name(project_name,color)
    with allure.step(f'点击创建按钮'):
        management.create_success(color)
    with allure.step(f'校验异常情况'):
        airtest_method.hover((882,320))
        if airtest_method.check_exit(light_control.proj_error):
            do_log.error(f'字符长度输入校验,用例执行失败')
            allure.attach('字符长度输入校验失败', name="异常情况", attachment_type=allure.attachment_type.TEXT)

@allure.title('编辑框输入多个字符创建方案成功')
@pytest.mark.smoke
def test_create_model():
    with allure.step(f'方案名称输入多字符'):
        airtest_method.touch_button(light_control.input_textbox)
        airtest_method.key_event('{BACKSPACE}')
        management.input_name('Auto',color)
    with allure.step(f'以分割算法为例'):       
        if not airtest_method.check_exit(light_control.seg_item,'FALSE',5) :
            assert False,'找不到分割算法控件'   
        else:
            airtest_method.touch_button(light_control.seg_item)    
    with allure.step(f'点击创建按钮'):
        management.create_success(color)
    do_log.info('方案成功新建,用例执行成功')

@allure.title('方案管理页面筛选框组合筛选')
@pytest.mark.smoke
def test_search_project():
    with allure.step(f'点击home键返回方案管理页面'):
        management.home()    
    with allure.step(f'混合筛选'):
        management.mixed_filtering('Auto') 
    do_log.info('成功混合筛选出方案,用例执行成功')

@allure.title('右键编辑')
@pytest.mark.smoke
def test_right_click_toedit():
    with allure.step(f'鼠标右键进行编辑'):
        text = 'o*￣▽￣*o hihi嗨嗨'
        management.right_click_toedit(text)
    do_log.info('右键编辑添加备注成功,用例执行成功')

@allure.title('右键关闭方案')
@pytest.mark.smoke
def test_closed_project():
    with allure.step(f'右键关闭方案'):
        management.right_click_toclosed()
        airtest_method.operate_sleep(2.0)
    do_log.info('成功关闭方案,用例执行成功')

@allure.title('双击打开方案')
@pytest.mark.smoke
def test_opened_project():
    with allure.step(f'双击打开方案'):
        management.double_click_toopened()
    do_log.info('成功打开方案,用例执行成功')





            

       


        



