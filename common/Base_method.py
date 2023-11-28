import os
import shutil
# from pymouse import PyMouse
from common.handle_log import do_log
from common.Airtest_method import airtest_method

class search_file():
    def get_file(file_path):
        
        '''遍历文件夹'''
        files = []
        for file in os.listdir(file_path):  
            files.append(file)    
        return files   
   
    def check_exists(path):
        if os.path.exists(path):
         shutil.rmtree(path)
        else:
            print('目标文件夹不存在')
   
    def copy_files(oldpath, newpath):
        '''复制文件和文件夹'''
        if os.path.exists(oldpath):
            if os.path.exists(newpath):
                if os.path.isfile(oldpath):
                    shutil.copy2(oldpath, newpath)
                else:
                    for file in search_file.get_file(oldpath):
                        shutil.copy2(file, newpath)
            else:
                print('目标文件夹不存在')
        else:
            print('源文件不存在')

class BasePage():
    # def __init__(self) -> None:
    #     self.mouse = PyMouse()

    # def click_pymouse(self, x, y, button=1, n=1):
    #     '''原生鼠标点击'''
    #     # button: 1为左击，2为右击
    #     # n:为点击次数
    #     try:
    #         time.sleep(0.5)
    #         self.mouse.move(x, y)
    #         time.sleep(0.5)
    #         self.mouse.click(x, y, button=button, n=n)
    #         time.sleep(0.5)
    #         do_log.info(f"鼠标在坐标{x, y}处点击成功")
    #     except Exception as err:
    #         do_log.error(f"鼠标在坐标{x, y}处点击失败：{err}")
    #     else:
    #         return self
    #     self.mouse.click(x, y)  # 移动并且在xy位置点击

    def click_move_to(start_points,end_points):
        """鼠标左键分别点击起点和终点"""
        try:
            airtest_method.click_coordinate_point(start_points)
            airtest_method.click_coordinate_point(end_points)
            do_log.info("从 ({}, {}) 移动到 ({}, {})".format(start_points,end_points))
            return True
        except Exception as e:
            do_log.error(f"从 ({start_points}) 移动到 ({end_points}) 失败: {e}")
            return False
      
    def click_multiple_points(V1,V2=None,V3=None,V4=None):
        """点击多个坐标点"""
        try:
            points_list = [V1,V2,V3,V4]
            for points in points_list:
                if points != None:
                    airtest_method.click_coordinate_point(points)
            return True
        except Exception as e:
            do_log.error(f"多个坐标点绘制失败: {e}")
            return False
          
    def click_hold_and_move_to(start_points,end_points):
        '''鼠标左键从起点移动到终点'''
        try:
            airtest_method.move_to(start_points,end_points) 
            do_log.info("从 ({}, {}) 移动到 ({}, {})".format(start_points,end_points))
        except Exception as e:
            do_log.error(f"多个坐标点绘制失败: {e}")
            return False
   
if __name__ == "__main__":
    file_name =  r"\\10.80.31.43\vimo数据SVNwc\10.ViMo DL测试数据\autotest_dataset\ocr算法"
    files = search_file.get_file(file_name)
    print(files)
              

    