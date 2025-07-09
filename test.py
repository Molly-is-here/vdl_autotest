from airtest.core.api import G, auto_setup
from paddleocr import PaddleOCR,draw_ocr
import cv2
from pages.open_sofrware import open_Software

# 1) 在脚本开头做一次环境初始化（路径/设备等）
auto_setup(__file__)
open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")

# 2) 模型提前加载（全局只执行一次）
_PRELOADED_OCR = {
    "ch": PaddleOCR(use_angle_cls=True, lang="ch"),   # 简体中文模型
    "en": PaddleOCR(use_angle_cls=True, lang="en"),   # 英文模型
    "japan": PaddleOCR(use_angle_cls=True, lang="japan"),
}


def ocr_region(region, lang=None, save_crop_path=None):
    """
    在 Airtest 当前屏幕上截取 region 区域，并用预加载的 PaddleOCR 识别文本。
    
    Args:
        region (tuple): (x1, y1, x2, y2) 截图区域。
        lang (str): OCR 识别语言模型，例如 "ch"、"en"、"japan" 等。
        save_crop_path (str, optional): 如需保存裁剪图，传入文件名。

    Returns:
        List[dict]: 每个识别到的文本块，包含：
            - 'text': 识别到的字符串
            - 'confidence': 置信度
            - 'bbox': 四点坐标
    """
    if lang is None or lang not in _PRELOADED_OCR:
        raise ValueError(f"Unsupported or missing lang: {lang}")

    # 全屏截图，返回 numpy.ndarray，格式 BGR
    screen_bgr = G.DEVICE.snapshot()

    # 裁剪区域（注意 numpy[y, x]）
    x1, y1, x2, y2 = region
    crop_bgr = screen_bgr[y1:y2, x1:x2]

    # 可选：保存裁剪图以便调试
    if save_crop_path:
        cv2.imwrite(save_crop_path, crop_bgr)

    # 使用预加载模型引擎
    ocr_engine = _PRELOADED_OCR[lang]
    raw_results = ocr_engine.ocr(crop_bgr, cls=True)

    # 整理结果
    texts = []
    for line in raw_results:
        for bbox, (txt, conf) in line:
            texts.append({
                "text": txt,
                "confidence": conf,
                "bbox": bbox
            })
    return texts
def ocr_touch(target_text) :
    """使用OCR识别并点击指定文本
    
    Args:
        target_text (str): 要查找并点击的目标文本
        
    Returns:
        None
        
    Example:
        >>> ocr_touch("オープンプロジェクト")  # 点击"打开项目"按钮
        
    Note:
        - 使用PaddleOCR进行日文文本识别
        - 如果找到目标文本，会点击其中心位置
        - 如果未找到目标文本，会打印提示信息
    """
     # 截屏
    pic_path=r"./now.png"
    G.DEVICE.snapshot(pic_path)
    
    # 使用PaddleOCR识别文字
    ocr = PaddleOCR(use_angle_cls=True, lang="ch") 
    ocr_result = ocr.ocr(pic_path, cls=True)
    
    # 遍历识别结果，找到目标文字的坐标
    target_coords = None
    for line in ocr_result:
        for word_info in line:
            #获取识别结果的文字信息
            textinfo = word_info[1][0]
            print(textinfo)
            
            if target_text in textinfo:
                # 获取文字的坐标（中心点）
                x1, y1 = word_info[0][0]
                x2, y2 = word_info[0][2]
                target_coords = ((x1 + x2) / 2, (y1 + y2) / 2)
                break
        if target_coords:
            break

    # 点击坐标
    if target_coords:
        G.DEVICE.touch(target_coords)
    else:
        print(f"未找到目标文字：{target_text}")


# —— 使用示例 —— #
if __name__ == "__main__":
    region1 = (25,290,205,326)  #给出控件的两个坐标X1,Y1,X2,Y2
    region2 = (368,63,580,100)

    results_cn1 = ocr_region(region1, lang="japan", save_crop_path="crop_cn1.png")
    results_cn2 = ocr_region(region2, lang="japan", save_crop_path="crop_cn2.png")

    print("识别结果1：", results_cn1)
    print("识别结果2：", results_cn2)

    
