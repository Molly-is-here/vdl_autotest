import random
import time
import subprocess
import re
import os
from airtest.core.api import *
from airtest.core.api import start_app
from pywinauto import Application

#选择模型类型（四类算法）
cls = r".\public\分类算法.png"
det = r".\public\检测算法.png"
seg = r".\public\分割算法.png"
ocr = r".\public\OCR算法.png"
project_list = [cls,det,seg,ocr]

#数据集（四类算法）
base_path = os.path.dirname(__file__)
cls_dataset = base_path + r"/分类算法/dataset"
det_dataset = base_path + r"/检测算法/dataset"
seg_dataset = base_path + r"/分割算法/dataset"
ocr_dataset = base_path + r"/ocr算法/dataset"

os.chdir(r"D:\ly\00_VDL\0612_0.3.4.0\ViMo-Deeplearning")

#打开软件
app = Application().start(r".\VDL.exe")
sleep(5.0)

#连接当前设备
connect_device("Windows:///?title_re=MainWindow.*")
sleep(2.0)

#将当前窗口截图
snapshot("当前窗口截图.png")

#点击窗口最大化
template_1 = Template(base_path + "\elements\public\01_窗口最大化.png", threshold=0.7)
pos_1 = exists(template_1)  #查找控件
if pos_1 is not None:
        #如果存在则选择点击
        touch(pos_1)
else:
    # 没有找到模板图片
    print("窗口最大化失败")
sleep(1.0)

#点击新建方案
create_project = Template(base_path + "/public/02_新建方案.png", threshold=0.7)
pos_create_project = exists(create_project) #查找控件

#选中编辑框
select_textbox = Template(base_path + "/public/03_方案名称编辑框.png", threshold=0.7)
pos_select_textbox = exists(select_textbox) #查找控件

#创建按钮
create_button = Template(base_path + "/public/05_创建按钮.png", threshold=0.7)
pos_create_button = exists(create_button) #查找控件

#点击添加文件夹 
add_file = Template(base_path + "/public/05_添加文件夹.png", threshold=0.7)
pos_add_file = exists(add_file) #查找控件

#选择文件夹按钮
choice_file = Template(base_path + "/public/05_选择文件夹.png", threshold=0.7)
pos_choice_file = exists(choice_file) #查找控件

#完成按钮
upload_done = Template(base_path + "/public/05_完成按钮.png", threshold=0.7)
pos_upload_done = exists(upload_done) #查找控件

#获得随机数
def get_character(length):
        character = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','x','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        radom_character = ''
        random.seed(time.time())
        for i in range(length): 
            radom_character += random.choice(character)
            input_character = "测试" + radom_character
            
        return input_character

#查看当前算法类型       
def get_params(param):
    print('查看当前算法类型：', param)

#遍历文件夹
def get_file(file_path):
     count = 0
     for root,dirs,files in os.walk(file_path):
          for file in files:
               count += 1 
               yield file
               print(count)            
     return file

#创建一个算法模板
def algorithm_template(item):
     #判断算法类型后再指定数据集
     for item in project_list:
        if item ==seg:
            dataset = seg_dataset
        if item == cls:
            dataset = cls_dataset
        if item == det:
            dataset = det_dataset
        if item == ocr:
            dataset = ocr_dataset

        for file in get_file(dataset):
            #点击新建方案
            touch(create_project)
            sleep(1.0)

            #选中编辑框
            touch(select_textbox)

            #输入方案名称
            random_string = get_character(3)
            text(random_string)
            sleep(1.0)
            
            #选择模型类型
            template_type = Template(item, threshold=0.7)
            pos_template_type = exists(template_type) #查找控件

            if pos_template_type is not None:
                touch(pos_template_type)
            else:
                print("未找模型类型")

            sleep(1.0)

            #点击创建按钮
            touch(create_button)

            #点击添加文件夹 
            touch(add_file)
            sleep(2.0)

            file_path = os.path.join(dataset,file)
            print(file_path)
            data_file = Template(file_path, threshold=0.7)
            pos_data_file = exists(data_file)#查找控件

            if pos_data_file is not None:
                touch(pos_data_file)
            else:
                print("数据集打开失败")

            #点击选择文件夹
            touch(choice_file)
            sleep(10.0)

            #点击完成按钮
            touch(upload_done)
            sleep(1.0)

            #切换图像标注页面
            template_7 = Template(r".\public\06_图像标注页面.png", threshold=0.7)
            pos_7 = exists(template_7) #查找控件

            if pos_7 is not None:
                # 切换至图像标注页面
                touch(pos_7)
            else:
                print("图像标注页面切换失败")

            sleep(1.0)

            #点击自动划分
            auto_divide = Template(r".\public\06_自动划分.png", threshold=0.7)
            pos_auto_divide = exists(auto_divide) #查找控件

            if pos_auto_divide is not None:
            # 点击自动划分按钮
                touch(pos_auto_divide)
            else:
                print("自动划分失败")

            sleep(1.0)


            #切换模型训练页面
            template_8 = Template(r".\public\07_模型训练页面.png", threshold=0.7)
            pos_8 = exists(template_8) #查找控件

            if pos_8 is not None:
                #切换至模型训练页面
                touch(pos_8)
            else:
                # 没有找到模板图片
                print("模型训练页面切换失败")

            sleep(1.0)

            #新增训练小卡片
            template_9 = Template(r".\public\08_新增训练小卡片.png", threshold=0.7)
            pos_9 = exists(template_9) #查找控件

            if pos_9 is not None:
                #新增训练小卡片
                touch(pos_9)
            else:
                print("新增卡片失败")

            sleep(1.0)


            #######以下步骤在真实使用时可以省略，真实使用时按默认配置处理#####
            #鼠标定位至批次大小
            template_10 = Template(r".\public\09_开benchsize.png", threshold=0.7)
            pos_10 = exists(template_10) #查找控件

            if pos_10 is not None:
                #点击批次大小下拉框
                touch(pos_10)
            else:
                # 没有找到模板图片
                print("批次大小下拉框无法选中")

            sleep(1.0)

            #选项为自定义
            template_11 = Template(r".\public\10_选择自定义.png", threshold=0.7)
            pos_11 = exists(template_11) #查找控件

            if pos_11 is not None:
                #选择自定义
                touch(pos_11)
            else:
                print("自定义选项未选中")

            sleep(1.0)

            #下调benchsize
            template_12 = Template(r".\public\11_benchsize下调按钮.png", threshold=0.7)
            pos_12 = exists(template_12) #查找控件

            if pos_12 is not None:
                #点击下调按钮
                touch(pos_12,times= 3)
            else:
                # 没有找到模板图片
                print("下调按钮点击无效")

            sleep(1.0)

            #####截止到这里是可以屏蔽的###

            #点击开始训练
            template_13 = Template(r".\public\12_开始训练.png", threshold=0.7)
            pos_13 = exists(template_13) #查找控件

            if pos_13 is not None:
                #点击开始训练按钮
                touch(pos_13)
            else:
                print("未正常开启训练")

            sleep(2.0)

            #切换模型评估页面
            template_17 = Template(r".\public\13_模型评估页面.png", threshold=0.7)
            pos_17 = exists(template_17) #查找控件

            if pos_17 is not None:
                #切换至模型评估页面
                touch(pos_17)
            else:
                # 没有找到模板图片
                print("模型评估页面切换失败")

            #判断是否评估完成
            template_18 = Template(r".\public\14_导出报告.png", threshold=0.7)
            pos_18 = exists(template_18) #查找控件

            while not exists(template_18):
                #状态还没转到评估中
                sleep(5.0)

            if pos_18 is not None:
                print("评估完成")
                sleep(1.0)
            
            #保存当前方案数据指标
            snapshot(file)

            #点击右侧更多按钮
            template_19 = Template(r".\public\14_右侧更多按钮.png", threshold=0.7)
            pos_19 = exists(template_19) #查找控件

            if pos_19 is not None:
                touch(pos_19)
            else:
                print("右侧更多点击无效")

            sleep(1.0)

            #点击导出模型
            template_20 = Template(r".\public\14_导出模型按钮.png", threshold=0.7)
            pos_20 = exists(template_20) #查找控件

            if pos_20 is not None:
                touch(pos_20)
            else:
                print("导出模型点击无效")

            sleep(1.0)

            #点击选择文件夹按钮
            template_21 = Template(r".\public\14_选择文件夹.png", threshold=0.7)
            pos_21 = exists(template_21) #查找控件

            if pos_21 is not None:
                touch(pos_21)
            else:
                print("选择文件夹点击无效")

            sleep(1.0)

            #选中编辑框
            template_22 = Template(r".\public\14_路径输入框.png", threshold=0.7)
            pos_22 = exists(template_22) #查找控件

            if pos_22 is not None:
                touch(pos_22)
            else:
                print("编辑框无法选中")

            sleep(1.0)

            #输入指定路径
            current_dir = os.getcwd()
            text(current_dir)
            sleep(2.0)

            #点击跳转
            template_23 = Template(r".\public\14_跳转.png", threshold=0.7)
            pos_23 = exists(template_23) #查找控件

            if pos_23 is not None:
                touch(pos_23)
            else:
                print("跳转无法选中")

            sleep(1.0)

            #点击选择文件夹
            touch(choice_file)
            sleep(5.0)

            #点击导出按钮
            template_24 = Template(r".\public\14_导出按钮.png", threshold=0.7)
            pos_24 = exists(template_24) #查找控件

            if pos_24 is not None:
                touch(pos_24)
            else:
                print("导出按钮无法选中")

            sleep(15.0)

            #点击文件按钮
            template_file = Template(r".\public\15_文件按钮.png", threshold=0.7)
            pos_file = exists(template_file) #查找控件

            if pos_file is not None:
                #点击文件按钮
                touch(pos_file)
            else:
                print("文件按钮点击无效")

            sleep(1.0)

            #点击关闭方案
            template_close = Template(r".\public\16_关闭方案.png", threshold=0.7)
            pos_close = exists(template_close) #查找控件

            if pos_close is not None:
                #点击关闭方案按钮
                touch(pos_close)
            else:
                print("关闭方案按钮点击无效")

            sleep(3.0)   

#GPU监控
def get_gpu_utilization():
    nvidia_smi_output = subprocess.check_output(["nvidia-smi", "--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits"]).decode("utf-8")
    utilization = re.findall(r"(\d+),\s+(\d+)", nvidia_smi_output)
    if len(utilization) > 0:
        gpu_util, mem_util = map(int, utilization[0])
        return gpu_util, mem_util
    else:
        return None
