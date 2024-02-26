import easyocr
from PIL import ImageGrab


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
    # ocr_organize(ocr_path)
    translate_text()