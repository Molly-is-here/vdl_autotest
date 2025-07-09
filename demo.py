from VDL_autotest.tools.ocr import *
import pandas as pd
import os
from pages.open_sofrware import open_Software
from common.Airtest_method import airtest_method
from common.handle_log import do_log

def process_excel_file(excel_path):
    """处理Excel文件，进行OCR识别和文本对比
    
    该函数主要完成以下工作：
    1. 读取Excel文件
    2. 验证必要的列是否存在
    3. 清理结果列的数据
    4. 对每一行进行OCR识别和文本对比
    5. 记录识别结果和匹配状态
    6. 保存处理结果到原文件
    
    Args:
        excel_path (str): Excel文件路径
        
    Returns:
        None: 处理结果会直接写入原Excel文件
    """
    try:
        # 1. 读取Excel文件
        df = pd.read_excel(excel_path)
        do_log.info(f"成功读取Excel文件")
        do_log.info(f"Excel文件的列名: {df.columns.tolist()}")
        
        # 2. 检查是否包含所有必要的列
        required_columns = ['fix-japanese', '坐标', 'click','hover','是否匹配']
        for col in required_columns:
            if col not in df.columns:
                do_log.error(f"Excel文件缺少必要的列: {col}")
                do_log.error(f"当前Excel文件的列名: {df.columns.tolist()}")
                raise ValueError(f"Excel文件缺少必要的列: {col}")
        
        # 3. 清空"是否匹配"和"实际结果"列，保证每次运行都是新结果
        df['是否匹配'] = ''
        if '实际结果' not in df.columns:
            df['实际结果'] = ''
        else:
            df['实际结果'] = ''
        
        do_log.info("已清理'是否匹配'和'实际结果'列的数据")
        
        # 4. 遍历每一行，逐行处理
        for index, row in df.iterrows():
            # 获取目标文本（日文）
            target_text = str(row['fix-japanese']).strip()
            
            # 解析坐标
            coords_text = str(row['坐标']).strip()
            try:
                # 去除括号和引号，分割为4个整数
                coords_text = coords_text.replace('(', '').replace(')', '').replace("'", '')
                x1, y1, x2, y2 = map(int, coords_text.split(','))
                region = (x1, y1, x2, y2)
            except:
                do_log.error(f"第{index+1}行的坐标格式错误: {coords_text}")
                df.at[index, '是否匹配'] = 'FALSE'
                df.at[index, '实际结果'] = '坐标格式错误'
                continue
            
            try:
                # 处理悬停操作（如果有）
                hover_coords = str(row['hover']).strip()
                if hover_coords and hover_coords != '0' and hover_coords != '':
                    try:
                        # 去除引号并分割为坐标
                        hover_coords = hover_coords.replace("'", '')
                        x, y = map(int, hover_coords.split(','))
                        do_log.info(f"第{index+1}行悬停坐标点: ({x}, {y})")
                        airtest_method.hover((x, y))
                    except Exception as e:
                        do_log.warning(f"第{index+1}行悬停操作失败，继续执行: {str(e)}")
                
                # 进行OCR识别，优先用日文，失败则用英文
                results = ocr_region(region, lang="japan")
                if results is None or not results:
                    do_log.info(f"第{index+1}行日文识别结果为空，尝试英文识别")
                    results = ocr_region(region, lang="en")
                    if results is None or not results:
                        do_log.error(f"第{index+1}行OCR识别结果为空")
                        df.at[index, '是否匹配'] = 'FALSE'
                        df.at[index, '实际结果'] = '识别结果为空'
                        continue
                # 获取识别到的文本
                recognized_text = results[0]['text'].strip()
                do_log.info(f"第{index+1}行识别结果: {recognized_text}")
                
                # 5. 对比识别结果和目标文本
                is_match = recognized_text == target_text
                df.at[index, '是否匹配'] = 'TRUE' if is_match else 'FALSE'
                if not is_match:
                    df.at[index, '实际结果'] = recognized_text
                
                # 6. 处理点击操作（如果有）
                click_coords = str(row['click']).strip()
                if click_coords and click_coords != '0' and click_coords != '':
                    try:
                        # 去除引号并分割为坐标
                        click_coords = click_coords.replace("'", '')
                        x, y = map(int, click_coords.split(','))
                        do_log.info(f"第{index+1}行点击坐标点: ({x}, {y})")
                        airtest_method.right_click((x, y))
                        airtest_method.click_coordinate_point((x, y))
                    except Exception as e:
                        do_log.warning(f"第{index+1}行点击操作失败，继续执行: {str(e)}")
            except Exception as e:
                do_log.error(f"第{index+1}行处理失败: {str(e)}")
                df.at[index, '是否匹配'] = 'FALSE'
                df.at[index, '实际结果'] = f'处理失败: {str(e)}'
        # 7. 保存处理结果到原Excel文件
        df.to_excel(excel_path, index=False)
        do_log.info("处理完成，结果已保存到Excel文件")
    except Exception as e:
        do_log.error(f"处理Excel文件时发生错误: {str(e)}")

if __name__ == "__main__":
    open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")

    # 设置Excel文件路径
    excel_path = R"C:\Users\user\Desktop\日文识别\综合判定页面.xlsx"
    
    # 检查文件是否存在
    if not os.path.exists(excel_path):
        do_log.error(f"Excel文件不存在: {excel_path}")
    else:
        process_excel_file(excel_path)


