from elements.public_control import control
from elements.public_control import label_control
from common.Base_method import BasePage
from common.Airtest_method import airtest_method 

class mark():
    
    def image_label():
        '''切换至图像标注'''
        airtest_method.touch_button(control.image_label)
        airtest_method.operate_sleep()
  
    def auto_divide():
        '''自动划分'''
        airtest_method.touch_button(control.auto_divide)
        airtest_method.operate_sleep()

    def import_label(file_path):
        '''串联方案导入标注'''
        if not airtest_method.check_exit(control.import_label,'FALSE') :
            assert False,'未找到导入标注按钮'
        else:
            airtest_method.touch_button(control.import_label)
        airtest_method.touch_button(control.choice_file1) 
        airtest_method.input_text(file_path)
        airtest_method.touch_button(control.jump_click)
        airtest_method.touch_button(control.click_area)
        '''全选'''
        airtest_method.key_event("^a")
        airtest_method.touch_button(control.ok_button)
        if not airtest_method.check_exit(control.upload_label,'FALSE') :
            assert False,'找不到导入完成标志'
        else:
            airtest_method.touch_button(control.upload_done)

    def add_label(label_name):
        '''添加特征标签'''
        if not airtest_method.check_exit(label_control.add_characteristic,'FALSE') :
            assert False,'未找到添加特征按钮'
        else:
            airtest_method.touch_button(label_control.add_characteristic)
        airtest_method.touch_button(label_control.name_edit)
        airtest_method.input_text(label_name)
        if not airtest_method.check_exit(label_control.confirm_button,'FALSE') :
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

    def rectangle_marking(start_points,end_points):
        '''矩形标注'''
        if not airtest_method.check_exit(label_control.rectangle_tool,'FALSE') :
            assert False,'未找到矩形工具'
        else:
            airtest_method.key_event('0')    #标注方式一：选中特征标签后进行特征标注
            airtest_method.touch_button(label_control.rectangle_tool)
            BasePage.click_move_to(start_points,end_points)

            airtest_method.key_event('{DOWN}')  #切换至下一张图片
            airtest_method.operate_sleep()
            airtest_method.key_event('0')    #先取消选中特征标签
            BasePage.click_move_to(start_points,end_points)
            airtest_method.touch_button(label_control.select_characteristic)  #标注方式二：先标注再选中标签
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true) 

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
            airtest_method.key_event('3')    #标注方式：选中特征标签后进行特征标注
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
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true) 

    def AI_marking(start_points,end_points,marking_points):
        '''AI标注'''
        if not airtest_method.check_exit(label_control.brush_tool,'FALSE') :
            assert False,'未找到画笔工具'
        else:
            airtest_method.touch_button(label_control.brush_tool)
            if not airtest_method.check_exit(label_control.AI_tool,'FALSE') :
                assert False,'未找到AI标注工具'
            else:
                airtest_method.key_event('{DOWN}')  #切换至下一张图片
                airtest_method.key_event('4')
                airtest_method.touch_button(label_control.AI_tool)
                

        BasePage.click_move_to(start_points,end_points)  #绘制自定义区域
        airtest_method.click_coordinate_point(marking_points)        #鼠标左键正点标注
        if not airtest_method.check_exit(label_control.select_true,'FALSE') :
            assert False,'未找到确认按钮'
        else:
            airtest_method.touch_button(label_control.select_true) 

    def pen_marking(start_points,end_points):
        '''笔形标注'''
        if not airtest_method.check_exit(label_control.brush_tool,'FALSE') :
            assert False,'未找到笔形工具'
        else:
            airtest_method.key_event('5')
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
            airtest_method.touch_button(label_control.auto_marking)
            if not airtest_method.check_exit(label_control.begin_marking,'FALSE') :
                assert False,'未找到开始标注按钮'
            else:
                airtest_method.touch_button(label_control.begin_marking)
                airtest_method.operate_sleep(10)
                if not airtest_method.check_exit(label_control.apply,'FALSE') :
                    assert False,'未找到应用按钮'
                else:
                    airtest_method.touch_button(label_control.apply)

        if not airtest_method.check_exit(label_control.confirm_button,'FALSE') :
            assert False,'未找到确认按钮'
        else:
            airtest_method.touch_button(label_control.confirm_button)

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

    def seq_rectangle_marking(v1,v2,v3):
        '''字符串算法矩形标注'''
        if not airtest_method.check_exit(label_control.rectangle_tool,'FALSE') :
            assert False,'未找到矩形工具'
        else:
            airtest_method.key_event('0')    #标注方式一：选中特征标签后进行特征标注
            airtest_method.touch_button(label_control.rectangle_tool)
            BasePage.click_multiple_points(v1,v2,v3)   #三点确定矩形框和方向
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true)

            airtest_method.key_event('{DOWN}')  #切换至下一张图片
            airtest_method.operate_sleep()
            airtest_method.key_event('0')    #先取消选中特征标签
            BasePage.click_multiple_points(v1,v2,v3)  #三点确定矩形框和方向
            airtest_method.touch_button(label_control.select_characteristic)  #标注方式二：先标注再选中标签
            if not airtest_method.check_exit(label_control.select_true,'FALSE') :
                assert False,'未找到确认按钮'
            else:
                airtest_method.touch_button(label_control.select_true) 

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




        


         
            






    
