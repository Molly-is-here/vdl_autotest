import pytest
from common.Airtest_method import airtest_method
from elements.public_control import control
from elements.elements_path import save_path
from common.handle_log import do_log


@pytest.mark.smoke
def test_add_image():
    '''导入图像'''      
    if not airtest_method.check_exit(control.add_image,'FALSE') :
        assert False,'找不到添加图像按钮'
    else:
        airtest_method.touch_button(control.add_image)
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
        airtest_method.touch_button(control.upload_done)
        do_log.info('成功导入图像,用例执行成功')

@pytest.mark.smoke
def test_add_label():
    '''导入标注'''   
    if not airtest_method.check_exit(control.add_label,'FALSE',5) :
        assert False,'找不到添加标注按钮'
    else:
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
        airtest_method.touch_button(control.upload_done)
        do_log.info('成功导入标注,用例执行成功')

@pytest.mark.skip("导入图像+标注放到增量训练过程")
def test_add_file():
    '''导入图像+标注'''   
    if not airtest_method.check_exit(control.add_file,'FALSE') :
        assert False,'找不到添加文件夹按钮'
    else:
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
        airtest_method.touch_button(control.upload_done)
        do_log.info('成功导入图像+标注,用例执行成功')
    