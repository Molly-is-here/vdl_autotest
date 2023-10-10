import os
import sys
import pytest

addpath = os.path.dirname(__file__)
if addpath not in sys.path:
    sys.path.append(addpath)
from pages.open_sofrware import open_Software

open_Software.open_sofeware(r".\VDL.exe")
open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
open_Software.click_maximize() 

run_command = ['D:\\ly\\VDL_autotest\\VDL_autotest\\testcase\\test01_management.py',
               'D:\\ly\\VDL_autotest\\VDL_autotest\\testcase\\test02_data.py',
                f'--alluredir={addpath}/report', '--clean-alluredir']


# run_command = ['D:\\ly\\VDL_autotest\\VDL_autotest\\testcase01\\test_01_openproj.py',
#                 'D:\\ly\\VDL_autotest\\VDL_autotest\\testcase\\test01_management.py',
#                 'D:\\ly\\VDL_autotest\\VDL_autotest\\testcase\\test02_data.py',
#                 'D:\\ly\\VDL_autotest\\VDL_autotest\\testcase\\test03_label.py',
#                 'D:\\ly\\VDL_autotest\\VDL_autotest\\testcase\\test04_training.py',
#                 'D:\\ly\VDL_autotest\\VDL_autotest\\testcase\\test05_evaluate.py',
#                 'D:\\ly\\VDL_autotest\\VDL_autotest\\testcase\\test06_infer.py']

# run_command = ['D:\\ly\\VDL_autotest\\VDL_autotest\\testcase\\test00_smoke.py']

pytest.main(run_command) 

# os.system('allure serve report')