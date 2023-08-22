import easyocr

def ocr_organize(file_path_list):
    ocr_list = []
    for file in file_path_list:
        reader = easyocr.Reader(['ar'])
        results = reader.readtext(file)
        print(results[1][1])
        ocr_list.append(results[1][1])
    #print(ocr_list)
    return ocr_list

if __name__ == "__main__":
    ocr_path = []
    path1 = r'C:\Users\yunli\Desktop\ly_autotest\VDL_autotest_0804\elements\static\UAD.png'
    path2 = r'C:\Users\yunli\Desktop\ly_autotest\VDL_autotest_0804\elements\static\cls.png'
    ocr_path = [path1,path2]
    ocr_organize(ocr_path)