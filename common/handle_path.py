import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))  # 获取主目录
CONF_PATH = os.path.join(BASE_PATH, 'configs')
CONF_FILE_PATH = os.path.join(CONF_PATH, 'testcases.yaml')
LOG_PATH = os.path.join(BASE_PATH, 'logs')
REPORTS_PATH = os.path.join(BASE_PATH, 'reports')
pass
