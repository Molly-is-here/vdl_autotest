'''封装AirTest基本方法'''
# from airtest.core.api import * 
import airtest.core.api as api
from pywinauto.mouse import *


class airtest_method:
    def start_app(self, app_path):
        '''启动应用程序'''
        api.start_app(app_path)

    def connect_app(self, url):
        '''连接应用'''
        api.connect_device(url)

    def touch_button(self, pos,times=1):
        '''点击按钮'''
        api.touch(pos,times)

    def input_text(self, content):
        '''输入文本'''
        api.text(content)

    def check_exit(self, element, msg = "", timeout = 60):
        '''循环查找元素''' 
        start_time = time.time()
        while not api.exists(element):
            if time.time() - start_time > timeout:
                print(f"{msg} not found")  
                return False        
        return True
        
    def screenshot(self, msg=""):
        '''屏幕截图'''
        api.snapshot(msg)        
        
    def operate_sleep(self, time = 1.0):
        api.sleep(time)

    def wait_unit(self, condition,timeout = 10,interval = 0.5,timeout_msg=None):
        '''等待控件出现'''
        api.wait(condition,timeout,interval,timeout_msg)

    def assert_method(self, element, msg=""):
        '''断言'''
        try:           
            pos = api.loop_find(element, timeout=api.ST.FIND_TIMEOUT, threshold=api.ST.THRESHOLD_STRICT or element.threshold,interval = 1)
            return pos
        except api.TargetNotFoundError:
            raise AssertionError(msg)
        
    def key_event(self, key):
        '''按键输入'''
        api.keyevent(key)

    def right_click(self, coords=(0,0)):
        '''右键'''
        right_click(self, coords)

    def double_click(self, pos):
        '''双击'''
        # touch(pos)
        # time.sleep(0.01)
        # touch(pos)
        api.double_click(pos)

    
            
        
            




    
