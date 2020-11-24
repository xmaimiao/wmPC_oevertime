from common.contants import basepage_dir, test_overtime_approval_dir
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

class Test_Overtime_Approval:
    with open(test_overtime_approval_dir, encoding="utf-8") as f:

        datas = yaml.safe_load(f)
        test_the_overtimeSn_for_approved_datas = datas["test_the_overtimeSn_for_approved"]
        test_the_overtimeSn_for_not_approved_datas = datas["test_the_overtimeSn_for_not_approved"]
        test_reminder_of_supplement_datas = datas["test_reminder_of_supplement"]
    _setup_datas = get_env()
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
            self.main.close()

    @pytest.mark.parametrize("data", test_the_overtimeSn_for_approved_datas)
    def test_the_overtimeSn_for_approved(self,data):
        '''
        根據加班單號進行審批：審批通過
        :return:
        '''
        result = self.main. \
            goto_overtime_approval().\
            goto_pending_for_approval().\
            the_overtimeSn_for_approved(data["overtimeSn"]). \
            goto_approved().\
            get_the_overtimeSn_status(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_the_overtimeSn_for_not_approved_datas)
    def test_the_overtimeSn_for_not_approved(self,data):
        '''
        根據加班單號進行審批：審批不批准
        '''
        result = self.main.goto_overtime_approval().\
            goto_pending_for_approval().\
            the_overtimeSn_for_not_approved(data["overtimeSn"]).\
            goto_approved().\
            get_the_overtimeSn_status(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_reminder_of_supplement_datas)
    def test_reminder_of_supplement(self, data):
        '''
        根據加班單號進行补充资料提醒操作
        '''
        result = self.main.goto_overtime_approval(). \
            goto_pending_for_approval(). \
            goto_approval_detail(data["overtimeSn"]). \
            click_reminder_of_supplement().close_poppage().\
            goto_approval_detail(data["overtimeSn"]).get_approval_history_action()
        assert result == data["expect"]
