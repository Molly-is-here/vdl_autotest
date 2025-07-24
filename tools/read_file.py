import os
import time

def check_train_over(file_path):
    '''检查训练是否结束'''
    start_time = time.time() 
    time_limit = 300 * 60  # 300分钟
    while time.time() - start_time < time_limit:  # 在10分钟内循环检查
        # 检查文件是否存在
        if not os.path.isfile(file_path):
            print(f"文件 {file_path} 不存在！正在等待文件出现...")
            time.sleep(1)  # 等待1秒钟后继续检查
            continue  # 文件不存在，继续等待
        
        # 如果文件存在，尝试打开并读取
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                line = file.readline()  # 读取文件的第一行
                while line:  # 只要文件中有内容
                    if 'train over' in line:
                        print("训练完成")
                        return 0  # 训练完成
                    if 'train failed' in line:
                        print("训练失败")
                        return 1  # 训练失败
                    line = file.readline()  # 继续读取下一行
                # 如果文件结尾未找到关键字，等待并继续
                time.sleep(1)
        except Exception as e:
            print(f"打开文件时发生错误: {str(e)}")
            return False
        
    # 超过时间限制仍未找到关键字
    print(f"等待时间超过限制({time_limit}秒)，训练状态未更新。")
    return False
