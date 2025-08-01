'''封装AirTest基本方法'''
import airtest.core.api as api
from airtest.core.win import *
from pywinauto.mouse import *


class airtest_method:
    def start_app(app_path):
        '''启动应用程序'''
        api.start_app(app_path)

    def connect_app(url):
        '''连接应用'''
        api.connect_device(url)

    def touch_button(pos,times=1):
        '''点击按钮'''
        api.touch(pos,times)

    def click_coordinate_point(points,times=1):
        '''点击坐标点'''
        api.touch(points,times)
        api.sleep(1.0)

    def input_text(content):
        '''输入文本'''
        api.text(content)

    def check_exit(element,msg = "",timeout = 60):
        '''循环查找元素''' 
        start_time = time.time()
        while not api.exists(element):
            if time.time() - start_time > timeout:
                print(msg)  
                return False        
        return True
    
    def check_exit_timeout(element,msg = "",timeout = 60):
        '''循环查找元素是否消失
        element: 要检查的元素
        msg: 超时时的提示信息
        timeout: 超时时间（秒）
        return: True - 元素消失，False - 元素一直存在
        ''' 
        start_time = time.time()
        while True:
            if not api.exists(element):
                return True  # 元素消失，立即返回True
            if time.time() - start_time > timeout:
                print(msg)  
                return False  # 超时且元素一直存在，返回False
            time.sleep(0.5)  # 避免过于频繁的检查
        
    def screenshot(msg=""):
        '''屏幕截图'''
        api.snapshot(msg)        
        
    def operate_sleep(time = 1.0):
        api.sleep(time)

    def wait_unit(condition,timeout = 10,interval = 0.5,timeout_msg=None):
        '''等待控件出现'''
        api.wait(condition,timeout,interval,timeout_msg)

    def assert_method(element, msg=""):
        '''断言'''
        try:           
            pos = api.loop_find(element, timeout=api.ST.FIND_TIMEOUT, threshold=api.ST.THRESHOLD_STRICT or element.threshold,interval = 1)
            return pos
        except api.TargetNotFoundError:
            raise AssertionError(msg)
        
    def key_event(key):
        '''按键输入'''
        api.keyevent(key)

    def right_click(coords=(0,0)):
        '''右键'''
        right_click(coords)

    def double_click(pos):
        '''双击'''
        api.double_click(pos)

    def move_to(start_points,end_points):
        '''使用坐标的方式进行滑动'''
        api.swipe(start_points,end_points)
        
    def hover(points):
        '''根据坐标点hover'''
        api.sleep(1.0)
        move(points)
        api.sleep(2.0)



    
            
        
            




    
