import pytest
from common.Airtest_method import airtest_method
from elements.public_control import control
from common.handle_log import do_log
from pages.training_page import training
from test02_data import test_add_file
from pages.assess_page import assess
from pages.marking_page import mark

model_selection = [control.high_power,control.low_power]
scaling_selection = [control.equal_size,control.zidingyi_size]

@pytest.mark.smoke
def test_training_page():
    #airtest_method.touch_button(control.model_training)
    training.model_training()
    if not airtest_method.check_exit(control.add_card,'FALSE') :
        do_log.error('模型训练页面切换失败，用例执行失败')
        assert False,'找不到模型训练页面'
    else:
       do_log.info('模型训练页面成功切换,用例执行成功')
    
# @pytest.mark.smoke
# def test_add_card():
#     airtest_method.touch_button(control.add_card)
#     if not airtest_method.check_exit(control.new_card,'FALSE') :
#         do_log.error('卡片新增失败，用例执行失败')
#         assert False,'模型小卡片创建失败'
#     else:
#         do_log.info('成功新建卡片,用例执行成功')

# @pytest.mark.smoke
# def test_rename():
#     airtest_method.touch_button(control.new_card)
#     airtest_method.right_click(coords=(199,195))
#     '''重命名'''    
#     if not airtest_method.check_exit(control.rename_button,'FALSE'):
#         do_log.error('重命名失败，用例执行失败')
#         assert False,'重命名按钮查找失败'
#     else:
#         airtest_method.touch_button(control.rename_button)
#     airtest_method.key_event("^a")
#     input_name = '草莓大福萬歲-_yep'
#     airtest_method.input_text(input_name)
#     do_log.info('卡片成功重命名,用例执行成功')

# @pytest.mark.smoke
# def test_edit_comment():
#     '''修改备注'''
#     airtest_method.touch_button(control.more_button,2) 
#     if not airtest_method.check_exit(control.edit_comment,'FALSE'):
#         do_log.error('备注失败，用例执行失败')
#         assert False,'备注按钮查找失败'
#     else:
#         airtest_method.touch_button(control.edit_comment)
#     input_comment = '發發'
#     airtest_method.input_text(input_comment)
#     do_log.info('卡片备注成功修改,用例执行成功')

# @pytest.mark.smoke
# def test_copy():
#     '''复制'''
#     airtest_method.touch_button(control.more_button,2)
#     if not airtest_method.check_exit(control.copy_button,'FALSE'):
#         do_log.error('复制失败，用例执行失败')
#         assert False,'复制按钮查找失败'
#     else:
#         airtest_method.touch_button(control.copy_button)
#         do_log.info('成功复制卡片,用例执行成功')

# @pytest.mark.smoke
# def test_delete():
#     '''删除'''
#     airtest_method.touch_button(control.new_card)
#     airtest_method.right_click(coords=(199,195))
#     if not airtest_method.check_exit(control.delete_button,'FALSE') :
#         do_log.error('删除失败，用例执行失败')
#         assert False,'删除按钮查找失败'
#     else:
#         airtest_method.touch_button(control.delete_button)

#     if not airtest_method.check_exit(control.delete_prompt,'FALSE'):
#         do_log.error('未出现删除提示，用例执行失败')
#         assert False,'未出现删除提示，删除失败'
#     else:
#         airtest_method.touch_button(control.training_okbutton)
#         do_log.info('成功删除卡片，用例执行成功')

# @pytest.mark.parametrize('type',model_selection)
# def test_choice_model(type):
#     airtest_method.touch_button(control.add_card)
#     airtest_method.touch_button(control.choice_model)
#     airtest_method.touch_button(type) #选择模型类型高精度或者低功耗
#     if not airtest_method.check_exit(type,'FALSE',5) : 
#         do_log.error('模型类型切换失败，用例执行失败')       
#         assert False,'模型类型切换失败'
#     do_log.info('成功切换模型类型,用例执行成功')

#     training.set_study() #设置学习次数
#     ''' 调整benchsize'''
#     training.mouse_move()
#     training.zidingyi_button()             
#     training.cut_benchsize()
#     '''开始训练'''
#     airtest_method.touch_button(control.star_training)
#     airtest_method.operate_sleep()
#     if not airtest_method.check_exit(control.review_assess,'FALSE',36000) :        
#         assert False,'找不到任务完成标志'
#     else:                
#         do_log.info('切换模型类型训练成功，用例执行成功')
#     airtest_method.operate_sleep()

@pytest.mark.smoke
def test_color_mode():
    airtest_method.touch_button(control.add_card)
    if not airtest_method.check_exit(control.color_mode,'FALSE',5) :        
        assert False,'找不到颜色按钮'
    else:         
        airtest_method.touch_button(control.color_mode)
        airtest_method.operate_sleep()
    if not airtest_method.check_exit(control.gray_image,'FALSE',5) :        
        assert False,'找不到灰度图按钮'
    else:         
        airtest_method.touch_button(control.gray_image)
        do_log.info('成功切换颜色模式,用例执行成功')

    airtest_method.operate_sleep()
    training.set_study() #设置学习次数
    
    ''' 调整benchsize'''
    training.mouse_move()
    training.zidingyi_button()             
    training.cut_benchsize()
    '''开始训练'''
    airtest_method.touch_button(control.star_training)
    airtest_method.operate_sleep()
    if not airtest_method.check_exit(control.review_assess,'FALSE',36000) :        
        assert False,'找不到任务完成标志'   
    else:
        do_log.info('切换颜色模式训练成功，用例执行成功')
    airtest_method.operate_sleep()

# @pytest.mark.parametrize('type',scaling_selection)
# def test_image_scaling(type):
#     airtest_method.touch_button(control.add_card)
#     if not airtest_method.check_exit(control.image_scaling,'FALSE',5) :        
#         assert False,'找不到图像缩放按钮'
#     else:         
#         airtest_method.touch_button(control.image_scaling)
#         airtest_method.operate_sleep()
#     airtest_method.touch_button(type) #选择等比例缩放或自定义缩放
#     if not airtest_method.check_exit(type,'FALSE',5) : 
#         do_log.error('图像缩放切换失败，用例执行失败')       
#         assert False,'图像缩放切换失败'
#     do_log.info('成功选择图像缩放,用例执行成功')

#     airtest_method.operate_sleep()
#     training.set_study() #设置学习次数
#     ''' 调整benchsize'''
#     training.mouse_move()
#     training.zidingyi_button()             
#     training.cut_benchsize()
#     '''开始训练'''
#     airtest_method.touch_button(control.star_training)
#     airtest_method.operate_sleep()
#     if not airtest_method.check_exit(control.review_assess,'FALSE',36000) :        
#         assert False,'找不到查看评估标志'
#     else:         
#         do_log.info('图像缩放训练成功，用例执行成功')
        
# @pytest.mark.smoke
# def test_continute_training():
#     '''评估完成后，返回训练页面''' 
#     airtest_method.touch_button(control.review_assess)
#     assess.assess_success()
#     training.model_training()  
#     '''继续训练'''
#     airtest_method.touch_button(control.more_button)
#     # if not airtest_method.check_exit(control.continu_training,'FALSE',5) :        
#     #     assert False,'找不到继续训练按钮'
#     # else:         
#     airtest_method.touch_button(control.continu_training)
#     airtest_method.operate_sleep()
#     airtest_method.touch_button(control.training_okbutton)
#     airtest_method.operate_sleep()
#     if not airtest_method.check_exit(control.review_assess,'FALSE',36000) :        
#         assert False,'找不到任务完成标志'
#     else:         
#         do_log.info('继续训练成功，用例执行成功')
#         airtest_method.touch_button(control.review_assess)

# @pytest.mark.smoke
# def test_image_cropping():
#     training.model_training()
#     airtest_method.touch_button(control.add_card)
#     if not airtest_method.check_exit(control.image_cropping,'FALSE',5) :        
#         assert False,'找不到图像裁切按钮'
#     else:         
#         airtest_method.touch_button(control.image_cropping)
#         airtest_method.operate_sleep()
#     if not airtest_method.check_exit(control.cropping_true,'FALSE',5) :        
#         assert False,'找不到是按钮'
#     else:         
#         airtest_method.touch_button(control.cropping_true)
#         do_log.info('确定裁切,用例执行成功')

#     airtest_method.operate_sleep()
#     training.set_study() #设置学习次数
#     ''' 调整benchsize'''
#     training.mouse_move()
#     training.zidingyi_button()             
#     training.cut_benchsize()
#     '''开始训练'''
#     airtest_method.touch_button(control.star_training)
#     airtest_method.operate_sleep()
#     if not airtest_method.check_exit(control.review_assess,'FALSE',36000) :        
#         assert False,'找不到查看评估标志'   
#     else:
#         do_log.info('图像裁切训练成功，用例执行成功')
#         airtest_method.touch_button(control.review_assess)
#         assess.assess_success()
#         airtest_method.operate_sleep()

# @pytest.mark.smoke
# def test_add_training(): 
    
#     training.model_training()    
#     '''增量训练'''
#     airtest_method.touch_button(control.more_button)
#     if not airtest_method.check_exit(control.add_training,'FALSE',5) :        
#         assert False,'找不到增量训练按钮'
#     else:         
#         airtest_method.touch_button(control.add_training)
#         airtest_method.operate_sleep()

#     '''切换回图像标注页面，新增数据集'''
#     airtest_method.touch_button(control.data_management_page)
#     test_add_file()
#     mark.image_label()
#     mark.auto_divide()

#     '''返回模型训练页面开始增量训练'''
#     training.model_training()
#     training.star_training()
#     airtest_method.touch_button(control.training_okbutton)
#     if not airtest_method.check_exit(control.review_assess,'FALSE',36000) :        
#         assert False,'找不到任务完成标志'
#     else:         
#         do_log.info('增量训练成功，用例执行成功')
#     airtest_method.operate_sleep()
    
    









    













