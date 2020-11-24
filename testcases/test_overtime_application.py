import shelve
from common.contants import basepage_dir, test_overtime_application_dir
from page.basepage import  _get_working
from page.main import Main
import pytest
import yaml

def get_env():
    '''
    获取环境变量：uat、dev、mo正式站
    '''
    with open(basepage_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        wm_env = datas["default"]
        setup_datas = datas[wm_env]
        return setup_datas

class Test_Overtime_Application:

    with open(test_overtime_application_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_overtime_application_datas = datas["test_overtime_application"]
        test_the_overtimeSn_for_cancel_datas = datas["test_the_overtimeSn_for_cancel"]
        test_upload_supplementary_meterials_datas = datas["test_upload_supplementary_meterials"]
    #获取环境变量，basepage中设置的登陆账号和密码
    _setup_datas = get_env()
    # 获取环境变量：1.端口调试、无界面浏览器、有界面浏览器、dockers环境运行 ； 2.dev\ust\mo
    _working = _get_working()
    if _working == "port":
        def setup(self):
            '''
            開啓調試端口啓用
            '''
            self.main = Main()
    else:
        def setup_class(self):
            '''
            非調試端口用
            '''
            self.main = Main().goto_login(). \
                username(self._setup_datas["username"]).password(self._setup_datas["password"]).save(). \
                goto_application(). \
                goto_overtime(self._setup_datas["application"])

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            # self.db.close()
            self.main.close()

    @pytest.mark.parametrize("data", test_overtime_application_datas)
    def test_overtime_application(self, data):
        '''
        验证申請加班
        '''
        result = self.main.goto_overtime_application().\
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]).\
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]).\
            save_click().wait_sleep(data["sleeps"]).edit_IDcard(data["IDcard"]).get_page_title()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_the_overtimeSn_for_cancel_datas)
    def test_the_overtimeSn_for_cancel(self,data):
        '''
        验证根据加班申请单号进行撤销操作
        '''
        result = self.main.goto_my_overtime_records().\
            the_overtimeSn_for_cancel(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_upload_supplementary_meterials_datas)
    def test_upload_supplementary_meterials(self,data):
        '''
        验证根据加班单号进行资料补充操作
        '''
        result = self.main.goto_my_overtime_records().\
            goto_application_detail(data["overtimeSn"]).\
            upload_supplementary_meterials(data["excel_path"]).\
            get_approval_history_action()
        assert result == data["expect"]