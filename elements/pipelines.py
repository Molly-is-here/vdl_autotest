from airtest.core.api import *
from elements.elements_path import save_path
from elements.public_control import light_control

class cls_seg():
    file_path = save_path.cls_seg
    pre_module = light_control.cls_module
    post_module = light_control.seg_module
    name = '分类-分割'

class cls_det():
    file_path = save_path.cls_det
    pre_module = light_control.cls_module
    post_module = light_control.det_module
    name = '分类-检测'

class cls_uad():
    file_path = save_path.cls_uad
    pre_module = light_control.cls_module
    post_module = light_control.uad_module
    name = '分类-无监督'

class cls_seq():
    file_path = save_path.cls_seq
    pre_module = light_control.cls_module
    post_module = light_control.seq_module
    name = '分类-字符串'

class det_OCR():
    file_path = save_path.det_OCR
    pre_module = light_control.det_module
    post_module = light_control.OCR_module
    name = '检测-OCR'

class det_seg():
    file_path = save_path.det_seg
    pre_module = light_control.det_module
    post_module = light_control.seg_module
    name = '检测-分割'

class det_uad():
    file_path = save_path.det_uad
    pre_module = light_control.det_module
    post_module = light_control.uad_module
    name = '检测-无监督'

class seg_OCR():
    file_path = save_path.seg_OCR
    pre_module = light_control.seg_module
    post_module = light_control.OCR_module
    name = '分割-OCR'

class seg_det():
    file_path = save_path.seg_det
    pre_module = light_control.seg_module
    post_module = light_control.det_module
    name = '分割-检测'

class seg_uad():
    file_path = save_path.seg_uad
    pre_module = light_control.seg_module
    post_module = light_control.uad_module
    name = '分割-无监督'

class seg_seg():
    file_path = save_path.seg_seg
    pre_module = light_control.seg_module
    post_module = light_control.seg_module
    name = '分割-分割'

class seg_seq():
    file_path = save_path.seg_seq
    pre_module = light_control.seg_module
    post_module = light_control.seq_module
    name = '分割-字符串'

class seq_uad():
    file_path = save_path.seq_uad
    pre_module = light_control.seq_module
    post_module = light_control.uad_module
    name = '字符串-无监督'

class seq_seg():
    file_path = save_path.seq_seg
    pre_module = light_control.seq_module
    post_module = light_control.seg_module
    name = '字符串-分割'

class seq_ocr():
    file_path = save_path.seq_ocr
    pre_module = light_control.seq_module
    post_module = light_control.OCR_module
    name = '字符串-OCR'

class ocr_cls():
    file_path = save_path.ocr_cls
    pre_module = light_control.OCR_module
    post_module = light_control.cls_module
    name = 'OCR-分类'

class ocr_uad():
    file_path = save_path.ocr_uad
    pre_module = light_control.OCR_module
    post_module = light_control.uad_module
    name = 'OCR-无监督'

class uad_seg1():
    file_path = save_path.uad_seg1
    pre_module = light_control.uad_module
    post_module = light_control.seg_module
    name = '无监督-分割1'

class uad_seg2():
    file_path = save_path.uad_seg2
    pre_module = light_control.uad_module
    post_module = light_control.seg_module
    name = '无监督-分割2'

class uad_det():
    file_path = save_path.uad_det
    pre_module = light_control.uad_module
    post_module = light_control.det_module
    name = '无监督-检测'

class roi_seg():
    file_path = save_path.roi_seg
    pre_module = light_control.roi_module
    post_module = light_control.seg_module
    name = 'ROI-分割'

class roi_uad():
    file_path = save_path.roi_uad
    pre_module = light_control.roi_module
    post_module = light_control.uad_module
    name = 'ROI-无监督'

class roi_OCR():
    file_path = save_path.roi_OCR
    pre_module = light_control.roi_module
    post_module = light_control.OCR_module
    name = 'ROI-OCR'

class rapid_det():
    file_path = save_path.rapid_det
    pre_module = light_control.rapid_module
    post_module = light_control.det_module
    points = [(643,591),(745,541),(809,662)]
    number = '8'
    name = '快速定位-检测'

class rapid_seg():
    file_path = save_path.rapid_seg
    pre_module = light_control.rapid_module
    post_module = light_control.seg_module
    points = [(746,370),(1147,370),(1147,763)]
    number = '1'
    name = '快速定位-分割'













