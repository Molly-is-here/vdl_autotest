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

def get_utilization(name,status,event):
    pynvml.nvmlInit()
    #handle = pynvml.nvmlDeviceGetHandleByIndex(0)
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
                    if name == 'CLS' or name == 'DET' or name == 'OCR' or name == 'SEG': 
                        if gpu_util > 20: #设置阈值，如果GPU利用率大于20才能够写入数据
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
 
if __name__ == "__main__":
    get_utilization('123',0,0)
        
    
