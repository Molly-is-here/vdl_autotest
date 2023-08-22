import easyocr

def ocr_organize(file_path_list):
    ocr_list = []
    for file in file_path_list:
        reader = easyocr.Reader(['ar'])
        result = reader.readtext(file)
        print(result)
        ocr_list.append(result)
    print(ocr_list)

    