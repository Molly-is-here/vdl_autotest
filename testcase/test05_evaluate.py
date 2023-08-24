import pytest
from common.Airtest_method import airtest_method
from elements.public_control import control
from common.handle_log import do_log
from pages.assess_page import assess
from pages.open_sofrware import open_Software

@pytest.mark.smoke
def test_export_model():
    airtest_method.touch_button(control.new_card)
    assess.model_assess()
    if not airtest_method.check_exit(control.report_button,'FALSE',36000) :
        assert False,'评估未完成'
    else:   
        assess.more_button()
        assess.export_model()
        do_log.info('模型成功导出,用例执行成功')

@pytest.mark.smoke
def test_export_report():
    assess.export_report()
    airtest_method.operate_sleep(5.0)
    open_Software.connect_sofeware("Windows:///?title_re=MainWindow.*")
    do_log.info('报告成功导出,用例执行成功')

