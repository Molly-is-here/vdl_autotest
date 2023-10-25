import os

class search_file():
     #遍历文件夹
     def get_file(self, file_path):
          files = []
          for file in os.listdir(file_path):  
             files.append(file)    
          return files   
          
   
if __name__ == "__main__":
    file_name =  r"\\10.80.31.43\vimo数据SVNwc\10.ViMo DL测试数据\autotest_dataset\ocr算法"
    files = search_file.get_file(file_name)
    print(files)
              

    