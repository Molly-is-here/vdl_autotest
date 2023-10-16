from airtest.core.api import *
from elements.elements_path import save_path

#公共控件
class control():
    #分割算法
    seg_item = Template(save_path.seg,threshold=0.7)

    #点击窗口最大化
    max_screen = Template(save_path.base_path + "/public/01_窗口最大化.png" , threshold=0.7)

    #点击新建方案
    create_project = Template(save_path.base_path + "/public/02_新建方案.png", threshold=0.7)

    #点击打开方案
    open_project = Template(save_path.base_path + "/public/02_打开方案.png", threshold=0.7)

    #方案输入错误提示
    proj_error = Template(save_path.base_path + "/public/03_方案输入错误提示.png", threshold=0.7)

    #选中方案
    click_project = Template(save_path.base_path + "/public/03_pro标志.png", threshold=0.7)

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

    #点击打开方案按钮
    openproj_button = Template(save_path.base_path + "/public/03_打开.png", threshold=0.7)

    #选中编辑框
    select_textbox = Template(save_path.base_path + "/public/03_方案名称编辑框.png", threshold=0.7)

    #确认按钮
    ok_button = Template(save_path.base_path + "/public/04_确认按钮1.png", threshold=0.7)

    #创建按钮
    create_button = Template(save_path.base_path + "/public/05_创建按钮.png", threshold=0.7)

    #数据管理页面
    data_management_page = Template(save_path.base_path + "/public/03_数据管理页面.png", threshold=0.7)

    #点击添加图像下划线
    add_image_underscore = Template(save_path.base_path + "/public/05_添加图像下划线.png", target_pos = 9,threshold=0.7)

    #点击添加图像
    add_image = Template(save_path.base_path + "/public/05_添加图像.png", threshold=0.7)

    #点击空白区域
    click_area = Template(save_path.base_path + "/public/05_点击空白区域.png", threshold=0.7)

    #点击添加标注
    add_label = Template(save_path.base_path + "/public/05_添加标注.png", threshold=0.7)

    #点击添加文件夹 
    add_file = Template(save_path.base_path + "/public/05_添加文件夹.png", threshold=0.7)

    #选择文件夹按钮
    choice_file1 = Template(save_path.base_path + "/public/05_路径编辑框3.png", threshold=0.7)

    #选择文件夹按钮
    choice_file = Template(save_path.base_path + "/public/05_路径编辑框2.png",target_pos = 5, threshold=0.7)

    #输入文件夹名称
    print_name = Template(save_path.base_path + "/public/03_输入文件夹名称.png", threshold=0.7)

    #点击选择文件夹按钮
    choice_button = Template(save_path.base_path + "/public/05_选择文件夹.png", threshold=0.7)

    #完成标志
    upload_label = Template(save_path.base_path + "/public/05_导入成功.png", threshold=0.7)

    #完成按钮
    upload_done = Template(save_path.base_path + "/public/05_完成按钮.png", threshold=0.7)

    #未完成标注
    unfinish_labeled = Template(save_path.base_path + "/public/03_未完成标注.png", threshold=0.7)

    #结果为空
    null_results = Template(save_path.base_path + "/public/03_结果为空.png", threshold=0.7)

    #图像标注页面
    image_label = Template(save_path.base_path + "/public/06_图像标注页面.png", threshold=0.7)
    
    #自动划分按钮
    auto_divide = Template(save_path.base_path + "/public/06_自动划分.png", threshold=0.7)

    #模型训练页面
    model_training = Template(save_path.base_path + "/public/07_模型训练页面.png", threshold=0.7)

    #新增训练小卡片
    add_card = Template(save_path.base_path + "/public/08_新增训练小卡片.png", threshold=0.7)

    #常规训练
    nomal_training = Template(save_path.base_path + "/public/08_常规训练.png", threshold=0.7)

    #一张新的卡片
    new_card = Template(save_path.base_path + "/public/07_新的卡片.png", threshold=0.7)

    #重命名
    rename_button = Template(save_path.base_path + "/public/08_重命名.png", threshold=0.7)

    #修改备注
    edit_comment = Template(save_path.base_path + "/public/08_修改备注.png", threshold=0.7)

    #复制
    copy_button = Template(save_path.base_path + "/public/08_复制.png", threshold=0.7)

    #删除
    delete_button = Template(save_path.base_path + "/public/08_删除.png", threshold=0.7)

    #删除弹窗提示
    delete_prompt = Template(save_path.base_path + "/public/08_删除提示.png", threshold=0.7)

    #删除确认按钮
    training_okbutton = Template(save_path.base_path + "/public/08_确认按钮.png", threshold=0.7)

    #模型选择
    choice_model = Template(save_path.base_path + "/public/09_模型选择.png",target_pos = 6,threshold=0.7)

    #低功耗
    low_power = Template(save_path.base_path + "/public/09_低功耗.png", threshold=0.7)

    #高精度
    high_power = Template(save_path.base_path + "/public/09_高精度.png", threshold=0.7)

    #颜色模式
    color_mode = Template(save_path.base_path + "/public/09_颜色模式.png",target_pos = 6, threshold=0.7)

    #灰度图
    gray_image = Template(save_path.base_path + "/public/09_灰度图.png", threshold=0.7)

    #图像裁切
    image_cropping = Template(save_path.base_path + "/public/09_图像裁切.png",target_pos = 6, threshold=0.7)

    #确定裁切
    cropping_true = Template(save_path.base_path + "/public/09_确定裁切.png", threshold=0.7)

    #图像缩放
    image_scaling = Template(save_path.base_path + "/public/09_图像缩放1.png",target_pos = 5, threshold=0.7)

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
    mouse_move = Template(save_path.base_path + "/public/09_开benchsize.png", threshold=0.7)

    #选项为自定义
    zidingyi_button = Template(save_path.base_path + "/public/10_选择自定义.png", threshold=0.7)

    #下调benchsize
    cut_benchsize = Template(save_path.base_path + "/public/11_benchsize下调按钮.png",target_pos = 6,threshold=0.7)

    #设置学习次数
    set_study = Template(save_path.base_path + "/public/11_设置学习次数.png",threshold=0.7)

    #点击开始训练
    star_training = Template(save_path.base_path + "/public/12_开始训练.png", threshold=0.7)

    #继续训练
    continu_training = Template(save_path.base_path + "/public/08_继续训练.png", threshold=0.7)

    #增量训练
    add_training = Template(save_path.base_path + "/public/08_增量训练.png", threshold=0.7)

    #任务完成标志
    task_finished = Template(save_path.base_path + "/public/12_任务完成1.png", threshold=0.7)

    #关闭任务完成标志
    close_task = Template(save_path.base_path + "/public/12_关闭任务完成.png", target_pos = 6,threshold=0.7)

    #点击查看评估
    review_assess = Template(save_path.base_path + "/public/12_查看评估.png",rgb=True,threshold=0.7)

    #切换至模型评估页面
    model_assess = Template(save_path.base_path + "/public/13_模型评估页面.png", threshold=0.7)

    #切换至类别级别
    change_type = Template(save_path.base_path + "/public/14_切换类别.png", threshold=0.7)
    
    #导出报告按钮
    report_button = Template(save_path.base_path + "/public/14_导出报告.png", threshold=0.7)
    
    #点击更多按钮
    more_button = Template(save_path.base_path + "/public/14_右侧更多按钮.png", threshold=0.7)

    #选中导出模型
    export_model = Template(save_path.base_path + "/public/14_导出模型按钮.png", threshold=0.7)

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

    #判断导出成功
    report_success =  Template(save_path.base_path + "/public/16_判断报告是否导出成功.png", threshold=0.7)

    #点击文件按钮
    template_file = Template(save_path.base_path + "/public/15_文件按钮.png", threshold=0.7)

    #点击帮助按钮
    template_help = Template(save_path.base_path + "/public/15_帮助按钮.png", threshold=0.7)

    #点击关闭方案
    template_close = Template(save_path.base_path + "/public/16_关闭方案.png", threshold=0.7)

    #点击软件使用手册
    user_guild = Template(save_path.base_path + "/public/16_软件使用手册.png", threshold=0.7)

    #判断软件使用手册导出成功
    user_success = Template(save_path.base_path + "/public/16_判断软件使用手册导出成功.png", threshold=0.7)

    #点击SDK开发手册
    SDK_guild = Template(save_path.base_path + "/public/16_SDK开发手册.png", threshold=0.7)

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
    begin_infering = Template(save_path.base_path + "/public/17_开始推理.png", threshold=0.7)

    #推理完成
    infering_finished = Template(save_path.base_path + "/public/17_推理完成.png",rgb= True, threshold=0.7)

    #解锁标志
    unlock_logo = Template(save_path.base_path + "/public/17_解锁标志 .png", threshold=0.7)

    #模式选择
    pattern_choice = Template(save_path.base_path + "/public/17_模式选择.png", threshold=0.7)

    #选择TRT模式
    pattern_TRT = Template(save_path.base_path + "/public/17_切换为TRT.png", threshold=0.7)

    #设备类型
    device_type = Template(save_path.base_path + "/public/17_设备类型.png", threshold=0.7)

    #选择CPU设备
    device_CPU = Template(save_path.base_path + "/public/17_选择CPU.png",target_pos = 5,threshold=0.7)
