import pytest
from pages.open_sofrware import open_Software

open_Software.open_sofeware(r".\VDL.exe")
open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
open_Software.click_maximize() 

#run_command = ['C:\\Users\\yunli\\Desktop\\ly_autotest\\VDL_autotest_0804\\testcase\\test_01_openproj.py',
#               'C:\\Users\\yunli\\Desktop\\ly_autotest\\VDL_autotest_0804\\testcase\\test_02_inferpage.py']


# run_command = [ 'C:\\Users\\yunli\\Desktop\\ly_autotest\\VDL_autotest\\testcase\\test01_management.py',
#                 'C:\\Users\\yunli\\Desktop\\ly_autotest\\VDL_autotest\\testcase\\test02_data.py',
#                 'C:\\Users\\yunli\\Desktop\\ly_autotest\\VDL_autotest\\testcase\\test03_label.py',
#                 'C:\\Users\\yunli\\Desktop\\ly_autotest\\VDL_autotest\\testcase\\test04_training.py',
#                 'C:\\Users\\yunli\\Desktop\\ly_autotest\\VDL_autotest\\testcase\\test05_evaluate.py',
#                 'C:\\Users\\yunli\\Desktop\\ly_autotest\\VDL_autotest\\testcase\\test06_infer.py']

run_command = ['C:\\Users\\yunli\\Desktop\\ly_autotest\\VDL_autotest\\testcase\\test_02_inferpage.py']

pytest.main(run_command) 
