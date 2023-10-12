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

# run_command = [f'{addpath}/testcase/test01_management.py',
#                 f'{addpath}/testcase/test02_data.py',
#                 f'{addpath}/testcase/test03_label.py',
#                 f'{addpath}/testcase/test04_training.py',
#                 f'{addpath}/testcase/test05_evaluate.py',
#                 f'{addpath}/testcase/test06_infer.py',
#                 f'{addpath}/testcase/test07_menu.py',
#                 f'--alluredir={addpath}/report', '--clean-alluredir']
run_command = [f'{addpath}/testcase/test01_management.py',
                f'--alluredir={addpath}/report', '--clean-alluredir']



pytest.main(run_command) 

# os.system('allure serve report')