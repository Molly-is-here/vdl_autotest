from elements.public_control import label_control
from common.Base_method import BasePage
from common.Airtest_method import airtest_method 
from elements.public_control import light_control,get_button_from_string

class mark():
    
    def image_label(color):
        '''切换至图像标注页面
        color light:浅色主题 dark:深色主题
        '''
        image_label_element = get_button_from_string(f"{color}_control.image_label")
        if not airtest_method.check_exit(image_label_element,'FALSE',5) :
            assert False,'找不到图像标注tab按钮'
        else:
            airtest_method.touch_button(image_label_element)
        airtest_method.operate_sleep()
  
    def auto_divide(color):
        '''自动划分
        color light:浅色主题 dark:深色主题
        '''
        auto_divide_element = get_button_from_string(f"{color}_control.auto_divide")
        train_ratio_element = get_button_from_string(f"{color}_control.train_ratio")
        train_60_element = get_button_from_string(f"{color}_control.train_60")
        
        airtest_method.touch_button(train_ratio_element) #训练比例
        airtest_method.touch_button(train_60_element) #60%

        if not airtest_method.check_exit(auto_divide_element,'FALSE',10) :
            assert False,'找不到数据划分按钮'
        else:
            airtest_method.touch_button(auto_divide_element)
        airtest_method.operate_sleep()

    def train_set():
        '划分为训练集'
        if not airtest_method.check_exit(light_control.train_set,'FALSE',5) :
            assert False,'找不到划分为训练集按钮'
        else:
            airtest_method.touch_button(light_control.train_set)
        airtest_method.operate_sleep()


    def import_label(file_path,color):
        '''串联方案导入标注
        color light:浅色主题 dark:深色主题
        '''
        #导入标注
        import_label_element = get_button_from_string(f"{color}_control.import_label")
        #导入完成
        upload_done = get_button_from_string(f"{color}_control.upload_done")
        
        if not airtest_method.check_exit(import_label_element,'FALSE') :
            assert False,'未找到导入标注按钮'
        else:
            airtest_method.touch_button(import_label_element)
        if not airtest_method.check_exit(light_control.choice_file,'FALSE') :
            assert False,'未找到导入文件夹按钮'
        else:
            airtest_method.touch_button(light_control.choice_file) 
        airtest_method.input_text(file_path)
        airtest_method.key_event("{ENTER}")
        airtest_method.touch_button(light_control.click_area)
        #全选
        airtest_method.key_event("^a")

        airtest_method.key_event("{ENTER}")
        if not airtest_method.check_exit(upload_done,'FALSE') :
            assert False,'找不到导入完成标志'
        else:
            airtest_method.touch_button(upload_done)

    def add_label(label_name):
        '''添加特征标签'''
        if not airtest_method.check_exit(label_control.add_characteristic,'FALSE') :
            assert False,'未找到添加特征按钮'
        else:
            airtest_method.touch_button(label_control.add_characteristic)
        airtest_method.touch_button(label_control.name_edit)
        airtest_method.input_text(label_name)
        if not airtest_method.check_exit(label_control.confirm_button,'FALSE',5) :
                assert False,'未找到确认按钮'
        else:
            airtest_method.touch_button(label_control.confirm_button)

    def acceptable_sample():
        '''合格样本'''
        if not airtest_method.check_exit(label_control.acceptable_sample_tool,'FALSE') :
            assert False,'未找到合格样本按钮'
        else:
            airtest_method.key_event('{DOWN}')  #切换至下一张图片
            airtest_method.touch_button(label_control.acceptable_sample_tool)  

    def NG_sample():
        '''NG样本'''
        if not airtest_method.check_exit(label_control.NG_sample_tool,'FALSE') :
            assert False,'未找到NG样本按钮'
        else:
            airtest_method.key_event('{DOWN}')  #切换至下一张图片
            airtest_method.touch_button(label_control.NG_sample_tool)  

    def rectangle_marking(start_points,end_points,number):
        '''矩形标注'''
        airtest_method.operate_sleep()
        if not airtest_method.check_exit(label_control.rectangle_tool,'FALSE') :
            assert False,'未找到矩形工具'
        else:
            airtest_method.key_event(number)    #标注方式一：选中特征标签后进行特征标注
            airtest_method.touch_button(label_control.rectangle_tool)
            BasePage.click_move_to(start_points,end_points)

            airtest_method.key_event('{DOWN}')  #切换至下一张图片
            airtest_method.operate_sleep()
            airtest_method.key_event(number)    #先取消选中特征标签
            BasePage.click_move_to(start_points,end_points)
            airtest_method.touch_button(label_control.select_characteristic)  #标注方式二：先标注再选中标签
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true) 

    def auto_rectangle_marking(start_points,end_points):
        '''智能矩形'''
        airtest_method.operate_sleep()
        airtest_method.key_event('{DOWN}')  #切换至下一张图片
        if not airtest_method.check_exit(label_control.rectangle_tool,'FALSE') :
            assert False,'未找到矩形工具'
        else:
            airtest_method.touch_button(label_control.rectangle_tool)
        if not airtest_method.check_exit(label_control.auto_rectangle_tool,'FALSE') :
            assert False,'未找到智能矩形工具'
        else:
            airtest_method.touch_button(label_control.auto_rectangle_tool)
            BasePage.click_move_to(start_points,end_points)

    def ocv_marking(start_points,end_points,number,content):
        '''OCV矩形标注'''
        airtest_method.operate_sleep()
        if not airtest_method.check_exit(label_control.rectangle_tool,'FALSE') :
            assert False,'未找到矩形工具'
        else:
            airtest_method.key_event(number)    
            airtest_method.touch_button(label_control.rectangle_tool)
            BasePage.click_move_to(start_points,end_points)
            airtest_method.operate_sleep(5.0)
            airtest_method.input_text(content)
            airtest_method.key_event('{ENTER}')
            airtest_method.operate_sleep(2.0)
        
    def polygon_marking(v1,v2,v3,v4=None):
        '''多边形标注'''
        if not airtest_method.check_exit(label_control.polygon_tool,'FALSE') :
            assert False,'未找到多边形工具'
        else:
            airtest_method.key_event('1')    #标注方式一：选中特征标签后进行特征标注
            airtest_method.touch_button(label_control.polygon_tool)
            BasePage.click_multiple_points(v1,v2,v3)
            airtest_method.click_coordinate_point(v1)  #三点确认一个多边形

            airtest_method.key_event('{DOWN}')  #切换至下一张图片
            airtest_method.operate_sleep()
            airtest_method.key_event('1')    #先取消选中特征标签
            BasePage.click_multiple_points(v1,v2,v3)
            airtest_method.click_coordinate_point(v1)  #三点确认一个多边形
            airtest_method.touch_button(label_control.select_characteristic)  #标注方式二：先标注再选中标签ignore
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true)  

    def line_marking(start_points,end_points):
        '''线标注'''
        if not airtest_method.check_exit(label_control.line_tool,'FALSE') :
            assert False,'未找到线工具'
        else:
            airtest_method.key_event('2')    #标注方式：选中特征标签后进行特征标注
            airtest_method.touch_button(label_control.line_tool)
            BasePage.click_move_to(start_points,end_points)

    def polyline_marking(v1,v2,v3):
        '''折线标注'''
        if not airtest_method.check_exit(label_control.polyline_tool,'FALSE') :
            assert False,'未找到折线工具'
        else:
            airtest_method.key_event('2')    #标注方式：选中特征标签后进行特征标注
            airtest_method.touch_button(label_control.polyline_tool)
            BasePage.click_move_to(v1,v2)
            airtest_method.double_click(v3) #双击确定标注

    def masking_area(v1,v2,v3,v4=None):
        '''屏蔽区域'''
        if not airtest_method.check_exit(label_control.masking_area,'FALSE') :
            assert False,'未找到屏蔽区域工具'
        else:
            airtest_method.touch_button(label_control.masking_area)
            BasePage.click_multiple_points(v1,v2,v3,)
            airtest_method.click_coordinate_point(v1)  #三点确认一个多边形
            # if not airtest_method.check_exit(label_control.select_true,'FALSE') :
            #     assert False,'未找到确认按钮'
            # else:
            #     airtest_method.touch_button(label_control.select_true) 

    def AI_marking(start_points,end_points,marking_points):
        '''AI标注'''
        if not airtest_method.check_exit(label_control.AI_tool,'FALSE') :
            assert False,'未找到AI标注工具'
        else:         
            airtest_method.key_event('{DOWN}')  #切换至下一张图片
            airtest_method.key_event('3')
            airtest_method.touch_button(label_control.AI_tool)
                

            BasePage.click_move_to(start_points,end_points)  #绘制自定义区域
            airtest_method.click_coordinate_point(marking_points)        #鼠标左键正点标注
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true) 

    def pen_marking(start_points,end_points):
        '''笔形标注'''
        airtest_method.key_event('4')
        airtest_method.touch_button(label_control.brush_tool)
        BasePage.click_hold_and_move_to(start_points,end_points)  #画笔滑动绘制
    
        if not airtest_method.check_exit(label_control.select_true,'FALSE') :
            assert False,'未找到确认按钮'
        else:
            airtest_method.touch_button(label_control.select_true)
         
    def auto_marking():
        '''自动标注'''
        if not airtest_method.check_exit(label_control.auto_marking,'FALSE') :
            assert False,'未找到自动标注工具'
        else:
            airtest_method.key_event('{DOWN}')
            airtest_method.touch_button(label_control.auto_marking)
            if not airtest_method.check_exit(label_control.begin_marking,'FALSE') :
                assert False,'未找到开始标注按钮'
            else:                
                airtest_method.touch_button(label_control.begin_marking)
                airtest_method.operate_sleep(5.0)
                if not airtest_method.check_exit(label_control.apply,'FALSE') :
                    assert False,'未找到应用按钮'
                else:
                    airtest_method.touch_button(label_control.apply)

        if not airtest_method.check_exit(label_control.confirm_button,'FALSE') :
            assert False,'未找到确认按钮'
        else:
            airtest_method.touch_button(label_control.confirm_button)
            airtest_method.operate_sleep()

    def add_marking():
        '''添加标签'''
        if not airtest_method.check_exit(label_control.add_marking,'FALSE') :
            assert False,'未找到标签'
        else:
            airtest_method.touch_button(label_control.add_marking)

        airtest_method.key_event('{DOWN}')  #切换至下一张图片
        if not airtest_method.check_exit(label_control.add_marking,'FALSE') :
                assert False,'未找到标签'
        else:
            airtest_method.touch_button(label_control.add_marking)

    def seq_rectangle_marking(v1,v2,v3,number):
        '''字符串算法矩形标注'''
        if not airtest_method.check_exit(label_control.rectangle_tool,'FALSE') :
            assert False,'未找到矩形工具'
        else:
            airtest_method.key_event(number)    #标注方式一：选中特征标签后进行特征标注
            airtest_method.touch_button(label_control.rectangle_tool)
            BasePage.click_multiple_points(v1,v2,v3)   #三点确定矩形框和方向
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true)

            airtest_method.key_event('{DOWN}')  #切换至下一张图片
            airtest_method.operate_sleep()
            airtest_method.key_event(number)    #先取消选中特征标签
            BasePage.click_multiple_points(v1,v2,v3)  #三点确定矩形框和方向
            airtest_method.touch_button(label_control.select_characteristic)  #标注方式二：先标注再选中标签
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true) 

    def rapid_rectangle_marking(v1,v2,v3):
        '''快速定位矩形标注'''
        if not airtest_method.check_exit(label_control.rapid_rectangle_tool,'FALSE') :
            assert False,'未找到矩形工具'
        else:
            airtest_method.touch_button(label_control.rapid_rectangle_tool)
            BasePage.click_multiple_points(v1,v2,v3)  #三点确定矩形框和方向
            airtest_method.operate_sleep()
            airtest_method.touch_button(light_control.training_okbutton)

    def seq_circle_marking(v1,v2,v3,v4):
        '''字符串算法环形标注'''
        if not airtest_method.check_exit(label_control.circle_tool,'FALSE') :
            assert False,'未找到环形工具'
        else:
            airtest_method.key_event('{DOWN}')  #切换至下一张图片
            airtest_method.key_event('1')    #标注方式：选中特征标签后进行特征标注
            airtest_method.touch_button(label_control.circle_tool)
            BasePage.click_multiple_points(v1,v2,v3,v4)   #四点确定环形框和方向
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true)




        


         
            






    
