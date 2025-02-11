__author__ = "yunliu"
import pytest
import allure
from common.Airtest_method import airtest_method
from pages.assess_page import assess
from common.handle_log import do_log

airtest_method.operate_sleep(5.0)

@allure.feature('菜单栏')
@allure.title('关闭方案')
@pytest.mark.smoke
def test_template_close():
    with allure.step(f'点击文件按钮'):
        assess.template_file()
    with allure.step(f'点击关闭方案'):
        assess.template_close()
        airtest_method.operate_sleep()
    do_log.info('关闭方案成功，用例执行成功')

@allure.title('导出SDK')
@pytest.mark.smoke
def test_template_SDK():
    with allure.step(f'点击文件按钮'):
        assess.template_file()
    with allure.step(f'导出SDK'):
        assess.template_SDK()
    do_log.info('导出SDK成功，用例执行成功')

@allure.title('高级设置')
def test_template_advanced():
    with allure.step(f'点击设置按钮'):
        assess.template_setting()
    with allure.step(f'点击高级设置'):
        worker,automl,maxdetect = 4,0.6,20
        assess.template_advanced(worker,automl,maxdetect)
    with allure.step(f'校验高级设置是否生效'):
        file_path = r"D:\ViMo-Deeplearning\setting.ini"
        with open(file_path, 'r',encoding='utf-8') as file:
            found_worker = False
            found_automl = False
            found_maxdetect = False
            for line in file:
                if f'Worker={worker}' in line:
                    found_worker = True
                if f'AutoMLIter={automl}' in line:
                    found_automl = True
                if f'MaxDetect={maxdetect}' in line:
                    found_maxdetect = True
                
                # 如果三者都找到了，则日志输出并退出
                if found_worker and found_automl and found_maxdetect:
                    do_log.info('高级设置生效，用例执行成功')
                    assess.template_setting()
                    break
            else:
                # 如果遍历完整个文件仍未找到所有条件
                assert False, '高级设置未生效'

@allure.title('导出软件功能手册')
@pytest.mark.smoke
def test_user_guild():
    with allure.step(f'点击帮助按钮'):
        assess.template_help()
    with allure.step(f'导出软件功能手册'):
        assess.user_guild()
    do_log.info('软件功能手册导出成功，用例执行成功')

@allure.title('导出软件操作手册')
@pytest.mark.smoke
def test_operating_guild():
    with allure.step(f'点击帮助按钮'):
        assess.template_help()
    with allure.step(f'导出软件操作手册'):
        assess.operating_guild()
    do_log.info('软件操作手册导出成功，用例执行成功')

@allure.title('导出软件使用SDK开发手册')
@pytest.mark.smoke
def test_SDK_guild():
    with allure.step(f'点击帮助按钮'):
        assess.template_help()
    with allure.step(f'导出C++ SDK开发手册'):
        assess.SDK_guild('c++')
    with allure.step(f'导出Csharp SDK开发手册'):
        assess.SDK_guild('csharp')
    with allure.step(f'导出Python SDK开发手册'):
        assess.SDK_guild('python')
        assess.template_help()
    do_log.info('SDK开发手册导出成功，用例执行成功')
