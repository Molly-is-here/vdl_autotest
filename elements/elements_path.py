import os

class save_path():
    '''适配浅色主题'''
    base_path = os.path.dirname(__file__)
    dataset_path = r"\\10.80.31.43\vimo数据SVNwc\15_VDL_autotest_dataset"      
    smoke_path = r"\\10.80.31.43\vimo数据SVNwc\14.VDL_SDK自动化\VDL_datasets"        #冒烟测试数据集
    project_path = r"D:\ly\VDL_projects"                                            #兼容性测试方案
    pipelines_path = r'C:\Users\user\Desktop\串联测试数据集\串联auto_test'            #串联方案数据集
    SDK_exe_path =   r"D:\ly\VDL_autotest\VDL_autotest\tools\test_executor_1023_1.exe"   #SDK对齐exe

    #算法类型（适用于单模块方案）
    cls = base_path + "/public/分类算法.png"
    det = base_path + "/public/检测算法.png"
    seg = base_path + "/public/分割算法.png"
    ocr = base_path + "/public/OCR算法.png"
    uad = base_path + "/public/无监督算法.png"
    seqocr = base_path + "/public/字符串算法.png"
    project_list = [cls,uad,ocr,seqocr,det,seg]

    #冒烟测试数据集
    cls_dataset = smoke_path + "\分类算法"
    det_dataset = smoke_path + "\检测算法"
    seg_dataset = smoke_path + "\分割算法"
    ocr_dataset = smoke_path + "\OCR算法"
    uad_dataset = smoke_path + "\无监督算法"
    seqocr_dataset = smoke_path + "\Seqocr算法"

    #算法校验测试方案
    cls_project = project_path + "\分类"
    det_project = project_path + "\检测"
    seg_project = project_path + "\分割"
    ocr_project = project_path + "\OCR"
    uad_project = project_path + "\无监督"
    seqocr_project = project_path + "\字符串"
    compare_project = [cls_project,det_project,seg_project,ocr_project,uad_project,seqocr_project]
    
    #串联pipelines数据集
    cls_seg = pipelines_path + "\分类-分割"
    cls_det = pipelines_path + "\分类-检测"
    cls_uad = pipelines_path + "\分类-无监督"
    cls_seq = pipelines_path + "\分类-字符串"
    det_OCR = pipelines_path + "\检测-OCR"
    det_seg = pipelines_path + "\检测-分割"
    det_uad = pipelines_path + "\检测-无监督"
    seg_OCR = pipelines_path + "\分割-OCR"
    seg_det = pipelines_path + "\分割-检测"
    seg_uad = pipelines_path + "\分割-无监督"
    seg_seg = pipelines_path + "\分割-分割"
    seg_seq = pipelines_path + "\分割-字符串"
    seq_uad = pipelines_path + "\字符串-无监督"
    seq_seg = pipelines_path + "\字符串-分割"
    seq_ocr = pipelines_path + "\字符串-OCR"
    ocr_cls = pipelines_path + "\OCR-分类"
    ocr_uad = pipelines_path + "\OCR-无监督"
    uad_seg1 = pipelines_path + "\无监督-分割1"
    uad_seg2 = pipelines_path + "\无监督-分割2"
    uad_det = pipelines_path + "\无监督-检测"
    roi_seg = pipelines_path + "\\roi-分割"
    roi_uad = pipelines_path + "\\roi-无监督"
    roi_OCR = pipelines_path + "\\roi-OCR"
    rapid_det = pipelines_path + "\快速定位_检测"
    rapid_seg = pipelines_path + "\快速定位_分割"


class dark_save_path():
    '''适配深色主题'''
    

