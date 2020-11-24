import shelve

from common.contants import basepage_dir, test_approval_OA_ALL_dir
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

class Test_Approval_OA_ALL:

    with open(test_approval_OA_ALL_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_approved_OA_ALL_agreement_datas = datas["test_approved_OA_ALL_agreement"]
        test_not_approved_OA_ALL_agreement_datas = datas["test_not_approved_OA_ALL_agreement"]
        test_approved_OA_ALL_datas = datas["test_approved_OA_ALL"]
        test_not_approved_OA_ALL_datas = datas["test_not_approved_OA_ALL"]
        test_reminder_of_supplement_OA_ALL_datas = datas["test_reminder_of_supplement_OA_ALL"]


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
            # 讀取數據庫
            self.main = Main().goto_login(). \
                username(self._setup_datas["username"]).password(self._setup_datas["password"]).save(). \
                goto_OA_approval()

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data", test_approved_OA_ALL_agreement_datas)
    def test_approved_OA_ALL_agreement(self, data):
        '''
        验证OA审批，勾选协议
        '''
        result = self.main.goto_ALL_approvals().\
            goto_pending_for_approval_OA_ALL().\
            goto_details_of_overtimeSn_OA_ALL(data["overtimeSn"]).\
            agree_overtime_work_agreement().approved_OA_ALL().\
            goto_approved_OA_ALL().get_the_status_of_overtimeSn(data["overtimeSn"])
        assert result == data["expect"]


    @pytest.mark.parametrize("data", test_approved_OA_ALL_datas)
    def test_approved_OA_ALL(self, data):
        '''
        验证OA审批，勾选协议
        '''
        result = self.main.goto_ALL_approvals().\
            goto_pending_for_approval_OA_ALL().\
            goto_details_of_overtimeSn_OA_ALL(data["overtimeSn"]).\
            approved_OA_ALL().goto_approved_OA_ALL().\
            get_the_status_of_overtimeSn(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_not_approved_OA_ALL_agreement_datas)
    def test_not_approved_OA_ALL_agreement(self, data):
        '''
        验证OA审批不批准，勾选协议
        '''
        result = self.main.goto_ALL_approvals().\
            goto_pending_for_approval_OA_ALL().\
            goto_details_of_overtimeSn_OA_ALL(data["overtimeSn"]).\
            agree_overtime_work_agreement().remark_OA_ALL(data["remark"]).not_approved_OA_ALL().\
            goto_approved_OA_ALL().get_the_status_of_overtimeSn(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_not_approved_OA_ALL_datas)
    def test_not_approved_OA_ALL(self, data):
        '''
        验证OA审批不批准
        '''
        result = self.main.goto_ALL_approvals().\
            goto_pending_for_approval_OA_ALL().\
            goto_details_of_overtimeSn_OA_ALL(data["overtimeSn"]).\
            remark_OA_ALL(data["remark"]).not_approved_OA_ALL().\
            goto_approved_OA_ALL().get_the_status_of_overtimeSn(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_reminder_of_supplement_OA_ALL_datas)
    def test_reminder_of_supplement_OA_ALL(self, data):
        '''
        验证OA审批-提醒资料补充
        '''
        result = self.main.goto_ALL_approvals().\
            goto_pending_for_approval_OA_ALL().\
            goto_details_of_overtimeSn_OA_ALL(data["overtimeSn"]).\
            reminder_of_supplement_OA_ALL().close_details_OA_ALL(). \
            goto_details_of_overtimeSn_OA_ALL(data["overtimeSn"]). \
            get_approval_history_action()
        assert result == data["expect"]
