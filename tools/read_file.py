import time
def check_train_over(file_path):
    '''检查训练是否结束'''
    start_time = time.time() 
    time_limit = 10 * 60  
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            while time.time() - start_time < time_limit:  # 在10分钟内检查
                line = file.readline()  
                if not line:  # 如果读取到文件结尾，且没有找到任何关键字，则跳出循环
                    time.sleep(1)
                    continue  # 跳过这一轮，继续下一轮检查
                if 'train over' in line:
                    return 0  # 训练完成
                if 'train failed' in line:
                    return 1  # 训练失败

        return False  # 如果10分钟内未找到关键字，返回False
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    

if __name__ == '__main__':
    file_path = r"D:\ViMo-Deeplearning\Example\Detect\output\2\vimo-train.log"
    result = check_train_over(file_path)
    print(result)