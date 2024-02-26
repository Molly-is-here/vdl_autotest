import pytest
import allure
from pages.management_page import management
from pages.data_page import data
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from pages.judgement_page import judgement
from pages.infering_page import infering
from common.Airtest_method import airtest_method
from elements.public_control import control
from elements.pipelines import *
from common.handle_log import do_log
from tools import ocr

cls_pipelines = [cls_seg,cls_det,cls_uad,cls_seq]
det_pipelines = [det_OCR,det_uad]
seg_pipellines = [seg_det,seg_uad,seg_seg,seg_OCR,seg_seq]
static_path = os.path.join(save_path.base_path, 'static')

@allure.feature('串联方案测试')
@allure.title('点击新建方案')
@pytest.mark.skip('新建方案')
def test_create_proj():   
    with allure.step(f'点击新建方案按钮'):
        management.create_project()
        do_log.info('成功点击新建方案按钮,用例执行成功')

@allure.title('创建方案')
@pytest.mark.skip('创建方案')
def test_create_model(remark):
    with allure.step(f'输入方案名称'):
        management.input_name('test')
    with allure.step(f'选择串并联方案类型'):       
        management.choice_project_type()  
        do_log.info('串并联方案类型选择成功,用例执行成功')
    with allure.step(f'输入方案备注'):
        management.manage_remark(remark)  
    with allure.step(f'点击创建按钮'):
        management.create_success()
        do_log.info('方案成功新建,用例执行成功')

@allure.title('切换方案')
@pytest.mark.skip("串联方案创建完成后切换方案")
def test_close_project():
    with allure.step(f'关闭方案'):    
        '''关闭方案'''
        assess.template_file()
        assess.template_close()
        airtest_method.operate_sleep(10.0)

@allure.title('文件夹导入分割串联数据集')
@pytest.mark.smoke
def test_seg_pipelines():
    for pipelines in seg_pipellines: 
            with allure.step(f'新建方案'):
                test_create_proj()
                test_create_model(pipelines.name)
            with allure.step(f'点击导入文件夹按钮'):
                file_path = pipelines.file_path + '\images'
                data.add_file(file_path)
                do_log.info('成功导入图像,用例执行成功')
            with allure.step(f'点击方案流程'):
                data.project_flow()
                do_log.info('方案流程画布打开,用例执行成功')
            with allure.step(f'数据源添加分割模块作为首模块'):
                data.add_pre_module(pipelines.pre_module)
                mark.image_label()  #点击图像标注按钮关闭方案流程画布
                do_log.info('分割首模块创建成功,用例执行成功')
            with allure.step(f'导入前置模块标注'):
                label1_path = pipelines.file_path + '\labels1'
                mark.import_label(label1_path)
                do_log.info('前置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide()
            with allure.step(f'开启训练'):
                training.model_training()
                training.add_card()
                training.set_study()
                training.star_training()
                assess.model_assess()
                assess.assess_success() 
                do_log.info('前置模块训练评估完成')
            with allure.step(f'添加后置模块'):
                data.project_flow()                
                data.add_pre_module(pipelines.post_module)
                mark.image_label()   #点击图像标注按钮关闭方案流程画布                
                do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide()
            with allure.step(f'开启训练'):
                training.model_training()
                training.add_card()
                if pipelines.post_module == control.uad_module:  #后置模块若为无监督算法，不需要调整学习次数
                    training.star_training() 
                else:
                    training.set_study()
                    training.star_training() 
                assess.model_assess()                                          
                assess.assess_success() 
                training.model_training()
                do_log.info('后置模块训练评估完成')
            with allure.step(f'返回数据源管理页面'):
                data.dataset_management()
                do_log.info('成功返回数据源管理页面')
            with allure.step(f'切换方案'):
                test_close_project()

@allure.title('文件夹导入检测串联数据集')
@pytest.mark.smoke
def test_det_pipelines():
    for pipelines in det_pipelines: 
            with allure.step(f'新建方案'):
                test_create_proj()
                test_create_model(pipelines.name)
            with allure.step(f'点击导入文件夹按钮'):
                file_path = pipelines.file_path + '\images'
                data.add_file(file_path)
                do_log.info('成功导入图像,用例执行成功')
            with allure.step(f'点击方案流程'):
                data.project_flow()
                do_log.info('方案流程画布打开,用例执行成功')
            with allure.step(f'数据源添加检测模块作为首模块'):
                data.add_pre_module(pipelines.pre_module)
                mark.image_label()  #点击图像标注按钮关闭方案流程画布
                do_log.info('检测首模块创建成功,用例执行成功')
            with allure.step(f'导入前置模块标注'):
                label1_path = pipelines.file_path + '\labels1'
                mark.import_label(label1_path)
                do_log.info('前置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide()
            with allure.step(f'开启训练'):
                training.model_training()
                training.add_card()
                training.set_study()
                training.star_training()
                assess.model_assess()
                assess.assess_success() 
                do_log.info('前置模块训练评估完成')
            with allure.step(f'添加后置模块'):
                data.project_flow()                
                data.add_pre_module(pipelines.post_module)
                mark.image_label()   #点击图像标注按钮关闭方案流程画布                
                do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide()
            with allure.step(f'开启训练'):
                training.model_training()
                training.add_card()
                if pipelines.post_module == control.uad_module:  #后置模块若为无监督算法，不需要调整学习次数
                    training.star_training() 
                else:
                    training.set_study()
                    training.star_training() 
                assess.model_assess()            
                training.review_assess('后置模块')               
                assess.assess_success()
                training.model_training()
                do_log.info('后置模块训练评估完成')
            with allure.step(f'返回数据源管理页面'):
                data.dataset_management()
                do_log.info('成功返回数据源管理页面')
            with allure.step(f'切换方案'):
                test_close_project()

@allure.title('文件夹导入分类串联数据集')
@pytest.mark.smoke
def test_cls_pipelines():
    for pipelines in cls_pipelines: 
            with allure.step(f'新建方案'):
                test_create_proj()
                test_create_model(pipelines.name)
            with allure.step(f'点击导入文件夹按钮'):
                file_path = pipelines.file_path + '\images'
                data.add_file(file_path)
                do_log.info('成功导入图像,用例执行成功')
            with allure.step(f'点击方案流程'):
                data.project_flow()
                do_log.info('方案流程画布打开,用例执行成功')
            with allure.step(f'数据源添加分类模块作为首模块'):
                data.add_pre_module(pipelines.pre_module)
                mark.image_label()  #点击图像标注按钮关闭方案流程画布
                do_log.info('分类首模块创建成功,用例执行成功')
            with allure.step(f'导入前置模块标注'):
                label1_path = pipelines.file_path + '\labels1'
                mark.import_label(label1_path)
                do_log.info('前置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide()
            with allure.step(f'开启训练'):
                training.model_training()
                training.add_card()
                training.set_study()
                training.star_training()
                assess.model_assess()
                assess.assess_success() 
                do_log.info('前置模块训练评估完成')
            with allure.step(f'添加后置模块'):
                data.project_flow()                
                data.add_pre_module(pipelines.post_module)
                mark.image_label()   #点击图像标注按钮关闭方案流程画布                
                do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide()
            with allure.step(f'开启训练'):
                training.model_training()
                training.add_card()
                if pipelines.post_module == control.uad_module:  #后置模块若为无监督算法，不需要调整学习次数
                    training.star_training() 
                else:
                    training.set_study()
                    training.star_training() 
                assess.model_assess()                             
                assess.assess_success()
                training.model_training()
                do_log.info('后置模块训练评估完成')
            with allure.step(f'返回数据源管理页面'):
                data.dataset_management()
                do_log.info('成功返回数据源管理页面')
            with allure.step(f'切换方案'):
                test_close_project()

@allure.title('使用GPU-ONNX推理')
@pytest.mark.skip('跳过使用GPU推理校验')
def test_GPU_ONNX_infering(dataset,file):
    with allure.step(f'导入图像'):
        infering.images_input(dataset,file)
        do_log.info('图像导入成功')
    with allure.step(f'开始推理'):
        judgement.judgement_infering()
    with allure.step(f'判断是否推理成功'):
        judgement.judgement_done()
        do_log.info('综合判定推理结束')

@allure.title('使用CPU推理')
@pytest.mark.skip('跳过使用CPU推理校验') 
def test_CPU_infering():
    if not airtest_method.check_exit(control.judgement_infering_button,'FALSE'):      
        assert False,'找不到开始推理按钮'
    else: 
        with allure.step(f'点击解锁按钮'):
            infering.unlock_infering()
        with allure.step(f'点击设备类型列表'):
            infering.infering_device_type()
        with allure.step(f'选择CPU设备'):
            infering.infering_device_CPU()
        with allure.step(f'开始推理'):
            judgement.judgement_infering()
            judgement.judgement_infering()
        with allure.step(f'判断是否推理成功'):
            judgement.judgement_done()
            do_log.info('CPU推理完成,用例执行成功') 

@allure.title('使用GPU-TRT推理')
@pytest.mark.skip('跳过使用GPU-TRT推理校验') 
def test_GPU_TRT_infering():
    if not airtest_method.check_exit(control.judgement_infering_button,'FALSE'):      
        assert False,'找不到开始推理按钮'
    else:         
        with allure.step(f'点击解锁按钮'):
            infering.unlock_infering()
        with allure.step(f'高级配置进行trt设置'):
            judgement.advanced_trt_acceleration()
        with allure.step(f'开始推理'):
            judgement.judgement_infering()
        with allure.step(f'判断是否推理成功'):
            judgement.judgement_done()
            do_log.info('GPU-TRT推理完成,用例执行成功') 
            
@allure.title('打开方案并切换至综合判定页面')
@pytest.mark.skip('跳过打开方案')
def test_open_pipelinespro():
    '''打开方案，切换至综合判定'''
    with allure.step(f'打开串联方案'):
        dataset = r"D:\方案\士多啤梨"
        management.open_project(dataset)
        management.click_project()
        airtest_method.operate_sleep(5.0)
    with allure.step(f'切换至综合判定页面'):
        judgement.judgement_page()
        do_log.info('成功切换至综合判定页面')

@allure.title('勾选分类判定范围')
@pytest.mark.smoke
def test_cls_judgement():
    test_open_pipelinespro()
    with allure.step(f'勾选分类判定范围'):
        judgement.judgement_area(control.cls_checkbox)
        do_log.info('分类判定范围勾选成功')
    with allure.step(f'设置分类判定规则'):
        judgement.judgement_rules()
        airtest_method.touch_button(control.cls_ok)
        airtest_method.touch_button(control.cls_ng)
        airtest_method.touch_button(control.save_button)  #点击保存
        airtest_method.operate_sleep()
        do_log.info('分类规则设置完成')
    with allure.step(f'使用GPU推理'): 
        dataset = r'D:\方案\士多啤梨'   
        test_GPU_ONNX_infering(dataset,'images')  
    with allure.step(f'使用CPU推理'):
        test_CPU_infering()
    with allure.step('使用TRT推理'):
        test_GPU_TRT_infering()
    with allure.step(f'筛选图片'):
        judgement.select_image('3.png')
        airtest_method.operate_sleep(3.0)
    with allure.step(f'截图识别结果'):             
        cls_results =  ocr.translate_text(1198,199,1302,226)
        do_log.info(f'分类判定结果{cls_results}')
        if cls_results == 'NG':
            cls_screenshot = os.path.join(static_path, "分类判定结果.png")        
            airtest_method.screenshot(cls_screenshot)   #截图
        else:
            assert False,'未识别判定结果'
    with allure.step(f'取消勾选分类判定范围'):
        judgement.judgement_area(control.cancel_select)
    with allure.step(f'关闭方案'):
        assess.template_file()
        assess.template_close()

@allure.title('勾选分割判定范围')
@pytest.mark.smoke
def test_seg_judgement():
    test_open_pipelinespro()
    with allure.step(f'勾选分割判定范围'):
        judgement.judgement_area(control.seg_checkbox)
        do_log.info('分割判定范围勾选成功')
    with allure.step(f'设置分割判定规则'):
        judgement.judgement_rules()
        airtest_method.touch_button(control.seg_rule)
        keyevent("{BACKSPACE}")
        airtest_method.input_text('1')
        airtest_method.touch_button(control.save_button)  #点击保存
        airtest_method.operate_sleep()
        do_log.info('分割规则设置完成')
    with allure.step(f'使用GPU推理'): 
        dataset = r'D:\方案\士多啤梨'   
        test_GPU_ONNX_infering(dataset,'images')
    with allure.step(f'使用CPU推理'):
        test_CPU_infering()
    with allure.step(f'筛选图片'):
        judgement.select_image('3.png')
        airtest_method.operate_sleep(3.0)
    with allure.step(f'截图识别结果'):             
        seg_results =  ocr.translate_text(1198,199,1302,226)
        do_log.info(f'分割判定结果{seg_results}')
        if seg_results == 'NG':
            seg_screenshot = os.path.join(static_path, "分割判定结果.png")        
            airtest_method.screenshot(seg_screenshot)   #截图
        else:
            assert False,'未识别判定结果'
  
@allure.title('批量推理')
@pytest.mark.smoke
def test_batch_infering():
    with allure.step(f'开启批量推理'):
        judgement.advanced_batch_infering(3)
    with allure.step(f'开始推理'):
            judgement.judgement_infering()
    with allure.step(f'判断是否推理成功'):
        judgement.judgement_done()
        do_log.info('批量推理完成,用例执行成功')
    with allure.step(f'取消勾选判定范围'):
        judgement.judgement_area(control.cancel_select)
    with allure.step(f'关闭方案'):
        assess.template_file()
        assess.template_close()




    
        
            
        
            

            



