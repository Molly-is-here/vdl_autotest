import os

class save_path():
    base_path = os.path.dirname(__file__)
    dataset_path = r"\\10.80.31.43\vimo数据SVNwc\15_VDL_autotest_dataset"      
    smoke_path = r"\\10.80.31.43\vimo数据SVNwc\14.VDL_SDK自动化\VDL_datasets"    #冒烟测试数据集
    project_path = r"D:\ly\VDL_projects"
    #选择模型类型（四类算法）
    cls = base_path + "/public/分类算法.png"
    det = base_path + "/public/检测算法.png"
    seg = base_path + "/public/分割算法.png"
    ocr = base_path + "/public/OCR算法.png"
    uad = base_path + "/public/无监督算法.png"
    project_list = [ocr,uad]

    #数据集（四类算法） 
    # cls_dataset = base_path + "/分类算法/dataset"
    # det_dataset = base_path + "/检测算法/dataset"
    # seg_dataset = base_path + "/分割算法/dataset"
    # ocr_dataset = base_path + "/ocr算法/dataset"

    '''新建方案数据集'''
    cls_dataset = smoke_path + "\分类算法"
    det_dataset = smoke_path + "\检测算法"
    seg_dataset = smoke_path + "\分割算法"
    ocr_dataset = smoke_path + "\OCR算法"
    uad_dataset = smoke_path + "\无监督算法"

    '''打开方案数据集'''
    cls_project = project_path + "\分类算法"
    det_project = project_path + "\检测算法"
    seg_project = project_path + "\分割算法"
    ocr_project = project_path + "\OCR算法"
    uad_project = project_path + "\无监督算法"