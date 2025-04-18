from airtest.core.api import *
from elements.elements_path import save_path

#公共控件
class light_control():
    #分割算法
    seg_item = Template(save_path.seg,threshold=0.7)

    #分类串联模块
    cls_module = Template(save_path.base_path + "/public/分类模块.png" , threshold=0.7)

    #前置模块
    pre_module = Template(save_path.base_path + "/public/前置模块.png" ,target_pos = 6,threshold=0.7)

    #分割串联模块
    seg_module = Template(save_path.base_path + "/public/分割模块.png" , threshold=0.7)

    #检测串联模块
    det_module = Template(save_path.base_path + "/public/检测模块.png" , threshold=0.7)

    #OCR串联模块
    OCR_module = Template(save_path.base_path + "/public/OCR模块.png" , threshold=0.7)

    #无监督串联模块
    uad_module = Template(save_path.base_path + "/public/无监督模块.png" , threshold=0.7)

    #字符串串联模块
    seq_module = Template(save_path.base_path + "/public/字符串模块.png" , threshold=0.7)

    #快速定位模块
    rapid_module = Template(save_path.base_path + "/public/快速定位模块.png" , threshold=0.7)

    #添加模版
    add_template = Template(save_path.base_path + "/public/20_添加模版.png" ,threshold=0.7)

    #编辑名称
    edit_name = Template(save_path.base_path + "/public/20_编辑名称.png" ,threshold=0.7)

    #模版设定
    template_setting = Template(save_path.base_path + "/public/20_模版设定.png" ,threshold=0.7)

    #单张测试
    single_test = Template(save_path.base_path + "/public/20_单张测试.png" , threshold=0.7)

    #全量测试
    full_test = Template(save_path.base_path + "/public/20_全量测试.png" , threshold=0.7)

    #过滤参数
    filter_parameter = Template(save_path.base_path + "/public/20_参数配置.png" ,target_pos= 5, threshold=0.7)

    #最大目标数
    max_target = Template(save_path.base_path + "/public/20_最大目标数.png" ,target_pos= 6,threshold=0.7)

    #更新数据到后置模块
    update_to_post_module = Template(save_path.base_path + "/public/20_更新数据到后置模块.png" ,threshold=0.7)

    #ROI模块
    roi_module = Template(save_path.base_path + "/public/ROI模块.png" , threshold=0.7)

    #新建ROI
    add_roi = Template(save_path.base_path + "/public/19_自定义ROI.png" ,target_pos= 2 , threshold=0.7)

    #ROI-大小-左边编辑框
    roi_size_left = Template(save_path.base_path + "/public/19_自定义ROI.png" ,target_pos= 4 , threshold=0.7)

    #ROI-大小-右边编辑框
    roi_size_right = Template(save_path.base_path + "/public/19_自定义ROI.png" ,target_pos= 6 , threshold=0.7)

    #ROI-位移-左边编辑框
    roi_displacement_left = Template(save_path.base_path + "/public/19_自定义ROI.png" ,target_pos= 7, threshold=0.7)

    #ROI-位移-右边编辑框
    roi_displacement_right = Template(save_path.base_path + "/public/19_自定义ROI.png" ,target_pos= 9 , threshold=0.7)

    #ROI模式切换
    roi_mode_switching = Template(save_path.base_path + "/public/19_模式切换.png" ,threshold=0.7)

    #ROI比例切分
    proportional_splitting = Template(save_path.base_path + "/public/19_比例切分.png" ,threshold=0.7)

    #点击窗口最大化
    max_screen = Template(save_path.base_path + "/public/01_窗口最大化.png" , threshold=0.7)

    #点击新建方案
    create_project = Template(save_path.base_path + "/public/02_新建方案.png", threshold=0.7)

    #选择方案类型
    project_type = Template(save_path.base_path + "/public/02_方案类型.png", threshold=0.7)

    #选择多模型串并联方案
    pipelines_project = Template(save_path.base_path + "/public/02_多模型串并联方案.png", threshold=0.7)

    #点击打开方案
    open_project = Template(save_path.base_path + "/public/02_打开方案.png", threshold=0.7)

    #方案输入错误提示
    proj_error = Template(save_path.base_path + "/public/03_方案输入错误提示.png",threshold=0.7)

    #选中方案
    click_project = Template(save_path.base_path + "/public/03_pro标志.png", threshold=0.7)

    #右键关闭
    right_click_toclosed = Template(save_path.base_path + "/public/02_右键编辑菜单.png",target_pos= 2, threshold=0.7)

    #右键编辑
    edited = Template(save_path.base_path + "/public/02_右键编辑.png",threshold=0.7)

    #点击home键
    home_button = Template(save_path.base_path + "/public/04_home键.png", threshold=0.7)

    #方案管理输入框
    manage_input = Template(save_path.base_path + "/public/03_方案搜索框.png", threshold=0.7)

    #方案管理算法筛选框
    manage_search = Template(save_path.base_path + "/public/03_算法筛选框.png", threshold=0.7)

    #选择分割算法
    search_seg = Template(save_path.base_path + "/public/03_分割算法.png", threshold=0.7)

    #选中方案
    choice_proj = Template(save_path.base_path + "/public/03_进入项目.png", threshold=0.7)

    #方案备注
    manage_remark = Template(save_path.base_path + "/public/03_方案备注.png", threshold=0.7)

    #创建时备注
    create_remark = Template(save_path.base_path + "/public/03_创建时备注.png", threshold=0.7)

    #点击打开方案按钮
    openproj_button = Template(save_path.base_path + "/public/03_打开.png", threshold=0.7)

    #选中编辑框
    select_textbox = Template(save_path.base_path + "/public/03_方案名称编辑框.png", threshold=0.7)
    
    #输入框
    input_textbox = Template(save_path.base_path + "/public/03_方案名称编辑框1.png", threshold=0.7)

    #确认按钮
    ok_button = Template(save_path.base_path + "/public/04_确认按钮.png", threshold=0.7)

    #确认按钮1
    ok_button1 = Template(save_path.base_path + "/public/04_确认按钮1.png", threshold=0.7)

    #创建按钮
    create_button = Template(save_path.base_path + "/public/05_创建按钮.png", threshold=0.7)

    #数据管理页面
    data_management_page = Template(save_path.base_path + "/public/03_数据管理页面.png", threshold=0.7)

    #点击添加图像下划线
    add_image_underscore = Template(save_path.base_path + "/public/05_添加图像下划线.png",threshold=0.7)

    #点击添加图像
    add_image = Template(save_path.base_path + "/public/05_添加图像.png", threshold=0.7)

    #点击空白区域
    click_area = Template(save_path.base_path + "/public/05_点击空白区域.png",target_pos=2, threshold=0.7)

    #点击添加标注
    add_label = Template(save_path.base_path + "/public/05_添加标注.png", threshold=0.7)

    #点击添加文件夹 
    add_file = Template(save_path.base_path + "/public/05_添加文件夹.png", threshold=0.7)

    #选择文件夹按钮
    choice_file1 = Template(save_path.base_path + "/public/05_路径编辑框1.png",threshold=0.7)

    #选择文件夹按钮
    choice_file = Template(save_path.base_path + "/public/05_路径编辑框.png",target_pos = 5, threshold=0.7)

    #输入文件夹名称
    print_name = Template(save_path.base_path + "/public/03_输入文件夹名称.png", threshold=0.7)

    #点击选择文件夹按钮
    choice_button = Template(save_path.base_path + "/public/05_选择文件夹.png", threshold=0.7)

    #完成标志
    upload_label = Template(save_path.base_path + "/public/05_导入成功.png", threshold=0.7)

    #完成按钮
    upload_done = Template(save_path.base_path + "/public/05_完成按钮1.png", threshold=0.7)

    #标签下拉框
    tag_dropdown = Template(save_path.base_path + "/public/05_标签下拉框.png", threshold=0.7)

    #标签搜索框
    tag_searching = Template(save_path.base_path + "/public/05_标签搜索框.png", threshold=0.7)

    #已标注标注
    finish_labeled = Template(save_path.base_path + "/public/03_已标注.png", threshold=0.7)

    #结果为空
    null_results = Template(save_path.base_path + "/public/03_结果为空.png", threshold=0.7)

    #方案流程
    project_flow = Template(save_path.base_path + "/public/03_方案流程.png", threshold=0.7)

    #添加数据源
    add_dataset = Template(save_path.base_path + "/public/03_添加模块.png", threshold=0.7)

    #数据源模块
    dataset_module = Template(save_path.base_path + "/public/03_数据源1.png",threshold=0.7)

    #图像标注页面
    image_label = Template(save_path.base_path + "/public/06_图像标注页面.png", threshold=0.7)

    #训练比例60%
    train_100 = Template(save_path.base_path + "/public/06_训练比例100.png", threshold=0.7)

    #训练比例
    train_ratio = Template(save_path.base_path + "/public/06_训练比例.png", threshold=0.7)
    
    #自动划分按钮
    auto_divide = Template(save_path.base_path + "/public/06_自动划分.png", threshold=0.7)

    #划分为训练集
    train_set = Template(save_path.base_path + "/public/06_划分为训练集.png", threshold=0.7)

    #导入标注
    import_label = Template(save_path.base_path + "/public/06_导入标注_01.png",target_pos= 4,threshold=0.7)

    #提示
    tip = Template(save_path.base_path + "/public/06_提示.png",target_pos= 8, threshold=0.7)

    #模型训练页面
    model_training = Template(save_path.base_path + "/public/07_模型训练页面.png", threshold=0.7)

    #新增训练小卡片
    add_card = Template(save_path.base_path + "/public/08_新增训练小卡片.png", threshold=0.7)

    #V2训练卡片
    V2_training = Template(save_path.base_path + "/public/08_V2训练卡片.png", threshold=0.7)

    #常规训练
    nomal_training = Template(save_path.base_path + "/public/08_常规训练.png", threshold=0.7)

    #一张新的卡片
    new_card = Template(save_path.base_path + "/public/07_新的卡片.png", threshold=0.7)

    #重命名
    rename_button = Template(save_path.base_path + "/public/08_重命名.png", threshold=0.7)
    
    #编辑
    edit_button = Template(save_path.base_path + "/public/08_编辑.png", threshold=0.7)

    #修改备注
    edit_comment = Template(save_path.base_path + "/public/08_修改备注.png", threshold=0.7)

    #复制
    copy_button = Template(save_path.base_path + "/public/08_复制.png", threshold=0.7)

    #删除
    delete_button = Template(save_path.base_path + "/public/08_删除.png", threshold=0.7)

    #删除弹窗提示
    delete_prompt = Template(save_path.base_path + "/public/08_删除提示.png", threshold=0.7)

    #确认按钮
    training_okbutton = Template(save_path.base_path + "/public/08_确认按钮.png", threshold=0.7)

    #模型选择
    choice_model = Template(save_path.base_path + "/public/09_模型选择.png",target_pos = 5,threshold=0.7)

    #无监督模型选择
    uad_choice_model = Template(save_path.base_path + "/public/09_无监督模型选择.png",threshold=0.7)

    #低功耗
    low_power = Template(save_path.base_path + "/public/09_低功耗.png", threshold=0.7)

    #高精度
    high_power = Template(save_path.base_path + "/public/09_高精度.png", threshold=0.7)

    #无监督分类
    uad_cls = Template(save_path.base_path + "/public/09_无监督分类.png",threshold=0.7)

    #无监督分割
    uad_seg = Template(save_path.base_path + "/public/09_无监督分割.png",threshold=0.7)

    #模型A低功耗
    modelA_low_power = Template(save_path.base_path + "/public/09_模型A低功耗.png", threshold=0.7)

    #模型A高精度
    modelA_high_power = Template(save_path.base_path + "/public/09_模型A高精度.png",target_pos = 2, threshold=0.7)

    #模型B
    modelB = Template(save_path.base_path + "/public/09_模型B.png", threshold=0.7)

    #颜色模式
    color_mode = Template(save_path.base_path + "/public/09_颜色模式.png",target_pos = 6, threshold=0.7)

    #灰度图
    gray_image = Template(save_path.base_path + "/public/09_灰度图.png", threshold=0.7)

    #图像裁切
    image_cropping = Template(save_path.base_path + "/public/09_图像裁切1.png",target_pos = 5, threshold=0.7)

    #确定裁切
    cropping_true = Template(save_path.base_path + "/public/09_确定裁切.png", threshold=0.7)

    #图像缩放
    image_scaling = Template(save_path.base_path + "/public/09_图像缩放.png",target_pos = 5, threshold=0.7)

    #无监督算法图像缩放
    uad_image_scaling = Template(save_path.base_path + "/public/09_无监督图像缩放.png",target_pos = 5, threshold=0.7)

    #等比例缩放
    equal_size = Template(save_path.base_path + "/public/09_等比例缩放.png", threshold=0.7)

    #自定义缩放
    zidingyi_size = Template(save_path.base_path + "/public/09_自定义尺寸.png", threshold=0.7)

    #自定义编辑框1
    zidingyi_edit_box1 = Template(save_path.base_path + "/public/09_自定义编辑框.png",target_pos = 4,threshold=0.7)

    #自定义编辑框2
    zidingyi_edit_box2 = Template(save_path.base_path + "/public/09_自定义编辑框.png",target_pos = 5,threshold=0.7)

    #鼠标定位至批次大小
    mouse_move = Template(save_path.base_path + "/public/09_开benchsize.png", target_pos= 5,threshold=0.7)

    #选项为自定义
    zidingyi_button = Template(save_path.base_path + "/public/10_选择自定义.png", target_pos= 8, threshold=0.7)

    #下调benchsize
    cut_benchsize = Template(save_path.base_path + "/public/11_batchsize下调按钮.png",target_pos = 6,threshold=0.7)

    #设置学习次数
    set_study = Template(save_path.base_path + "/public/11_设置学习次数.png",threshold=0.7)

    #缺陷生成设置学习次数
    generation_study = Template(save_path.base_path + "/public/11_缺陷生成设置学习次数.png",threshold=0.7)

    #字符串阶段一
    seq_step1_study = Template(save_path.base_path + "/public/11_字符串设置学习次数.png",target_pos = 4,threshold=0.7)

    #字符串阶段二
    seq_step2_study = Template(save_path.base_path + "/public/11_字符串设置学习次数.png",target_pos = 5,threshold=0.7)

    #字符串阶段三
    seq_step3_study = Template(save_path.base_path + "/public/11_字符串设置学习次数.png",target_pos = 6,threshold=0.7)

    #OCV阶段一
    ocv_step1_study = Template(save_path.base_path + "/public/11_ocv设置学习次数.png",target_pos = 5,threshold=0.7)

    #OCV阶段二
    ocv_step2_study = Template(save_path.base_path + "/public/11_ocv设置学习次数.png",target_pos = 6,threshold=0.7)

    #点击开始训练
    star_training = Template(save_path.base_path + "/public/12_开始训练.png",threshold=0.9)

    #继续训练
    continu_training = Template(save_path.base_path + "/public/08_继续训练.png", threshold=0.7)

    #增量训练
    add_training = Template(save_path.base_path + "/public/08_增量训练.png", threshold=0.7)

    #参数配置为模版
    set_template = Template(save_path.base_path + "/public/08_保存参数为模板.png", threshold=0.7)

    #通过模板创建
    create_using_template = Template(save_path.base_path + "/public/08_通过模板创建.png", threshold=0.7)

    #任务完成标志
    task_finished = Template(save_path.base_path + "/public/12_任务完成1.png", threshold=0.7)

    #关闭任务完成标志
    close_task = Template(save_path.base_path + "/public/12_关闭任务完成.png", target_pos = 6,threshold=0.7)

    #点击查看评估
    review_assess = Template(save_path.base_path + "/public/12_查看评估.png",rgb=True,threshold=0.8)

    #停止训练
    stop_training = Template(save_path.base_path + "/public/12_停止训练.png",rgb=True,threshold=0.7)

    #训练失败
    training_failed = Template(save_path.base_path + "/public/12_训练失败.png",rgb= True,threshold=0.7)

    #训练报错
    training_error = Template(save_path.base_path + "/public/12_训练报错.png",threshold=0.7)

    #模型评估页面
    model_assess = Template(save_path.base_path + "/public/13_模型评估页面.png", threshold=0.7)

    #切换至类别级别
    change_type = Template(save_path.base_path + "/public/14_切换类别.png", threshold=0.7)
    
    #导出报告按钮
    report_button = Template(save_path.base_path + "/public/14_导出报告.png", threshold=0.7)
    
    #点击更多按钮
    more_button = Template(save_path.base_path + "/public/14_右侧更多按钮.png", threshold=0.7)

    #选中导出模型
    export_model = Template(save_path.base_path + "/public/14_导出模型按钮.png", threshold=0.7)

    #导出SDK
    export_SDK = Template(save_path.base_path + "/public/14_导出SDK.png", threshold=0.7)

    #点击选择文件夹按钮
    file_name = Template(save_path.base_path + "/public/14_选择文件夹.png", threshold=0.7)

    #点击导出报告选择文件夹
    report_name = Template(save_path.base_path + "/public/15_导出报告文件夹.png", threshold=0.7)

    #包含参数设置
    add_parameter = Template(save_path.base_path + "/public/15_增加参数配置.png",target_pos = 6,threshold = 0.7)

    #选中编辑框
    edit_box = Template(save_path.base_path + "/public/14_路径输入框.png", threshold=0.7) 

    #点击跳转
    jump_click = Template(save_path.base_path +"/public/14_跳转.png", threshold=0.7)

    #点击导出按钮
    export_button = Template(save_path.base_path + "/public/14_导出按钮.png", threshold=0.7)

    #混淆矩阵
    confusion_matrix =  Template(save_path.base_path + "/public/14_混淆矩阵.png", threshold=0.7)

    #敏感区域
    sensitive_area = Template(save_path.base_path + "/public/14_敏感区域.png", threshold=0.7)

    #后处理参数配置
    process_setting = Template(save_path.base_path + "/public/14_后处理参数配置.png", threshold=0.7)

    #判断导出成功
    report_success =  Template(save_path.base_path + "/public/16_判断报告是否导出成功.png", threshold=0.7)

    #点击文件按钮
    template_file = Template(save_path.base_path + "/public/15_文件按钮.png", threshold=0.7)

    #点击设置按钮
    setting_button = Template(save_path.base_path + "/public/15_设置按钮.png", threshold=0.7)

    #导入扩展包
    template_extension = Template(save_path.base_path + "/public/15_导入扩展包.png", threshold=0.7)

    #导入
    template_import = Template(save_path.base_path + "/public/15_导入.png", threshold=0.7)

    #深色版本
    change_theme =  Template(save_path.base_path + "/public/15_深色主题.png", threshold=0.7)

    #点击导出SDK按钮
    template_SDK = Template(save_path.base_path + "/public/15_导出SDK.png", threshold=0.7)

    #点击帮助按钮
    template_help = Template(save_path.base_path + "/public/15_帮助按钮.png", threshold=0.7)

    #点击关闭方案
    template_close = Template(save_path.base_path + "/public/16_关闭方案.png", threshold=0.7)

    #高级设置
    template_advanced = Template(save_path.base_path + "/public/16_高级设置.png", threshold=0.7)

    #算法训练进程数
    template_process = Template(save_path.base_path + "/public/16_算法训练进程数.png", threshold=0.7)

    #automl迭代强度
    template_automl = Template(save_path.base_path + "/public/16_automl迭代强度.png", threshold=0.7)

    #实例最大检出数
    template_max_detection = Template(save_path.base_path + "/public/16_实例最大检出数.png", threshold=0.7)

    #点击软件功能手册
    user_guild = Template(save_path.base_path + "/public/16_软件功能手册.png",target_pos = 8, threshold=0.7)

    #点击软件操作手册
    operating_guild = Template(save_path.base_path + "/public/16_软件操作手册.png", threshold=0.7) 

    #判断软件使用手册导出成功
    user_success = Template(save_path.base_path + "/public/16_判断软件使用手册导出成功.png", threshold=0.7)

    #点击SDK开发手册
    SDK_guild = Template(save_path.base_path + "/public/16_SDK开发手册.png", threshold=0.7)

    #c++
    guild_c =  Template(save_path.base_path + "/public/16_c++.png", threshold=0.7)

    #csharp
    guild_csharp =  Template(save_path.base_path + "/public/16_csharp.png", threshold=0.7)

    #python
    guild_python = Template(save_path.base_path + "/public/16_python.png", threshold=0.7)

    #判断SDK开发手册导出成功
    SDK_success = Template(save_path.base_path + "/public/16_判断SDK开发手册导出成功.png", threshold=0.7)

    #退出
    template_quit = Template(save_path.base_path + "/public/16_退出.png", threshold=0.7)

    #模型推理页面
    model_infering = Template(save_path.base_path + "/public/17_模型推理页面.png", threshold=0.7)

    #导入图片文件夹
    images_input = Template(save_path.base_path + "/public/17_导入图片.png", threshold=0.7)

    #文件导入成功
    file_upload = Template(save_path.base_path + "/public/17_完成按钮.png", threshold=0.7)

    #开始推理
    begin_infering = Template(save_path.base_path + "/public/17_开始推理.png",rgb= True, threshold=0.7)

    #重新推理
    return_infering = Template(save_path.base_path + "/public/17_重新推理.png",rgb= True, threshold=0.7)

    #推理完成
    infering_finished = Template(save_path.base_path + "/public/17_推理完成.png",rgb= True, threshold=0.7)

    #解锁标志
    unlock_logo = Template(save_path.base_path + "/public/17_解锁标志 .png", threshold=0.7)

    #模式选择
    pattern_choice = Template(save_path.base_path + "/public/17_模式选择.png", threshold=0.7)

    #TRT FP32模式
    FP32_TRT = Template(save_path.base_path + "/public/17_FP32.png", threshold=0.7)

    #TRT FP16模式
    FP16_TRT = Template(save_path.base_path + "/public/17_FP16.png", threshold=0.7)

    #设备类型
    device_type = Template(save_path.base_path + "/public/17_设备类型.png", threshold=0.7)

    #选择CPU设备
    device_CPU = Template(save_path.base_path + "/public/17_选择CPU.png",target_pos = 5,threshold=0.7)

    #批量推理
    batch_infering = Template(save_path.base_path + "/public/17_批量推理.png",threshold=0.7)

    #导出渲染图
    rendering_image = Template(save_path.base_path + "/public/17_导出渲染图.png", threshold=0.7)

    #综合判定
    judgement_page = Template(save_path.base_path + "/public/18_综合判定.png", threshold=0.7)

    #判定范围
    judgement_area = Template(save_path.base_path + "/public/18_判定功能.png", target_pos = 4,threshold=0.7)

    # 判定规则
    judgement_rules = Template(save_path.base_path + "/public/18_判定功能.png", target_pos = 5,threshold=0.7) 

    #添加规则
    add_rules = Template(save_path.base_path + "/public/18_添加标准.png",threshold=0.7)

    # 开始推理 
    judgement_infering = Template(save_path.base_path + "/public/18_判定功能.png", target_pos = 6,threshold=0.7)   

    #复选框
    checkbox = Template(save_path.base_path + "/public/18_复选框.png",threshold=0.7) 

    #判定范围
    judge_checkbox = Template(save_path.base_path + "/public/18_判定范围.png",threshold=0.7)

    # #分类特征_OK
    # judge_ok = Template(save_path.base_path + "/public/18_分类特征ok.png",threshold=0.7)

    # #分类特征_NG
    # cls_ng = Template(save_path.base_path + "/public/18_分类特征ng.png",threshold=0.7)

    # #分割判定范围
    # seg_checkbox = Template(save_path.base_path + "/public/18_判定范围.png",target_pos = 5,threshold=0.7)

    # #分割规则
    # seg_rule = Template(save_path.base_path + "/public/18_分割规则.png",target_pos = 5,threshold=0.7)

    # #检测判定范围
    # det_checkbox = Template(save_path.base_path + "/public/18_判定范围.png",target_pos = 8,threshold=0.7)

    #保存
    save_button = Template(save_path.base_path + "/public/18_保存按钮.png",threshold=0.7)   

    #综合判定完成
    judgement_done =  Template(save_path.base_path + "/public/18_综合判定完成.png",threshold=0.7)   

    #综合判定开始推理按钮
    judgement_infering_button = Template(save_path.base_path + "/public/18_判定开始推理.png",threshold=0.7)

    #判定页面图像筛选框
    judgement_search =  Template(save_path.base_path + "/public/18_图像筛选框.png",threshold=0.7)

    #筛选结果
    select_image = Template(save_path.base_path + "/public/18_筛选结果.png",threshold=0.7)

    #取消选中复选框
    cancel_select = Template(save_path.base_path + "/public/18_已勾选.png",threshold=0.7)

    #高级配置
    advanced = Template(save_path.base_path + "/public/18_高级配置.png",threshold=0.7)

    #不使用加速
    not_use_acceleration = Template(save_path.base_path + "/public/18_不使用加速.png",threshold=0.7)

    #使用trtfp16加速
    use_trt_16acceleration = Template(save_path.base_path + "/public/18_使用fp16加速.png",threshold=0.7)

    #导出所有模块渲染图
    export_rendering_image = Template(save_path.base_path + "/public/18_导出所有模块渲染图.png",threshold=0.7)

    #类别级别
    type_image = Template(save_path.base_path + "/public/类别级别.png",threshold=0.7)

    #像素级别
    pixel_image = Template(save_path.base_path + "/public/像素级别.png",threshold=0.7)

    #字符级别
    ocr_image = Template(save_path.base_path + "/public/字符级别.png",threshold=0.7)

    #内容级别
    content_image = Template(save_path.base_path + "/public/内容级别.png",threshold=0.7)

    #切换为类别级别
    change_type_image = Template(save_path.base_path + "/public/切换为类别级别.png",threshold=0.7)

    #导入完成
    import_done = Template(save_path.base_path + "/public/21_导入完成.png",threshold=0.7)

#标注工具控件
class label_control():   
    #添加特征按钮
    add_characteristic = Template(save_path.base_path + "/auto_label/00_添加特征.png" , threshold=0.7) 

    #名称编辑框
    name_edit = Template(save_path.base_path + "/auto_label/00_名称编辑框.png" , threshold=0.7)

    #确认添加按钮
    confirm_button = Template(save_path.base_path + "/auto_label/00_确认.png" , threshold=0.7) 

    #合格样本工具
    acceptable_sample_tool = Template(save_path.base_path + "/auto_label/00_合格样本.png" , threshold=0.7)

    #选择特征标签
    select_characteristic = Template(save_path.base_path + "/auto_label/00_选择特征标签.png" , threshold=0.7)

    #确认选中特征标签
    select_true = Template(save_path.base_path + "/auto_label/00_确认选中标签.png" , threshold=0.7)

    #置为背景
    set_background = Template(save_path.base_path + "/auto_label/07_置为背景.png" , threshold=0.7)

    #编辑信息
    edit_content = Template(save_path.base_path + "/auto_label/07_编辑信息.png" , threshold=0.7)

    #特征名称
    characteristic_name = Template(save_path.base_path + "/auto_label/07_特征名称.png" , threshold=0.7)

    #矩形工具
    rectangle_tool = Template(save_path.base_path + "/auto_label/01_矩形工具.png" , threshold=0.7)

    #智能矩形
    auto_rectangle_tool = Template(save_path.base_path + "/auto_label/03_智能矩形.png" , threshold=0.7)

    #快速定位矩形工具
    rapid_rectangle_tool = Template(save_path.base_path + "/auto_label/02_快速定位矩形工具.png" , target_pos= 5,threshold=0.7)

    #环形工具
    circle_tool = Template(save_path.base_path + "/auto_label/06_环形工具.png" , threshold=0.7)

    #多边形工具
    polygon_tool = Template(save_path.base_path + "/auto_label/02_多边形工具.png" , threshold=0.7)

    #画笔工具
    brush_tool = Template(save_path.base_path + "/auto_label/02_画笔工具.png" , threshold=0.7)

    #AI标注
    AI_tool = Template(save_path.base_path + "/auto_label/02_AI标注.png" , threshold=0.7)

    #笔形工具
    pen_tool = Template(save_path.base_path + "/auto_label/02_笔形工具.png", threshold=0.7)

    #线工具
    line_tool = Template(save_path.base_path + "/auto_label/02_线工具.png" , threshold=0.7)

    #折线工具
    polyline_tool = Template(save_path.base_path + "/auto_label/02_折线工具.png" , threshold=0.7)

    #屏蔽区域
    masking_area = Template(save_path.base_path + "/auto_label/02_屏蔽区域.png" , threshold=0.7)

    #动态正选
    dynamic_selection = Template(save_path.base_path + "/auto_label/02_动态屏蔽.png" ,target_pos= 4, threshold=0.7)

    #动态反选
    dynamic_deselection = Template(save_path.base_path + "/auto_label/02_动态屏蔽.png" ,target_pos= 5, threshold=0.7)
    
    #自动标注
    auto_marking = Template(save_path.base_path + "/auto_label/03_自动标注.png" , threshold=0.7)

    #开始标注
    begin_marking = Template(save_path.base_path + "/auto_label/03_开始标注.png" , threshold=0.7)

    #应用
    apply = Template(save_path.base_path + "/auto_label/03_应用.png" ,rgb=True,threshold=0.7)

    #添加标签
    add_marking = Template(save_path.base_path + "/auto_label/04_添加标签.png" ,threshold=0.7)

    #NG样本工具
    NG_sample_tool = Template(save_path.base_path + "/auto_label/05_NG样本.png" ,threshold=0.7)

#深色版本公共控件
class dark_control():
    #分割模块
    seg_module = Template(save_path.base_path + "/public_dark/分割模块.png", threshold=0.7)
    
    #切换主题
    change_theme = Template(save_path.base_path + "/public_dark/00_浅色主题.png", threshold=0.7)
    
    #新建方案
    create_project = Template(save_path.base_path + "/public_dark/00_新建方案.png" , threshold=0.7) 

    #选中编辑框
    select_textbox = Template(save_path.base_path + "/public_dark/00_方案名称编辑框.png", threshold=0.7)

    #方案类型
    project_type = Template(save_path.base_path + "/public_dark/00_方案类型.png", threshold=0.7)
    
    #多模型串并联方案
    pipelines_project = Template(save_path.base_path + "/public_dark/00_多模型串并联方案.png", threshold=0.7)

    #创建按钮
    create_button = Template(save_path.base_path + "/public_dark/00_创建按钮.png", threshold=0.7)

    #添加图像
    add_image = Template(save_path.base_path + "/public_dark/01_添加图像.png", threshold=0.7)

    #导入成功
    upload_label = Template(save_path.base_path + "/public_dark/01_导入成功.png", threshold=0.7)

    #完成按钮
    upload_done = Template(save_path.base_path + "/public_dark/01_完成按钮.png", threshold=0.7)

    #添加标注
    add_label = Template(save_path.base_path + "/public_dark/01_添加标注.png", threshold=0.7)
    
    #方案流程
    project_flow = Template(save_path.base_path + "/public_dark/01_方案流程.png", threshold=0.7)
    
    #数据源
    data_source = Template(save_path.base_path + "/public_dark/02_数据源.png",target_pos= 6 , threshold=0.7)

    #图像标注页面
    image_label = Template(save_path.base_path + "/public_dark/02_图像标注页面.png", threshold=0.7)

    #训练比例60%
    train_60 = Template(save_path.base_path + "/public_dark/02_训练比例60.png", threshold=0.7)

    #训练比例
    train_ratio = Template(save_path.base_path + "/public_dark/02_训练比例.png", threshold=0.7)

    #自动划分按钮
    auto_divide = Template(save_path.base_path + "/public_dark/02_自动划分.png", threshold=0.7)

    #导入标注
    import_label =  Template(save_path.base_path + "/public_dark/02_导入标注.png", threshold=0.7) 
    
    #添加模块
    add_module = Template(save_path.base_path + "/public_dark/02_添加模块.png", threshold=0.7) 

    #模型训练页面
    model_training = Template(save_path.base_path + "/public_dark/03_模型训练.png", threshold=0.7)
    
    #新增训练小卡片
    add_card = Template(save_path.base_path + "/public_dark/03_新增训练小卡片.png", threshold=0.7)

    #常规训练
    nomal_training = Template(save_path.base_path + "/public_dark/03_常规训练.png", threshold=0.7)

    #设置学习次数
    set_study = Template(save_path.base_path + "/public_dark/03_设置学习次数.png", threshold=0.7)
    
    #鼠标定位至批次大小
    mouse_move = Template(save_path.base_path + "/public_dark/03_开batchsize.png", target_pos= 5,threshold=0.7)
    
    #选项为自定义
    zidingyi_button = Template(save_path.base_path + "/public_dark/03_选择自定义.png", target_pos= 8, threshold=0.7)

    #下调benchsize
    cut_benchsize = Template(save_path.base_path + "/public_dark/03_下调batchsize按钮.png",target_pos = 6,threshold=0.7)

    #开始训练
    star_training = Template(save_path.base_path + "/public_dark/03_开始训练.png", threshold=0.7)

    #模型评估页面
    model_assess = Template(save_path.base_path + "/public_dark/04_模型评估.png", threshold=0.7)

    #评估完成
    infering_finished = Template(save_path.base_path + "/public_dark/04_评估完成.png",rgb= True,threshold=0.7)
    
    #模型推理页面
    model_infering =  Template(save_path.base_path + "/public_dark/05_模型推理.png",threshold=0.7)   
    
    #导入图片
    images_input = Template(save_path.base_path + "/public_dark/05_导入图片.png",threshold=0.7)

    #开始推理
    begin_infering = Template(save_path.base_path + "/public_dark/05_开始推理.png",threshold=0.7)

def get_button_from_string(button_string):
    """
    根据给定的字符串获取按钮对象。

    参数:
        button_string (str): 包含模块名和属性名的字符串，如 'control.create_project'

    返回:
        object: 按钮对象
    """
    module_name, attr_name = button_string.split('.')  # 分割模块名和属性名
    module = globals().get(module_name)  # 获取模块对象
    
    if module is None:
        raise ImportError(f"模块 '{module_name}' 未找到")
    
    button_object = getattr(module, attr_name)  # 获取实际按钮对象
    return button_object