import easyocr
from PIL import ImageGrab
from airtest.core.api import G, auto_setup
from paddleocr import PaddleOCR,draw_ocr
import cv2
from common.handle_log import do_log


#模型提前加载（全局只执行一次）
_PRELOADED_OCR = {
    "ch": PaddleOCR(use_angle_cls=True, lang="ch"),   # 简体中文模型
    "en": PaddleOCR(use_angle_cls=True, lang="en"),   # 英文模型
    "japan": PaddleOCR(use_angle_cls=True, lang="japan"), #日文模型
}

def prepare_for_ocr(crop_bgr, scale=2):
    # 灰度化 + 二值化 + 放大增强
    gray = cv2.cvtColor(crop_bgr, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    binary_bgr = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    resized = cv2.resize(binary_bgr, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    return resized

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

    #裁图并识别
    x1, y1, x2, y2 = region

    if x2 - x1 <= 1 or y2 - y1 <= 1:
        do_log.error("⚠️ 裁剪区域无效或太小，跳过识别")
    else:
        crop_bgr = screen_bgr[y1:y2, x1:x2]
        ocr_engine = _PRELOADED_OCR[lang]
        raw_results = ocr_engine.ocr(crop_bgr, cls=True)
        if raw_results is None:
            do_log.error("⚠️ OCR 识别返回 None，可能图像无内容或太模糊")
        else:
            for line in raw_results:
                print(line)

    # # 裁剪区域（注意 numpy[y, x]）
    # x1, y1, x2, y2 = region
    # crop_bgr = screen_bgr[y1:y2, x1:x2]

    # # 可选：保存裁剪图以便调试
    # if save_crop_path:
    #     cv2.imwrite(save_crop_path, crop_bgr)

    # # 使用预加载模型引擎
    # ocr_engine = _PRELOADED_OCR[lang]
    # raw_results = ocr_engine.ocr(crop_bgr, cls=True)

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
def ocr_touch(target_text, exact_match=False) :
    """使用OCR识别并点击指定文本
    
    Args:
        target_text (str): 要查找并点击的目标文本
        exact_match (bool): 是否精确匹配，默认为False
            - False: 部分匹配，只要目标文本是识别文本的一部分即可
            - True: 精确匹配，识别文本必须完全等于目标文本
        
    Returns:
        None
        
    Example:
        >>> ocr_touch("请输入")  # 部分匹配，会匹配到"方案*请输入"中的"请输入"
        >>> ocr_touch("请输入", exact_match=True)  # 精确匹配，只会匹配到"请输入"
        
    Note:
        - 使用PaddleOCR进行中文文本识别
        - 如果找到目标文本，会点击其中心位置
        - 如果未找到目标文本，会打印提示信息
    """
     # 截屏
    # pic_path=r"./now.png"
    # G.DEVICE.snapshot(pic_path)
    pic_path = r"C:\Users\user\Documents\ShareX\Screenshots\2025-05\VDL_tgdrjxAMLL.png"
    
    # 使用PaddleOCR识别文字
    ocr = PaddleOCR(use_angle_cls=True, lang="japan") 
    ocr_result = ocr.ocr(pic_path, cls=True)
    
    # 遍历识别结果，找到目标文字的坐标
    target_coords = None
    for line in ocr_result:
        for word_info in line:
            #获取识别结果的文字信息
            textinfo = word_info[1][0]
            print(textinfo)
            # do_log.info(f"识别结果：{textinfo}")
            
            # 根据匹配模式判断是否匹配
            if exact_match:
                if textinfo == target_text:
                    target_coords = get_center_coords(word_info[0])
                    print(target_coords)
                    break
            else:
                if target_text in textinfo:
                    target_coords = get_center_coords(word_info[0])
                    print(target_coords)
                    break
        if target_coords:
            break

    # 点击坐标
    # if target_coords:
    #     G.DEVICE.touch(target_coords)
    #     print(target_coords)
    #     # do_log.info(f"点击坐标：{target_coords}")
    # else:
    #     print(f"未找到目标文字：{target_text}")
        # do_log.error(f"未找到目标文字：{target_text}")

def get_center_coords(bbox):
    """计算文本框的中心坐标
    
    Args:
        bbox: 文本框的四个角坐标
        
    Returns:
        tuple: (x, y) 中心点坐标
    """
    x1, y1 = bbox[0]
    x2, y2 = bbox[2]
    print(x1,y1,x2,y2)
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def ocr_organize(file_path_list):
    ocr_list = []
    for file in file_path_list:
        reader = easyocr.Reader(['en'])
        results = reader.readtext(file)
        print(results[1][1])
        ocr_list.append(results[1][1])
    #print(ocr_list)
    return ocr_list

def translate_text(left, top, right, bottom):
    '''根据坐标点截图并进行OCR识别'''
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot.save(r'D:\ly\VDL_autotest\VDL_autotest\截图.png')
    screenshot_path = r"D:\ly\VDL_autotest\VDL_autotest\截图.png"
    reader = easyocr.Reader(['en'])
    results = reader.readtext(screenshot_path)
    print(results[0][1])
    return results[0][1]



if __name__ == "__main__":
    # ocr_path = []
    # path1 = r"C:\Users\yunli\Desktop\ly_autotest\VDL_autotest\elements\static\SEG_infer_min.png"
    # path2 = r"C:\Users\yunli\Desktop\ly_autotest\VDL_autotest\elements\static\SEG_infer_max.png"1198,199,1302,226
    # ocr_path = [path1,path2]
    ocr_touch("モード選択")