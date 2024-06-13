# -*- coding: utf-8 -*-
import os, re, time, xlrd
import logging
import pyautogui
import pyperclip
from playwright.sync_api import sync_playwright
from common.Airtest_method import airtest_method
from airtest.core.api import *

# Create a logger and set the log level to INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Add a StreamHandler to send log messages to console
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
# 录制：python -m playwright codegen

def docqq_easylogin(page):
    # logger.info("qq快捷登录（PC已经登录QQ）~~~~~~~~~~~~~~")
    try:
        # logger.info("点击 登录腾讯文档")
        page.get_by_role("button", name="登录腾讯文档").click()
        time.sleep(3)
        # logger.info("点击 QQ登录->点击登录qq头像")
        page.get_by_text("QQ登录").click()
        time.sleep(5)
        # logger.info("点击qq头像~~~~~~~~~~~~~~")
        pyautogui.click(1019, 621)
        time.sleep(5)
        # logger.info("登录success")
    except Exception as err:
        logger.error(f"login FAIL:{err}")

def docqq_login(page, username, password):
    # logger.info("开始腾讯文档登录~~~~~~~~~~~~~~")
    try:
        logger.info("点击 登录腾讯文档")
        page.get_by_role("button", name="登录腾讯文档").click()
        time.sleep(3)
        logger.info(
            "点击 QQ登录-点击 密码登录->点击 支持QQ号/邮箱/手机号登录->输入账号->点击 请输入密码->输入密码->回车确认")
        page.get_by_text("QQ登录").click()
        time.sleep(1)
        page.frame_locator("iframe[name=\"login_frame\"]").frame_locator("iframe[name=\"ptlogin_iframe\"]").get_by_role(
            "link", name="密码登录").click()
        time.sleep(1)
        page.frame_locator("iframe[name=\"login_frame\"]").frame_locator(
            "iframe[name=\"ptlogin_iframe\"]").get_by_label("支持QQ号/邮箱/手机号登录").click()
        time.sleep(1)
        page.frame_locator("iframe[name=\"login_frame\"]").frame_locator(
            "iframe[name=\"ptlogin_iframe\"]").get_by_label("支持QQ号/邮箱/手机号登录").fill(username)
        time.sleep(1)
        page.frame_locator("iframe[name=\"login_frame\"]").frame_locator(
            "iframe[name=\"ptlogin_iframe\"]").get_by_label("请输入密码").click()
        time.sleep(1)
        page.frame_locator("iframe[name=\"login_frame\"]").frame_locator(
            "iframe[name=\"ptlogin_iframe\"]").get_by_label("请输入密码").fill(password)
        time.sleep(1)
        page.frame_locator("iframe[name=\"login_frame\"]").frame_locator(
            "iframe[name=\"ptlogin_iframe\"]").get_by_label("请输入密码").press("Enter")
        logger.info("登录success")
    except Exception as err:
        logger.error(f"login FAIL:{err}")


def docqq_export(page):
    # logger.info("导出腾讯文档~~~~~~~~~~~~~~")
    try:
        page.get_by_label("file").locator("div").nth(3).click()
        time.sleep(1)
        page.get_by_role("menuitem", name="导出为").click()
        time.sleep(1)
        with page.expect_download() as download_info:
            page.get_by_role("menuitem", name="本地Excel表格 (.xlsx)").click()
        download = download_info.value
        new_path = os.path.join(os.getcwd(), download.suggested_filename)
        download.save_as(new_path)
        return new_path
    except Exception as err:
        logger.error(f"export FAIL:{err}")


def docqq_rows(page):
    # logger.info("获取文档行数~~~~~~~~~~~~~~")
    try:
        path = docqq_export(page)
        logger.info(f"download path:{path}")
        time.sleep(3)
        workbook = xlrd.open_workbook(path)
        worksheet = workbook.sheet_by_index(0)
        num_rows = worksheet.nrows
        logger.info("获取行数success")
        return num_rows
    except Exception as err:
        logger.error(f"get rows FAIL:{err}")


def open_url(page, url):
    # logger.info("打开腾讯文档~~~~~~~~~~~~~~")
    try:
        page.goto(url)
        logger.info("打开文档success")
    except Exception as err:
        logger.error(f"open doc FAIL:{err}")


def row_write(page, content):
    # logger.info("写入内容~~~~~~~~~~~~~~")
    try:
        for i in range(len(content)):
            # page.locator("#alloy-simple-text-editor").get_by_role("paragraph").click()
            # logger.info("上方文本输入框，坐标需自己填~~~~~~~~~~~~~~")
            pyautogui.click(238, 245)
            time.sleep(1)
            # page.locator("#alloy-rich-text-editor").fill("1111111111")  #不生效
            text = str(content[i])
            if contains_chinese(text):
                type_chinese_text(text)
            else:
                pyautogui.typewrite(text)
            time.sleep(1)
            # page.locator("#alloy-rich-text-editor").press("Tab")
            page.locator("#alloy-rich-text-editor").press("ArrowRight")
            time.sleep(1)
    except Exception as err:
        logger.error(f"write FAIL:{err}")


def contains_chinese(text):
    pattern = re.compile(r'[\u4e00-\u9fff]')  # 匹配中文字符的正则表达式
    return bool(re.search(pattern, text))


def type_chinese_text(text):
    # 将中文文本复制到剪贴板
    pyperclip.copy(text)
    # 模拟粘贴操作
    pyautogui.hotkey('ctrl', 'v')


def rm_tk():
    # logger.info("去除左上方页面弹框，坐标需自己填~~~~~~~~~~~~~~")
    pyautogui.click(411,87)


def run(url, content,get_images):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
        context = browser.new_context(viewport={"width": 1920, "height": 1080}, no_viewport=True)  # 全屏

        # logger.info("打开文档~~~~~~~~~~~~~")
        page = context.new_page()
        page.set_default_timeout(10000)
        open_url(page, url)
        time.sleep(10)

        # logger.info("去掉左上角讨厌的弹框~~~~~~~~~~~~~")
        rm_tk()
        time.sleep(1)

        # logger.info("登录~~~~~~~~~~~~~")
        docqq_easylogin(page)
        # docqq_login(page, username, password)
        time.sleep(5)

        # logger.info("确认当前文档行数~~~~~~~~~~~~~")
        num_rows = docqq_rows(page)
        logger.info(f"lines:{num_rows}")
        # MOCK new_path = r"C:\Users\Smartmore\Desktop\python\coding git\docsQQ\2024.xlsx"
        # MOCK num_rows = 20
        time.sleep(10)

        # logger.info("重新打开原文档首页，焦点回到首行第一列~~~~~~~~~~~~~")
        open_url(page, url)
        time.sleep(10)

        # logger.info("键盘操作，挪动焦点到待写入的位置~~~~~~~~~~~~~")
        for i in range(num_rows):
            # pyautogui.press('enter')
            page.locator("#alloy-rich-text-editor").press("ArrowDown")
            time.sleep(1)

        # logger.info("按照行写入~~~~~~~~~~~~~")
        content[0] = num_rows
        row_write(page, content)
        rm_tk()
        time.sleep(1)

        insert = Template(r"D:\ly\VDL_autotest\VDL_autotest\tools\insert.png",threshold=0.7)
        cell_image = Template(r"D:\ly\VDL_autotest\VDL_autotest\tools\cell_image.png",threshold=0.7)
        # airtest_method.touch_button(insert)
        # airtest_method.touch_button(cell_image)
        # airtest_method.operate_sleep(5.0)
        for element in get_images:
            # input_content = os.path.join(r"D:\ly\VDL_autotest\VDL_autotest\elements",element")
            airtest_method.touch_button(insert)
            airtest_method.touch_button(cell_image)
            airtest_method.operate_sleep(5.0)
            airtest_method.input_text(element)
            airtest_method.key_event('{ENTER}')
            page.locator("#alloy-rich-text-editor").press("ArrowRight")
        time.sleep(5.0)


if __name__ == "__main__":
    '''说明
    默认输入：线上文档地址doc_url，写入内容按行row_content，默认从文档的下一行接着写，比如现在10行，则从第11行写
    2个坐标需修改：row_write 里的是文档上方编辑框，rm_tk 页面弹框
    '''
    doc_url = "https://docs.qq.com/sheet/DY2NOYmlzcUtmaGNy?tab=BB08J2"  
    row_content = ["2", "china", "中国新年好", "万事大吉", "Hello"]
    run(doc_url, row_content)
    logger.info("run success")
    # time.sleep(200)
