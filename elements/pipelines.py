from airtest.core.api import *
from elements.elements_path import save_path
from elements.public_control import control

class cls_seg():
    file_path = save_path.cls_seg
    pre_module = control.cls_module
    post_module = control.seg_module

class cls_det():
    file_path = save_path.cls_det
    pre_module = control.cls_module
    post_module = control.det_module

class cls_uad():
    file_path = save_path.cls_uad
    pre_module = control.cls_module
    post_module = control.uad_module

class det_OCR():
    file_path = save_path.det_OCR
    pre_module = control.det_module
    post_module = control.OCR_module

class det_seg():
    file_path = save_path.det_seg
    pre_module = control.det_module
    post_module = control.seg_module

class det_uad():
    file_path = save_path.det_uad
    pre_module = control.det_module
    post_module = control.uad_module

class seg_OCR():
    file_path = save_path.seg_OCR
    pre_module = control.seg_module
    post_module = control.OCR_module

class seg_det():
    file_path = save_path.seg_det
    pre_module = control.seg_module
    post_module = control.det_module

class seg_uad():
    file_path = save_path.seg_uad
    pre_module = control.seg_module
    post_module = control.uad_module

