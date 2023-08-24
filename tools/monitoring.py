import subprocess
import re
import time
import csv
import pynvml
import datetime
import psutil
import os
import pandas as pd
import statistics
from common.Airtest_method import airtest_method 
from PIL import Image
from tools.ocr_identify import ocr_organize

def get_training_utilization(name,status,event):
    pynvml.nvmlInit()
    #handle = pynvml.nvmlDeviceGetHandleByIndex(0)

    header = ['Time', 'GPU利用率/%', '显存使用量/Mib','CPU利用率/%','内存使用量/MB','磁盘使用量/GB']  #设置表头

    file_name = name + '.csv'      
    with open(file_name, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)#将表头写入表格
        '''磁盘使用情况'''              
        partition = "D:\\"  #磁盘分区的挂载点路径
        init_disk_used = psutil.disk_usage(partition).used / (1024 * 1024 * 1024)
        print(f'磁盘已使用：{init_disk_used:.2f} GB')
    if status[0] == 0:
        while True:
            #调用英伟达命令行
            nvidia_smi_output = subprocess.check_output(["nvidia-smi","--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits"]).decode("utf-8")
            utilization = re.findall(r"(\d+),\s+(\d+)", nvidia_smi_output)

            if len(utilization) > 0:
                gpu_util, mem_util = map(int, utilization[0]) #GPU利用率和显存使用量
                
                '''获取磁盘使用情况'''
                disk_used = psutil.disk_usage(partition).used / (1024 * 1024 * 1024)
                lated_disk_used = disk_used - init_disk_used
                print(f'磁盘使用量为：{lated_disk_used:.2f} GB')

                '''根据进程号获取CPU使用情况'''
                cpu_sum = 0
                men_cum = 0
                plist = ['VDL.exe','python.exe','QtWebEngineProcess.exe']
                #print('cpu核数：',psutil.cpu_count())

                for proc in psutil.process_iter(['name']):
                    if proc.info['name'] in plist:
                        pid = proc.pid
                        print(proc.info['name'] ,"的进程号是：", pid)
                        process_cpu_usage = proc.cpu_percent()/psutil.cpu_count()
                        process_mem_usage = proc.memory_info().rss / (1024*1024)
                        cpu_sum += process_cpu_usage
                        men_cum += process_mem_usage
                        
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")#获取当前时间
               
                with open(file_name, 'a', newline='') as f:
                    writer = csv.writer(f)
                    if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'SEG': 
                        if gpu_util > 20: #设置阈值，如果GPU利用率大于20才能够写入数据ffffffff
                            writer.writerow([current_time, gpu_util, mem_util,round(cpu_sum,2),round(men_cum,2),round(lated_disk_used,2)])
                    else:
                        writer.writerow([current_time, gpu_util, mem_util,round(cpu_sum,2),round(men_cum,2),round(lated_disk_used,2)])
                    time.sleep(1)
                if status[0] == 1:                       
                    break
    event.set() 

    '''统计表格数据'''
    with open(file_name,'r',newline='', errors='replace') as read_f:
        read_file = pd.read_csv(read_f)
        columns = ['GPU利用率/%', '显存使用量/Mib','CPU利用率/%','内存使用量/MB','磁盘使用量/GB']
        for column in columns:
            column_total = {}
            if column not in read_file.columns:
                print(f"Column '{column}' not found in the CSV file.")
                continue

            max_value = read_file[column].max()
            min_value = read_file[column].min()
            avg_value = read_file[column].mean()
            van_value = statistics.variance(read_file[column])
            range_value = max_value - min_value           

            '''将统计信息添加到结果字典中'''
            column_total[column] = {
                    'max': max_value,
                    'min': min_value,
                    'avg': round(avg_value,2),
                    'van': round(van_value,2),
                    'ran' :round(range_value,2)
                }
           
            '''写入统计数据'''
            with open(file_name, 'a', newline='') as write_f:
                writer_file = csv.writer(write_f)
                writer_file.writerow([column_total])

def get_infer_utilization(name,status,event,path):
    pynvml.nvmlInit()
    current_dir = os.getcwd()

    header = ['Time', 'GPU利用率/%', '显存使用量/Mib','CPU利用率/%','内存使用量/MB','磁盘使用量/GB']  #设置表头

    file_name = name + '.csv'      
    with open(file_name, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)#将表头写入表格
        '''磁盘使用情况'''              
        partition = "D:\\"  #磁盘分区的挂载点路径
        init_disk_used = psutil.disk_usage(partition).used / (1024 * 1024 * 1024)
        print(f'磁盘已使用：{init_disk_used:.2f} GB')
    if status[0] == 0:
        while True:
            #调用英伟达命令行
            nvidia_smi_output = subprocess.check_output(["nvidia-smi","--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits"]).decode("utf-8")
            utilization = re.findall(r"(\d+),\s+(\d+)", nvidia_smi_output)

            if len(utilization) > 0:
                gpu_util, mem_util = map(int, utilization[0]) #GPU利用率和显存使用量
                
                '''获取磁盘使用情况'''
                disk_used = psutil.disk_usage(partition).used / (1024 * 1024 * 1024)
                lated_disk_used = disk_used - init_disk_used
                print(f'磁盘使用量为：{lated_disk_used:.2f} GB')

                '''根据进程号获取CPU使用情况'''
                cpu_sum = 0
                men_cum = 0
                plist = ['VDL.exe','python.exe','QtWebEngineProcess.exe']
                #print('cpu核数：',psutil.cpu_count())

                for proc in psutil.process_iter(['name']):
                    if proc.info['name'] in plist:
                        pid = proc.pid
                        print(proc.info['name'] ,"的进程号是：", pid)
                        process_cpu_usage = proc.cpu_percent()/psutil.cpu_count()
                        process_mem_usage = proc.memory_info().rss / (1024*1024)
                        cpu_sum += process_cpu_usage
                        men_cum += process_mem_usage
                        
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")#获取当前时间
               
                with open(file_name, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([current_time, gpu_util, mem_util,round(cpu_sum,2),round(men_cum,2),round(lated_disk_used,2)])
                    time.sleep(1)
                if status[0] == 1:                       
                    break
    event.set() 

    '''统计表格数据'''
    with open(file_name,'r',newline='', errors='replace') as read_f:
        read_file = pd.read_csv(read_f)
        columns = ['GPU利用率/%', '显存使用量/Mib','CPU利用率/%','内存使用量/MB','磁盘使用量/GB']
        for column in columns:
            column_total = {}
            if column not in read_file.columns:
                print(f"Column '{column}' not found in the CSV file.")
                continue
           
            max_value = read_file[column].max()
            min_value = read_file[column].min()
            avg_value = read_file[column].mean()
            van_value = statistics.variance(read_file[column])
            range_value = max_value - min_value                      

            '''将统计信息添加到结果字典中'''
            column_total[column] = {
                    'max': max_value,
                    'min': min_value,
                    'avg': round(avg_value,2),
                    'van': round(van_value,2),
                    'ran' :round(range_value,2)
                }
            
            '''写入统计数据'''
            with open(file_name, 'a', newline='') as write_f:
                writer_file = csv.writer(write_f)
                writer_file.writerow([column_total])
            
    static_path = os.path.join(path, 'static')
    project_name = f"{name}"
    detail_screenshot = os.path.join(static_path, f"{project_name}.png")
    min_time = os.path.join(static_path, f"{project_name}_min.png")
    max_time = os.path.join(static_path, f"{project_name}_max.png")
    avg_time = os.path.join(static_path, f"{project_name}_avg.png")

    airtest_method.screenshot(detail_screenshot)   #全屏截图
    detail_image =  os.path.join(path,detail_screenshot)  #指定路径
    region_image = Image.open(detail_image)

    min_time_screenshot = region_image.crop((1440,428,1580,515)) #最小值截图
    min_time_screenshot.save(min_time)

    max_time_screenshot = region_image.crop((1600,428,1740,515)) #最大值截图
    max_time_screenshot.save(max_time)

    avg_time_screenshot = region_image.crop((1760,428,1900,515)) #平均值截图
    avg_time_screenshot.save(avg_time)

    ocr_character = [min_time,max_time,avg_time]
    ocr_content = ocr_organize(ocr_character)    
    # data = [int(ocr_content[0]),int(ocr_content[1])]
    # van_time = statistics.variance(data)
    # range_time = ocr_content[1] - ocr_content[0]      
        
    '''将ct时间记录至表格'''
    content = {}
    content = {
        'min:' :ocr_content[0],
        'max:' :ocr_content[1],
        'avg:' :ocr_content[2],
        # 'van:' :van_time,
        # 'range:' : range_time
    }
    with open(file_name, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([content])
 
if __name__ == "__main__":
    get_infer_utilization()
        
    
