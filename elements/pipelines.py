from airtest.core.api import *
from elements.elements_path import save_path
from elements.public_control import control

class cls_seg():
    file_path = save_path.cls_seg
    pre_module = control.cls_module
    post_module = control.seg_module
    name = '分类-分割'

class cls_det():
    file_path = save_path.cls_det
    pre_module = control.cls_module
    post_module = control.det_module
    name = '分类-检测'

class cls_uad():
    file_path = save_path.cls_uad
    pre_module = control.cls_module
    post_module = control.uad_module
    name = '分类-无监督'

class cls_seq():
    file_path = save_path.cls_seq
    pre_module = control.cls_module
    post_module = control.seq_module
    name = '分类-字符串'

class det_OCR():
    file_path = save_path.det_OCR
    pre_module = control.det_module
    post_module = control.OCR_module
    name = '检测-OCR'

class det_seg():
    file_path = save_path.det_seg
    pre_module = control.det_module
    post_module = control.seg_module
    name = '检测-分割'

class det_uad():
    file_path = save_path.det_uad
    pre_module = control.det_module
    post_module = control.uad_module
    name = '检测-无监督'

class seg_OCR():
    file_path = save_path.seg_OCR
    pre_module = control.seg_module
    post_module = control.OCR_module
    name = '分割-OCR'

class seg_det():
    file_path = save_path.seg_det
    pre_module = control.seg_module
    post_module = control.det_module
    name = '分割-检测'

class seg_uad():
    file_path = save_path.seg_uad
    pre_module = control.seg_module
    post_module = control.uad_module
    name = '分割-无监督'

class seg_seg():
    file_path = save_path.seg_seg
    pre_module = control.seg_module
    post_module = control.seg_module
    name = '分割-分割'

class seg_seq():
    file_path = save_path.seg_seq
    pre_module = control.seg_module
    post_module = control.seq_module
    name = '分割-字符串'

class seq_uad():
    file_path = save_path.seq_uad
    pre_module = control.seq_module
    post_module = control.uad_module
    name = '字符串-无监督'

class seq_cls():
    file_path = save_path.seq_cls
    pre_module = control.seq_module
    post_module = control.cls_module
    name = '字符串-分类'

class seq_ocr():
    file_path = save_path.seq_ocr
    pre_module = control.seq_module
    post_module = control.OCR_module
    name = '字符串-OCR'

class ocr_cls():
    file_path = save_path.ocr_cls
    pre_module = control.OCR_module
    post_module = control.cls_module
    name = 'OCR-分类'

class ocr_uad():
    file_path = save_path.ocr_uad
    pre_module = control.OCR_module
    post_module = control.uad_module
    name = 'OCR-无监督'

class uad_seg():
    file_path = save_path.uad_seg
    pre_module = control.uad_module
    post_module = control.seg_module
    name = '无监督-分割'











