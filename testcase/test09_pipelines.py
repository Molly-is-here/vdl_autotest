__author__ = "yunliu"
import pytest
import allure
from pages.management_page import management
from pages.data_page import data
from pages.marking_page import mark
from pages.training_page import training
from pages.assess_page import assess
from common.Airtest_method import airtest_method
from elements.public_control import light_control
from elements.public_control import label_control
from elements.pipelines import *
from common.handle_log import do_log

cls_pipelines = [cls_seq,cls_det,cls_seg]
det_pipelines = [det_OCR]
seg_pipellines = [seg_OCR,seg_seg,seg_det,seg_seq]
seq_pipelines = [seq_seg,seq_ocr]
uad_pipelines = [uad_det,uad_seg2,uad_seg1]
roi_pipelines = [roi_seg,roi_OCR]
rapid_pipelines = [rapid_det,rapid_seg,rapid_OCR]
learning_times = '10'
color = 'light'
static_path = os.path.join(save_path.base_path, 'static')

@allure.feature('串联方案测试')
@allure.title('点击新建方案')
@pytest.mark.skip('新建方案')
def test_create_proj():   
    '''新建方案'''
    with allure.step(f'点击新建方案按钮'):
        management.create_project(color)
        do_log.info('成功点击新建方案按钮,用例执行成功')

@allure.title('创建方案')
@pytest.mark.skip('创建方案')
def test_create_model(remark):
    '''创建方案'''
    with allure.step(f'输入方案名称'):
        management.input_name('test',color)
    with allure.step(f'选择串并联方案类型'):       
        management.choice_project_type(color)  
        do_log.info('串并联方案类型选择成功,用例执行成功')
    with allure.step(f'输入方案备注'):
        management.manage_remark(remark)  
    with allure.step(f'点击创建按钮'):
        management.create_success(color)
        do_log.info('方案成功新建,用例执行成功')

@allure.title('切换方案')
@pytest.mark.skip('串联方案创建完成后切换方案')
def test_close_project():
    '''关闭方案'''
    with allure.step(f'关闭方案'):          
        assess.template_file()
        assess.template_close()
        airtest_method.operate_sleep(20.0)

@allure.title('后置模块屏蔽区域-动态正选')
@pytest.mark.skip('屏蔽区域在串联方案中加入')
def test_dynamic_selection():
    with allure.step(f'动态正选'):
        airtest_method.touch_button(label_control.masking_area)
        airtest_method.touch_button(label_control.dynamic_selection)

@allure.title('后置模块屏蔽区域-动态反选')
@pytest.mark.skip('屏蔽区域在串联方案中加入')
def test_dynamic_deselection():
    with allure.step(f'动态反选'):
        airtest_method.touch_button(label_control.masking_area)
        airtest_method.touch_button(label_control.dynamic_deselection)

@allure.title('自定义ROI模块')
@pytest.mark.skip('跑ROI串联pipelines的时候再加')
def test_zidingyi_roi_module(sizes):
    # sizes = ['92.93', '40.47', '-0.32', '-13.22', '-0.52', '11.71']
    with allure.step(f'设置ROI参数'):
        data.setting_size(sizes[0],sizes[1])
        data.setting_displacement(sizes[2],sizes[3])
    with allure.step(f'新增ROI'):
        data.add_roi()
        data.setting_size(sizes[0],sizes[1])
        data.setting_displacement(sizes[4],sizes[5])
    do_log.info('自定义参数设置成功,用例执行成功')

@allure.title('新建ROI模块')
@pytest.mark.skip('跑ROI串联pipelines的时候再加')
def test_create_roi_module(name,file_path):
    with allure.step(f'新建方案'):
        test_create_proj()
        test_create_model(name)
    with allure.step(f'创建模块'):
        data.add_file(file_path)
    with allure.step(f'点击方案流程'):
        data.project_flow(color)
    with allure.step(f'数据源添加roi模块作为首模块'):
        data.add_pre_module(light_control.roi_module)
        data.project_flow(color)  #关闭方案流程画布
    do_log.info('成功新增ROI模块,用例执行成功')

@allure.title('比例划分ROI模块')
@pytest.mark.skip('跑ROI串联pipelines的时候再加')
def test_proportional_splitting(sizes):
    # sizes = ['1','2','38.60','78.62','0.00','1.01','-17.50','-1.70']
    with allure.step(f'切换模式'):
        data.change_ROI_mode()
    with allure.step(f'设置数量'):
        data.splitting_number(sizes[0],sizes[1])
    with allure.step(f'设置大小'):
        data.splitting_size(sizes[2],sizes[3])
    with allure.step(f'设置间隔'):
        data.splitting_interval(sizes[4],sizes[5])
    with allure.step(f'设置偏移'):
        data.splitting_displacement(sizes[6],sizes[7])
    do_log.info('比例划分参数设置成功,用例执行成功')

@allure.title('新建快速定位模块')
@pytest.mark.skip('跑快速定位pipelines的时候再加')
def test_add_rapid_module(name,file_path):
    with allure.step(f'新建方案'):
        test_create_proj()
        test_create_model(name)
    with allure.step(f'创建模块'):
        data.add_file(file_path)
    with allure.step(f'点击方案流程'):
        data.project_flow(color)
    with allure.step(f'数据源添加快速定位模块作为首模块'):
        data.add_pre_module(light_control.rapid_module)
        data.project_flow(color)  #关闭方案流程画布
    do_log.info(f'快速定位模块创建成功，用例执行成功')

@allure.title('绘制基准图像')
@pytest.mark.skip('跑快速定位pipelines的时候再加')
def test_painting_area(template_name,points,v1,v2,v3,number):
    with allure.step(f'新增模版'):
        data.add_template(template_name,points)
    with allure.step(f'矩形工具绘制区域'):
        mark.rapid_rectangle_marking(v1,v2,v3)
    with allure.step(f'单张测试'):
        data.rapid_single_test()
    with allure.step(f'调整参数'):
        data.set_filter_parameter(number,points)
    with allure.step(f'全量测试'):
        data.rapid_full_test()
    do_log.info(f'模板绘制成功，用例执行成功')

@allure.title('文件夹导入快速定位串联数据集')
@pytest.mark.smoke
def test_rapid_pipelines():
    '''单个快速定位模版串联pipelines'''
    for pipelines in rapid_pipelines: 
        with allure.step(f'创建快速定位方案'):
            file_path = pipelines.file_path + '\images'
            test_add_rapid_module(pipelines.name,file_path)
        with allure.step(f'绘制基准图像并进行推理'):
            get_points = pipelines.points
            test_painting_area('auto_match',(1844,314),get_points[0],get_points[1],get_points[2],pipelines.number)
        with allure.step(f'添加后置模块'):
            data.project_flow(color)   
            data.add_pre_module(pipelines.post_module) 
            # data.update_to_post_module()    
            data.project_flow(color)  #关闭方案流程画布                              
            do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):                 
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path,color)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                training.set_study(learning_times,color)
                training.star_training(color) 
                assess.model_assess(color)                             
                assess.assess_success(color)
                training.model_training(color)
                do_log.info('后置模块训练评估完成')
            with allure.step(f'关闭方案'):
                airtest_method.key_event("^w") 
                airtest_method.operate_sleep(3.0) 

@allure.title('多模版快速定位')
@pytest.mark.smoke
def test_multi_template_rapid_pipelines():
    '''多个快速定位模版串联pipelines'''
    with allure.step(f'创建快速定位方案'):
        file_path = rapid_OCR.file_path + '\images'
        test_add_rapid_module(rapid_OCR.name,file_path)
    with allure.step(f'绘制基准图像并进行推理'):
        i = 1
        for get_points in rapid_OCR.points:
            template_name = f'auto_match_{i}'
            if i == 1:
                points = (1844,314)
            else:
                points = (1844,358)
            test_painting_area(template_name,points,get_points[0],get_points[1],get_points[2],rapid_OCR.number)
            i += 1
        with allure.step(f'添加后置模块'):
            data.project_flow(color)   
            data.add_pre_module(rapid_OCR.post_module) 
            # data.update_to_post_module()    
            data.project_flow(color)  #关闭方案流程画布                              
            do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):                 
                label2_path = rapid_OCR.file_path + '\labels2'
                mark.import_label(label2_path,color)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                training.set_study(learning_times,color)
                training.star_training(color) 
                assess.model_assess(color)                             
                assess.assess_success(color)
                training.model_training(color)
                do_log.info('后置模块训练评估完成')
            with allure.step(f'关闭方案'):
                airtest_method.key_event("^w") 
                airtest_method.operate_sleep(3.0) 


@allure.title('文件夹导入ROI串联数据集')
@pytest.mark.smoke
def test_roi_pipelines():
    for pipelines in roi_pipelines: 
            zidingyi_sizes = ['95.65','48.08','0.31','-21.61','0.87','17.56']
            splitting_sizes = ['1','2','47.66','99.00','0.00','2.00','-24.83','0.49']
            with allure.step(f'新建方案'):
                file_path = pipelines.file_path + '\images'
                test_create_roi_module(pipelines.name,file_path)
            with allure.step(f'设置参数比例'):
                if pipelines == roi_uad:
                    test_proportional_splitting(splitting_sizes)
                else:
                    test_zidingyi_roi_module(zidingyi_sizes)
            with allure.step(f'添加后置模块'):
                data.project_flow(color)                              
                data.add_pre_module(pipelines.post_module)
                mark.image_label(color)   #点击图像标注按钮关闭方案流程画布                
                do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path,color)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                if pipelines.post_module == light_control.uad_module:  #后置模块若为无监督算法，不需要调整学习次数
                    training.star_training(color) 
                else:
                    training.set_study(learning_times,color)
                    training.star_training(color) 
                assess.model_assess(color)                             
                assess.assess_success(color)
                training.model_training(color)
                do_log.info('后置模块训练评估完成')
            with allure.step(f'返回数据源管理页面'):
                data.dataset_management(color)
                do_log.info('成功返回数据源管理页面')
            with allure.step(f'切换方案'):
                test_close_project()

@allure.title('文件夹导入分割串联数据集')
@pytest.mark.smoke
def test_seg_pipelines():
    for pipelines in seg_pipellines: 
            with allure.step(f'新建方案'):
                test_create_proj()
                test_create_model(pipelines.name)
                do_log.info(f"当前创建的pipelines为{pipelines.name}")
            with allure.step(f'点击导入文件夹按钮'):
                file_path = pipelines.file_path + '\images'
                data.add_file(file_path)
                do_log.info('成功导入图像,用例执行成功')
            with allure.step(f'点击方案流程'):
                data.project_flow(color)
                do_log.info('方案流程画布打开,用例执行成功')
            with allure.step(f'数据源添加分割模块作为首模块'):
                data.add_pre_module(pipelines.pre_module)
                mark.image_label(color)  #点击图像标注按钮关闭方案流程画布
                do_log.info('分割首模块创建成功,用例执行成功')
            with allure.step(f'导入前置模块标注'):
                label1_path = pipelines.file_path + '\labels1'
                mark.import_label(label1_path,color)
                do_log.info('前置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                training.set_study(learning_times,color)
                training.star_training(color)
                assess.model_assess(color)
                assess.assess_success(color) 
                do_log.info('前置模块训练评估完成')
            with allure.step(f'添加后置模块'):
                data.project_flow(color)                
                data.add_pre_module(pipelines.post_module)
                mark.image_label(color)   #点击图像标注按钮关闭方案流程画布                
                do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path,color)
                do_log.info('后置模块标注导入成功')           
            if pipelines == seg_seg:
                with allure.step(f'动态反选'):
                    test_dynamic_deselection()
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                if pipelines == seg_seq:
                    training.seq_set_study(learning_times)
                    training.star_training(color)
                else:
                    training.set_study(learning_times,color)
                    training.star_training(color) 
                assess.model_assess(color)                                          
                assess.assess_success(color) 
                training.model_training(color)
                do_log.info('后置模块训练评估完成')
            with allure.step(f'返回数据源管理页面'):
                data.dataset_management(color)
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
                do_log.info(f"当前创建的pipelines为{pipelines.name}")
            with allure.step(f'点击导入文件夹按钮'):
                file_path = pipelines.file_path + '\images'
                data.add_file(file_path)
                do_log.info('成功导入图像,用例执行成功')
            with allure.step(f'点击方案流程'):
                data.project_flow(color)
                do_log.info('方案流程画布打开,用例执行成功')
            with allure.step(f'数据源添加检测模块作为首模块'):
                data.add_pre_module(pipelines.pre_module)
                mark.image_label(color)  #点击图像标注按钮关闭方案流程画布
                do_log.info('检测首模块创建成功,用例执行成功')
            with allure.step(f'导入前置模块标注'):
                label1_path = pipelines.file_path + '\labels1'
                mark.import_label(label1_path,color)
                do_log.info('前置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                training.set_study(learning_times,color)
                training.star_training(color)
                assess.model_assess(color)
                assess.assess_success(color) 
                do_log.info('前置模块训练评估完成')
            with allure.step(f'添加后置模块'):
                data.project_flow(color)                
                data.add_pre_module(pipelines.post_module)
                mark.image_label(color)   #点击图像标注按钮关闭方案流程画布                
                do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path,color)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                if pipelines.post_module == light_control.uad_module:  #后置模块若为无监督算法，不需要调整学习次数
                    training.star_training(color) 
                else:
                    training.set_study(learning_times,color)
                    training.star_training(color) 
                assess.model_assess(color)            
                training.review_assess('后置模块')               
                assess.assess_success(color)
                training.model_training(color)
                do_log.info('后置模块训练评估完成')
            with allure.step(f'返回数据源管理页面'):
                data.dataset_management(color)
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
                do_log.info(f"当前创建的pipelines为{pipelines.name}")
            with allure.step(f'点击导入文件夹按钮'):
                file_path = pipelines.file_path + '\images'
                data.add_file(file_path)
                do_log.info('成功导入图像,用例执行成功')
            with allure.step(f'点击方案流程'):
                data.project_flow(color)
                do_log.info('方案流程画布打开,用例执行成功')
            with allure.step(f'数据源添加分类模块作为首模块'):
                data.add_pre_module(pipelines.pre_module)
                mark.image_label(color)  #点击图像标注按钮关闭方案流程画布
                do_log.info('分类首模块创建成功,用例执行成功')
            with allure.step(f'导入前置模块标注'):
                label1_path = pipelines.file_path + '\labels1'
                mark.import_label(label1_path,color)
                do_log.info('前置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                training.set_study(learning_times,color)
                training.star_training(color)
                assess.model_assess(color)
                assess.assess_success(color) 
                do_log.info('前置模块训练评估完成')
            with allure.step(f'添加后置模块'):
                data.project_flow(color)                
                data.add_pre_module(pipelines.post_module)
                mark.image_label(color)   #点击图像标注按钮关闭方案流程画布                
                do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path,color)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                if pipelines == cls_seq:
                    training.seq_set_study(learning_times)
                    training.star_training(color)
                else:
                    training.set_study(learning_times,color)
                    training.star_training(color) 
                assess.model_assess(color)                             
                assess.assess_success(color)
                training.model_training(color)
                do_log.info('后置模块训练评估完成')
            with allure.step(f'返回数据源管理页面'):
                data.dataset_management(color)
                do_log.info('成功返回数据源管理页面')
            with allure.step(f'切换方案'):
                test_close_project()

@allure.title('文件夹导入字符串串联数据集')
@pytest.mark.smoke
def test_seq_pipelines():
    for pipelines in seq_pipelines: 
            with allure.step(f'新建方案'):
                test_create_proj()
                test_create_model(pipelines.name)
                do_log.info(f"当前创建的pipelines为{pipelines.name}")
            with allure.step(f'点击导入文件夹按钮'):
                file_path = pipelines.file_path + '\images'
                data.add_file(file_path)
                do_log.info('成功导入图像,用例执行成功')
            with allure.step(f'点击方案流程'):
                data.project_flow(color)
                do_log.info('方案流程画布打开,用例执行成功')
            with allure.step(f'数据源添加字符串模块作为首模块'):
                data.add_pre_module(pipelines.pre_module)
                mark.image_label(color)  #点击图像标注按钮关闭方案流程画布
                do_log.info('字符串首模块创建成功,用例执行成功')
            with allure.step(f'导入前置模块标注'):
                label1_path = pipelines.file_path + '\labels1'
                mark.import_label(label1_path,color)
                do_log.info('前置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                training.seq_set_study(learning_times)
                training.star_training(color)
                assess.model_assess(color)
                assess.assess_success(color) 
                do_log.info('前置模块训练评估完成')
            with allure.step(f'添加后置模块'):
                data.project_flow(color)                
                data.add_pre_module(pipelines.post_module)
                mark.image_label(color)   #点击图像标注按钮关闭方案流程画布                
                do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path,color)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                if pipelines.post_module == light_control.uad_module:  #后置模块若为无监督算法，不需要调整学习次数
                    training.star_training(color) 
                else:
                    training.set_study(learning_times,color)
                    training.star_training(color) 
                assess.model_assess(color)                             
                assess.assess_success(color)
                training.model_training(color)
                do_log.info('后置模块训练评估完成')
            with allure.step(f'返回数据源管理页面'):
                data.dataset_management(color)
                do_log.info('成功返回数据源管理页面')
            with allure.step(f'切换方案'):
                test_close_project()

@allure.title('文件夹导入无监督串联数据集')
@pytest.mark.smoke
def test_uad_pipelines():
    for pipelines in uad_pipelines: 
            with allure.step(f'新建方案'):
                test_create_proj()
                test_create_model(pipelines.name)
                do_log.info(f"当前创建的pipelines为{pipelines.name}")
            with allure.step(f'点击导入文件夹按钮'):
                file_path = pipelines.file_path + '\images'
                data.add_file(file_path)
                do_log.info('成功导入图像,用例执行成功')
            with allure.step(f'点击方案流程'):
                data.project_flow(color)
                do_log.info('方案流程画布打开,用例执行成功')
            with allure.step(f'数据源添加无监督模块作为首模块'):
                data.add_pre_module(pipelines.pre_module)
                mark.image_label(color)  #点击图像标注按钮关闭方案流程画布
                do_log.info('无监督首模块创建成功,用例执行成功')
            with allure.step(f'导入前置模块标注'):
                label1_path = pipelines.file_path + '\labels1'
                mark.import_label(label1_path,color)
                do_log.info('前置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                if pipelines.pre_module == light_control.uad_module:  #后置模块若为无监督算法，不需要调整学习次数
                    training.star_training(color) 
                else:
                    training.set_study(learning_times,color)
                    training.star_training(color)
                assess.model_assess(color)
                assess.assess_success(color) 
                do_log.info('前置模块训练评估完成')
            with allure.step(f'添加后置模块'):
                data.project_flow(color)                
                data.add_pre_module(pipelines.post_module)
                mark.image_label(color)   #点击图像标注按钮关闭方案流程画布                
                do_log.info(f'后置模块创建成功')
            with allure.step(f'导入后置模块标注'):
                label2_path = pipelines.file_path + '\labels2'
                mark.import_label(label2_path,color)
                do_log.info('后置模块标注导入成功')
            with allure.step(f'自动划分数据集'):
                mark.auto_divide(color)
            with allure.step(f'开启训练'):
                training.model_training(color)
                training.add_card(color)
                if pipelines.post_module == light_control.uad_module:  #后置模块若为无监督算法，不需要调整学习次数
                    training.star_training(color) 
                else:
                    training.set_study(learning_times,color)
                    training.star_training(color) 
                assess.model_assess(color)                             
                assess.assess_success(color)
                training.model_training(color)
                do_log.info('后置模块训练评估完成')
            with allure.step(f'返回数据源管理页面'):
                data.dataset_management(color)
                do_log.info('成功返回数据源管理页面')
            with allure.step(f'切换方案'):
                test_close_project()

     




    
        
            
        
            

            



