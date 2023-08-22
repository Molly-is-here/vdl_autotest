# -*- encoding=utf8 -*-
__author__ = "yunliu"

from airtest.core.api import *
from airtest.core.api import start_app
from pywinauto import Application
import function
import random
import time
import gc
auto_setup(__file__)

#选择模型类型（四类算法）
cls = r".\public\分类算法.png"
det = r".\public\检测算法.png"
seg = r".\public\分割算法.png"
ocr = r".\public\OCR算法.png"
#project_list = [cls,det,seg,ocr]
project_list = [seg]


for item in project_list:
    function.get_params(item)
    if item == seg:
         function.algorithm_template(seg)
    if item == cls:
         function.algorithm_template(cls)
    if item == det:
         function.algorithm_template(det)
    if item == ocr:
         function.algorithm_template(ocr)
    else:
         break





