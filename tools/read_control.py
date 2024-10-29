import pandas as pd
from elements.public_control import get_button_from_string

# 读取CSV文件
file_path = r"D:\ly\VDL_autotest\VDL_autotest\tools\控件.csv"  
data = pd.read_csv(file_path, encoding='gbk')

def read_control(element):
    '''按列读取元素'''
    result = data[data['控件名称'] == f'{element}']

    if not result.empty:
        theme = []
        light_theme_str = result['浅色模式'].values[0]
        dark_theme_str = result['深色模式'].values[0]
        print(f'浅色模式: {light_theme_str}, 深色模式: {dark_theme_str}')
        
        theme.append(light_theme_str)
        theme.append(dark_theme_str)  
    else:
        print('未找到该控件名称')
        return []  # 返回空列表以表示未找到

    return theme

def get_button_name(control,color):
    '''映射控件名称
    0 浅色
    1 深色
    '''
    theme = read_control(control)
    element = get_button_from_string(theme[color])
    return element


if __name__ == "__main__":
    theme = get_button_name('新建方案',1)