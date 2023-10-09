import pytest
import allure
from pages.management_page import management
from common.Airtest_method import airtest_method
from elements.public_control import control
from common.handle_log import do_log


@allure.title("方案管理页面测试")
@pytest.mark.smoke
def test_create_proj():   
    if not airtest_method.check_exit(control.create_project,'FALSE',5) :
        assert False,'找不到新建方案按钮'
    else:
        management.create_project()
        do_log.info('成功点击新建方案按钮,用例执行成功')

@pytest.mark.smoke
def test_input_name():
    with allure.step(f'点击编辑框'):
        airtest_method.touch_button(control.select_textbox)
        project_name = '1'
    with allure.step(f'输入字符'):
        airtest_method.input_text(project_name)
    with allure.step(f'点击创建按钮'):
        airtest_method.touch_button(control.create_button)  
        if airtest_method.check_exit(control.proj_error,'TRUE',5):
            do_log.error(f'字符长度输入校验,用例执行失败')
            allure.attach(airtest_method.screenshot,'异常')

@pytest.mark.smoke
def test_create_model():
    project_name = '中文繁體A-B_[c]'
    airtest_method.input_text(project_name)
    do_log.info('方案名称成功输入,用例执行成功')
    airtest_method.touch_button(control.seg_item)
    if not airtest_method.check_exit(control.seg_item,'FALSE',5) :
        assert False,'找不到分割算法控件'
    else:
        airtest_method.touch_button(control.create_button)
        do_log.info('方案成功新建,用例执行成功')

@pytest.mark.smoke
def test_search_project():
    if not airtest_method.check_exit(control.home_button,'FALSE',10) :
        assert False,'找不到home键'
    else:
        airtest_method.touch_button(control.home_button)
        do_log.info('成功切换回方案管理页面,用例执行成功')  
    airtest_method.operate_sleep()
    airtest_method.touch_button(control.manage_input)
    project_name = '中文'
    airtest_method.input_text(project_name)
    airtest_method.touch_button(control.manage_search)
    airtest_method.touch_button(control.search_seg)
    if not airtest_method.check_exit(control.choice_proj,'FALSE',5) :
        assert False,'找不到选中方案'
    else:
        airtest_method.touch_button(control.choice_proj)
        airtest_method.double_click(control.choice_proj)
        # airtest_method.right_click(coords=(613,533))
        # airtest_method.touch_button(control.openproj_button)
        do_log.info('成功混合筛选出方案,用例执行成功')




            

       


        



