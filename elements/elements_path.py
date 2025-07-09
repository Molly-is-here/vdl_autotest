import os

class save_path():
    '''适配浅色主题'''
    base_path = os.path.dirname(__file__)
    dataset_path = r"\\10.80.31.43\vimo数据SVNwc\15_VDL_autotest_dataset"      
    smoke_path = r"\\10.80.31.43\vimo数据SVNwc\14.VDL_SDK自动化\VDL_datasets"        #冒烟测试数据集
    project_path = r"D:\ly\VDL_projects"                                            #兼容性测试方案
    pipelines_path = r"C:\Users\user\Desktop\串联测试数据集\串联auto_test"           #串联方案数据集
    SDK_exe_path =   r"D:\ly\VDL_autotest\tools\demo.exe"   #SDK运行exe
    project_save_path = r"C:\Users\user\Documents"

    #算法类型（适用于单模块方案）
    cls = os.path.join(base_path, "public", "分类算法.png")
    det = os.path.join(base_path, "public", "检测算法.png")
    seg = os.path.join(base_path, "public", "分割算法.png")
    ocr = os.path.join(base_path, "public", "OCR算法.png")
    uad = os.path.join(base_path, "public", "无监督算法.png")
    seqocr = os.path.join(base_path, "public", "字符串算法.png")
    clsocv = os.path.join(base_path, "public", "有监督字符检查.png")
    uadocv = os.path.join(base_path, "public", "无监督字符检查.png")
    generation = os.path.join(base_path, "public", "缺陷生成.png")
    project_list = [cls,seg,ocr,seqocr,det,clsocv,uadocv,uad]


    #冒烟测试数据集
    cls_dataset = os.path.join(smoke_path, "分类算法")
    det_dataset = os.path.join(smoke_path, "检测算法")
    seg_dataset = os.path.join(smoke_path, "分割算法")
    ocr_dataset = os.path.join(smoke_path, "OCR算法")
    uad_dataset = os.path.join(smoke_path, "无监督算法")
    seqocr_dataset = os.path.join(smoke_path, "Seqocr算法")
    clsocv_dataset = os.path.join(smoke_path, "有监督字符检查")
    uadocv_dataset = os.path.join(smoke_path, "无监督字符检查")
    generation_dataset = os.path.join(smoke_path, "缺陷生成")

    #算法校验测试方案
    cls_project = os.path.join(project_path, "分类")
    det_project = os.path.join(project_path, "检测")
    seg_project = os.path.join(project_path, "分割")
    ocr_project = os.path.join(project_path, "OCR")
    uad_project = os.path.join(project_path, "无监督")
    seqocr_project = os.path.join(project_path, "字符串")
    uadocv_project = os.path.join(project_path, "无监督字符检查")
    clsocv_project = os.path.join(project_path, "有监督字符检查")
    compare_project = [cls_project,det_project,seg_project,ocr_project,uad_project,seqocr_project,uadocv_project,clsocv_project]
    
    #串联pipelines数据集
    cls_seg = os.path.join(pipelines_path, "分类-分割")
    cls_det = os.path.join(pipelines_path, "分类-检测")
    cls_uad = os.path.join(pipelines_path, "分类-无监督")
    cls_seq = os.path.join(pipelines_path, "分类-字符串")
    det_OCR = os.path.join(pipelines_path, "检测-OCR")
    det_seg = os.path.join(pipelines_path, "检测-分割")
    det_uad = os.path.join(pipelines_path, "检测-无监督")
    seg_OCR = os.path.join(pipelines_path, "分割-OCR")
    seg_det = os.path.join(pipelines_path, "分割-检测")
    seg_uad = os.path.join(pipelines_path, "分割-无监督")
    seg_seg = os.path.join(pipelines_path, "分割-分割")
    seg_seq = os.path.join(pipelines_path, "分割-字符串")
    seq_uad = os.path.join(pipelines_path, "字符串-无监督")
    seq_seg = os.path.join(pipelines_path, "字符串-分割")
    seq_ocr = os.path.join(pipelines_path, "字符串-OCR")
    ocr_cls = os.path.join(pipelines_path, "OCR-分类")
    ocr_uad = os.path.join(pipelines_path, "OCR-无监督")
    uad_seg1 = os.path.join(pipelines_path, "无监督-分割1")
    uad_seg2 = os.path.join(pipelines_path, "无监督-分割2")
    uad_det = os.path.join(pipelines_path, "无监督-检测")
    roi_seg = os.path.join(pipelines_path, "roi-分割")
    roi_uad = os.path.join(pipelines_path, "roi-无监督")
    roi_OCR = os.path.join(pipelines_path, "roi-OCR")
    rapid_det = os.path.join(pipelines_path, "快速定位_检测")
    rapid_seg = os.path.join(pipelines_path, "快速定位_分割")
    rapid_OCR = os.path.join(pipelines_path, "快速定位_OCR")


class dark_save_path():
    '''适配深色主题'''
    

