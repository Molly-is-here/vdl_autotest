from PIL import Image
import os
from pages.open_sofrware import open_Software
from elements.elements_path import *
from tools.docqq import *

'''生成HTML文件'''
def create_html_file(version,name,images,write_header=True):
    html_code = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>版本对比记录</title>
    <style>
    table {
      width: 100%;
      border-collapse: collapse;
    }
    
    table,th,td {
      border: 1px solid black;
    }
    
    td {
      padding: 8px;
      text-align: center;
    }
    
    th {
      padding: 8px;
      background-color: #9cc25b;
    }
    </style>
    </head>
    <body>
    '''
    if write_header:
        html_code += '''
        <table>
            <thead>
            <tr>
            <th style="width:100px;">软件版本</th>
            <th style="width:100px;">算法类型</th>
            <th style="width:100px;">指标记录</th>
            </tr>
            </thead>
        </table>
        '''
    html_content = f'''
    <table>
        <tbody>
        <tr>
        <td style="width:100px;">{version}</td>
        <td style="width:100px;">{name}</td> 
        <td style="width:100px;"><a href="{images}" target="_blank">查看详情</a></td> 
        </tr>
        </tbody>
    </table>
    
    </body>
    </html>
    '''
    html_name = save_path.base_path + '\\' + 'static' + '\\' + version + '评估指标.html'
    # html_name = r"D:\ly\VDL_autotest\VDL_autotest\elements\static\V0.9.0评估指标.html"
    if not os.path.exists(html_name):
        with open(html_name, 'a') as output_file:
            output_file.write(html_code)
            output_file.write(html_content)
    else:
        with open(html_name, 'r+') as output_file:
            output_file.seek(0, os.SEEK_END)
            output_file.write(html_content)# 

    content = ["",version,name]
    run("https://docs.qq.com/sheet/DY2ZHWnFlQXplWUFv?tab=BB08J2",content)
    open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")



# 调用函数示例
# i = 0
# while i < 2:
#   i+=1
#   create_html_file("0.9.0","分类算法",r"D:\ly\VDL_autotest\VDL_autotest\elements\分类算法评估完成.png")