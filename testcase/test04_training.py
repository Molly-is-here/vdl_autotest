import pytest
import allure
from common.Airtest_method import airtest_method
from elements.public_control import control
from common.handle_log import do_log
from pages.training_page import training
from pages.assess_page import assess
from test02_data import test_add_file
from test03_label import *
from airtest.core.api import *

model_selection = [control.high_power,control.low_power]
scaling_selection = [control.equal_size,control.zidingyi_size]
input_size = ['512']

@allure.feature('模型训练页面')
@allure.title('切换至模型训练页面')
@pytest.mark.smoke
def test_training_page():
    with allure.step(f'点击模型训练tab按钮'):
        training.model_training()
        do_log.info('模型训练页面成功切换,用例执行成功')

@allure.title('新建训练小卡片') 
@pytest.mark.smoke
def test_add_card():
    with allure.step(f'点击新的训练按钮'):
        training.add_card()
        if not airtest_method.check_exit(control.new_card,'FALSE') :
            assert False,'训练小卡片创建失败'
        else:
            do_log.info('成功新建卡片,用例执行成功')

@allure.title('重命名训练小卡片') 
@pytest.mark.smoke
def test_rename():
    airtest_method.touch_button(control.new_card)
    with allure.step(f'鼠标右键'):
        airtest_method.right_click(coords=(199,195)) #右键
    with allure.step(f'点击重命名按钮'):   
        training.rename_button()
        airtest_method.key_event("^a") #全选      
    with allure.step(f'重命名'):
        input_name = '草莓大福萬歲-_yep'
        airtest_method.input_text(input_name)
        do_log.info('卡片成功重命名,用例执行成功')

@allure.title('修改备注') 
@pytest.mark.smoke
def test_edit_comment():
    with allure.step(f'点击更多按钮'):
        airtest_method.touch_button(control.more_button,2) #[更多]按钮
    with allure.step(f'点击修改备注按钮'):
        training.edit_comment()
    with allure.step(f'修改备注'):
        input_comment = '發發'
        airtest_method.input_text(input_comment)
        do_log.info('卡片备注成功修改,用例执行成功')

@allure.title('复制训练小卡片') 
@pytest.mark.smoke
def test_copy():
    with allure.step(f'点击更多按钮'):
        airtest_method.touch_button(control.more_button,2)
    with allure.step(f'点击复制按钮'):
        training.copy_button()
        do_log.info('成功复制卡片,用例执行成功')
        
@allure.title('删除卡片') 
@pytest.mark.smoke
def test_delete():  
    #airtest_method.touch_button(control.new_card)
    with allure.step(f'鼠标右键'):
        airtest_method.right_click(coords=(199,195))
    with allure.step(f'点击删除卡片按钮'):
        training.delete_button()

        if not airtest_method.check_exit(control.delete_prompt,'FALSE'):
            assert False,'未出现删除提示，删除失败'
        else:
            with allure.step(f'确认删除'):
                airtest_method.touch_button(control.training_okbutton)
                do_log.info('成功删除卡片，用例执行成功')

@allure.title('图像裁切')                
@pytest.mark.smoke
def test_image_cropping():
    with allure.step(f'选择图像裁切按钮'):
        training.image_cropping()
        airtest_method.operate_sleep()
        if not airtest_method.check_exit(control.cropping_true,'FALSE',5) :        
            assert False,'找不到是按钮'
        else:  
            with allure.step(f'选择是，确认开启图像裁切'):       
                airtest_method.touch_button(control.cropping_true)

        airtest_method.operate_sleep()
        with allure.step(f'设置学习次数'):
            training.set_study() 
        with allure.step(f'调整benchsize'):   
            training.mouse_move()
            training.zidingyi_button()             
            training.cut_benchsize()
        with allure.step(f'点击开始训练'):
            training.star_training()
        with allure.step(f'判断是否完成训练-评估'):
            assess.model_assess()
        with allure.step(f'判断是否评估成功'):  
            if not airtest_method.check_exit(control.infering_finished,'FALSE',360000) :
                assert False,'评估未完成'
            else:
                airtest_method.operate_sleep()
                do_log.info('图像裁切训练成功，用例执行成功')
        with allure.step(f'返回模型训练页面'): 
            training.model_training()

# @allure.title('继续训练') 
# @pytest.mark.smoke
# def test_continute_training():
#     with allure.step(f'点击更多按钮'):
#         airtest_method.touch_button(control.more_button)  
#     with allure.step(f'点击继续训练'):  
#         training.continu_training()
#         airtest_method.operate_sleep()
#     with allure.step(f'确认继续训练'): 
#         airtest_method.touch_button(control.training_okbutton) #确认继续训练       
#     with allure.step(f'判断是否训练成功'):
#         name = '继续训练'
#         training.review_assess(name) 
#     with allure.step(f'判断是否评估成功'):  
#         assess.assess_success()
#         do_log.info('继续训练成功，用例执行成功')
#     with allure.step(f'返回模型训练页面'): 
#         training.model_training()
#         test_delete()

@allure.title('增量训练')   
@pytest.mark.smoke
def test_add_training():  
    with allure.step(f'点击更多按钮'):    
        airtest_method.touch_button(control.more_button)
    with allure.step(f'选择增量训练'): 
        training.add_training()
        airtest_method.operate_sleep()
    with allure.step(f'返回数据管理页面'):
        airtest_method.touch_button(control.data_management_page)
    with allure.step(f'通过导入文件夹导入图像+标注'):
        test_add_file()
    with allure.step(f'图像标注页面重新划分数据集'):
        test_data_page()
        test_auto_divide()

    with allure.step(f'返回模型训练页面开始增量训练'):
        training.model_training()
    with allure.step(f'点击开始训练'):
        training.star_training()
    with allure.step(f'确认开启增量训练'):
        airtest_method.touch_button(control.training_okbutton)
    with allure.step(f'开启训练'):
        airtest_method.operate_sleep(120.0)      
        assess.model_assess()
    with allure.step(f'判断是否评估成功'):
        if not airtest_method.check_exit(control.report_button,'FALSE',360000) :
            assert False,'评估未完成'
        else:
            do_log.info('增量训练模型评估成功，用例执行成功')
    with allure.step(f'返回模型训练页面'): 
        training.model_training()
        
    
    
    









    













