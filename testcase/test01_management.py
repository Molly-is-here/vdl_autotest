import pytest
import allure
from elements.elements_path import save_path
from pages.management_page import management
from common.Airtest_method import airtest_method
from elements.public_control import control
from tools.radom_character import radom_Name
from common.handle_log import do_log
import os


@allure.feature('方案管理页面测试')
@allure.title('点击新建方案')
@pytest.mark.smoke
def test_create_proj():   
    if not airtest_method.check_exit(control.create_project,'FALSE',5) :
        assert False,'找不到新建方案按钮'
    else:
        with allure.step(f'点击新建方案按钮'):
            management.create_project()
            do_log.info('成功点击新建方案按钮,用例执行成功')

@allure.title('编辑框仅输入单个字符创建方案失败')
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
            static_path = os.path.join('C:\\Users\\user\\.jenkins\\workspace\\VDL_test\\elements\\', 'static')
            screen_shot = os.path.join('C:\\Users\\user\\.jenkins\\workspace\\VDL_test\\elements\\', f"{project_name}.png")
            airtest_method.screenshot(screen_shot)
            falied_image =  os.path.join(save_path().base_path,screen_shot)  #指定路径
            allure.attach(falied_image,name="异常附件", attachment_type=allure.attachment_type.PNG)

@allure.title('编辑框输入多个字符创建方案成功')
@pytest.mark.smoke
def test_create_model():
    with allure.step(f'方案名称输入随机数'):
        random_string = radom_Name.get_character(3)
        airtest_method.input_text(random_string)
        do_log.info('方案名称成功输入,用例执行成功')
    with allure.step(f'选择模型类型'):
        airtest_method.touch_button(control.seg_item)
        if not airtest_method.check_exit(control.seg_item,'FALSE',5) :
            assert False,'找不到分割算法控件'
        else:
            with allure.step(f'点击创建按钮'):
                airtest_method.touch_button(control.create_button)
                do_log.info('方案成功新建,用例执行成功')

@allure.title('筛选框组合筛选')
@pytest.mark.smoke
def test_search_project():
    with allure.step(f'点击home键返回方案管理页面'):
        if not airtest_method.check_exit(control.home_button,'FALSE',10) :
            assert False,'找不到home键'
        else:
            airtest_method.touch_button(control.home_button)
            do_log.info('成功切换回方案管理页面,用例执行成功')  
        airtest_method.operate_sleep()
    with allure.step(f'搜索框输入关键字'):
        airtest_method.touch_button(control.manage_input)
        project_name = '测试發'
        airtest_method.input_text(project_name)
    with allure.step(f'筛选列表筛选算法类型'):
        airtest_method.touch_button(control.manage_search)
        airtest_method.touch_button(control.search_seg)
        if not airtest_method.check_exit(control.choice_proj,'FALSE',5) :
            assert False,'找不到选中方案'
        else:
            airtest_method.touch_button(control.choice_proj)
            airtest_method.double_click(control.choice_proj)
            do_log.info('成功混合筛选出方案,用例执行成功')




            

       


        



