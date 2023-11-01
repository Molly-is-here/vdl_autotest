import os

class save_path():
    base_path = os.path.dirname(__file__)
    dataset_path = r"\\10.80.31.43\vimo数据SVNwc\15_VDL_autotest_dataset"      
    smoke_path = r"\\10.80.31.43\vimo数据SVNwc\14.VDL_SDK自动化\VDL_datasets"        #冒烟测试数据集
    project_path = r"D:\ly\VDL_projects"                                            #兼容性测试方案
    pipelines_path = r'C:\Users\user\Desktop\串联测试数据集\串联auto_test'            #串联方案数据集

    #算法类型（适用于单模块方案）
    cls = base_path + "/public/分类算法.png"
    det = base_path + "/public/检测算法.png"
    seg = base_path + "/public/分割算法.png"
    ocr = base_path + "/public/OCR算法.png"
    uad = base_path + "/public/无监督算法.png"
    project_list = [cls,det,ocr,uad,seg]

    '''冒烟测试数据集'''
    cls_dataset = smoke_path + "\分类算法"
    det_dataset = smoke_path + "\检测算法"
    seg_dataset = smoke_path + "\分割算法"
    ocr_dataset = smoke_path + "\OCR算法"
    uad_dataset = smoke_path + "\无监督算法"

    '''兼容性测试方案'''
    cls_project = project_path + "\分类算法"
    det_project = project_path + "\检测算法"
    seg_project = project_path + "\分割算法"
    ocr_project = project_path + "\OCR算法"
    uad_project = project_path + "\无监督算法"

    '''串联pipelines数据集'''
    cls_seg = pipelines_path + "\分类-分割"
    cls_det = pipelines_path + "\分类-检测"
    cls_uad = pipelines_path + "\分类-无监督"
    det_OCR = pipelines_path + "\检测-OCR"
    det_seg = pipelines_path + "\检测-分割"
    det_uad = pipelines_path + "\检测-无监督"
    seg_OCR = pipelines_path + "\分割-OCR"
    seg_det = pipelines_path + "\分割-检测"
    seg_uad = pipelines_path + "\分割-无监督"

