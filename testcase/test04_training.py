import pytest
from common.Airtest_method import airtest_method
from elements.public_control import control
from common.handle_log import do_log
from pages.training_page import training
from test02_data import test_add_file
from pages.assess_page import assess
from pages.marking_page import mark
from airtest.core.api import *

model_selection = [control.high_power,control.low_power]
scaling_selection = [control.equal_size,control.zidingyi_size]
input_size = ['512']

@pytest.mark.smoke
def test_training_page():
    training.model_training()
    if not airtest_method.check_exit(control.add_card,'FALSE') :
        do_log.error('模型训练页面切换失败，用例执行失败')
        assert False,'找不到模型训练页面'
    else:
       do_log.info('模型训练页面成功切换,用例执行成功')
    
@pytest.mark.smoke
def test_add_card():
    training.add_card()
    if not airtest_method.check_exit(control.new_card,'FALSE') :
        do_log.error('卡片新增失败，用例执行失败')
        assert False,'模型小卡片创建失败'
    else:
        do_log.info('成功新建卡片,用例执行成功')

@pytest.mark.smoke
def test_rename():
    airtest_method.touch_button(control.new_card)
    airtest_method.right_click(coords=(199,195)) #右键
    '''重命名'''    
    training.rename_button()
    airtest_method.key_event("^a") #全选
    input_name = '草莓大福萬歲-_yep'
    airtest_method.input_text(input_name)
    do_log.info('卡片成功重命名,用例执行成功')

@pytest.mark.smoke
def test_edit_comment():
    '''修改备注'''
    airtest_method.touch_button(control.more_button,2) #【更多】按钮
    training.edit_comment()
    input_comment = '發發'
    airtest_method.input_text(input_comment)
    do_log.info('卡片备注成功修改,用例执行成功')

@pytest.mark.smoke
def test_copy():
    '''复制'''
    airtest_method.touch_button(control.more_button,2)
    training.copy_button()
    do_log.info('成功复制卡片,用例执行成功')

@pytest.mark.smoke
def test_delete():
    '''删除'''
    airtest_method.touch_button(control.new_card)
    airtest_method.right_click(coords=(199,195))
    training.delete_button()

    if not airtest_method.check_exit(control.delete_prompt,'FALSE'):
        do_log.error('未出现删除提示，用例执行失败')
        assert False,'未出现删除提示，删除失败'
    else:
        airtest_method.touch_button(control.training_okbutton)
        do_log.info('成功删除卡片，用例执行成功')

@pytest.mark.parametrize('type',model_selection)
def test_choice_model(type):
    '''高精度/低功耗'''
    training.add_card()
    training.choice_model()
    airtest_method.touch_button(type) #选择模型类型高精度或者低功耗
    if not airtest_method.check_exit(type,'FALSE',5) : 
        do_log.error('模型类型切换失败，用例执行失败')       
        assert False,'模型类型切换失败'
    do_log.info('成功切换模型类型,用例执行成功')

    training.set_study() #设置学习次数
    ''' 调整benchsize'''
    training.mouse_move()
    training.zidingyi_button()             
    training.cut_benchsize()

    '''开始训练'''
    training.star_training()
    training.review_assess()
    assess.assess_success()
    do_log.info('切换模型类型训练成功，用例执行成功')
    training.model_training()

@pytest.mark.parametrize('type',scaling_selection)
@pytest.mark.parametrize('size',input_size)
def test_image_scaling(type,size):
    '''图像缩放'''
    training.add_card()
    training.image_scaling()
    airtest_method.operate_sleep()
    airtest_method.touch_button(type) #选择等比例缩放或自定义缩放
    
    if not airtest_method.check_exit(type,'FALSE',5) : 
        do_log.error('图像缩放切换失败，用例执行失败')       
        assert False,'图像缩放切换失败'
    do_log.info('成功选择图像缩放,用例执行成功')
    if type == control.zidingyi_size:
        airtest_method.touch_button(control.zidingyi_edit_box1) #第一个编辑框
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        airtest_method.input_text(size)

        airtest_method.touch_button(control.zidingyi_edit_box2) #第二个编辑框
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        keyevent("{BACKSPACE}")
        airtest_method.input_text(size)

    airtest_method.operate_sleep()
    training.set_study() #设置学习次数
    ''' 调整benchsize'''
    training.mouse_move()
    training.zidingyi_button()             
    training.cut_benchsize()
    '''开始训练'''
    training.star_training()
    training.review_assess() 
    assess.assess_success()
    do_log.info('图像缩放训练成功，用例执行成功')
    training.model_training()
        
@pytest.mark.smoke
def test_continute_training():
    '''继续训练'''
    airtest_method.touch_button(control.new_card)
    airtest_method.operate_sleep()
    airtest_method.touch_button(control.more_button)       
    training.continu_training()
    airtest_method.operate_sleep()

    airtest_method.touch_button(control.training_okbutton) #确认继续训练
    training.review_assess()   
    assess.assess_success()
    do_log.info('继续训练成功，用例执行成功')
    training.model_training()
        
@pytest.mark.smoke
def test_image_cropping():
    training.add_card()
    training.image_cropping()
    airtest_method.operate_sleep()
    if not airtest_method.check_exit(control.cropping_true,'FALSE',5) :        
        assert False,'找不到是按钮'
    else:         
        airtest_method.touch_button(control.cropping_true)

    training.set_study() #设置学习次数
    ''' 调整benchsize'''
    training.mouse_move()
    training.zidingyi_button()             
    training.cut_benchsize()

    '''开始训练'''
    training.star_training()
    training.review_assess()
    assess.assess_success()
    do_log.info('图像裁切训练成功，用例执行成功')
    training.model_training()
    
@pytest.mark.smoke
def test_color_mode():
    '''彩色图/灰度图'''
    training.add_card()
    training.color_mode()
    airtest_method.operate_sleep()
    if not airtest_method.check_exit(control.gray_image,'FALSE',5) :        
        assert False,'找不到灰度图按钮'
    else:         
        airtest_method.touch_button(control.gray_image)
        do_log.info('成功切换至灰度图,用例执行成功')

    airtest_method.operate_sleep()
    training.set_study() #设置学习次数
    
    ''' 调整benchsize'''
    training.mouse_move()
    training.zidingyi_button()             
    training.cut_benchsize()

    '''开始训练'''
    training.star_training()
    training.review_assess()
    assess.assess_success()
    do_log.info('切换颜色模式训练成功，用例执行成功')
    training.model_training()

@pytest.mark.smoke
def test_add_training():      
    '''增量训练'''
    airtest_method.touch_button(control.new_card)
    airtest_method.operate_sleep()
    airtest_method.touch_button(control.more_button)
    training.add_training()
    airtest_method.operate_sleep()

    '''切换回图像标注页面，新增数据集'''
    airtest_method.touch_button(control.data_management_page)
    test_add_file()
    mark.image_label()
    mark.auto_divide()

    '''返回模型训练页面开始增量训练'''
    training.model_training()
    training.star_training()
    airtest_method.touch_button(control.training_okbutton)
    training.review_assess()
    do_log.info('增量训练成功，用例执行成功')
    
    
    









    













