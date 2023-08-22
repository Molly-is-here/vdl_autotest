from PIL import Image
import os
from elements.elements_path import *

'''生成HTML文件'''
def create_html_file(name,Accuracy_image,Recall_image,mIOU_image,detail_image,train_count, file,training_spend_time,assess_spend_time,ct_time,write_header=True):
    html_code = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>多模型评估指标记录</title>
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
            <th style="width:100px;">算法类型</th>
            <th style="width:100px;">循环次数</th>
            <th style="width:100px;">项目名称</th>
            <th style="width:100px;">训练时长/s</th>
            <th style="width:100px;">评估时长/s</th>
            <th style="width:100px;">总CT时长/s</th>
            <th style="width:300px;">精确率</th>
            <th style="width:300px;">召回率</th>
            <th style="width:300px;">mIOU</th>
            <th style="width:100px;">查看详情</th>
            </tr>
            </thead>
        </table>
        '''
    html_content = f'''
    <table>
        <tbody>
        <tr>
        <td style="width:100px;">{name}</td>
        <td style="width:100px;">{train_count}</td>
        <td style="width:100px;">{file}</td>
        <td style="width:100px;">{training_spend_time}</td>
        <td style="width:100px;">{assess_spend_time}</td>
        <td style="width:100px;">{ct_time}</td>
        <td style="width:300px;"><img src = "{Accuracy_image}"></td>
        <td style="width:300px;"><img src = "{Recall_image}"></td>
        <td style="width:300px;"><img src = "{mIOU_image} " alt="null"></td>
        <td style="width:100px;"><a href="{detail_image}" target="_blank">点击查看详情</a></td>     
        </tr>
        </tbody>
    </table>
    
    </body>
    </html>
    '''
    html_name = save_path.base_path + '\\' + 'static' + '\\' + file + '.html'
    if not os.path.exists(html_name):
        with open(html_name, 'a') as output_file:
            output_file.write(html_code)
            output_file.write(html_content)
    else:
        with open(html_name, 'r+') as output_file:
            output_file.seek(0, os.SEEK_END)
            output_file.write(html_content)# 

# 调用函数示例
i = 0
while i < 2:
  i+=1
  #create_html_file(r"C:\Users\yunli\Desktop\ly_autotest\VDL_autotest_0625\当前窗口截图.png",i,'testxiangmu1')