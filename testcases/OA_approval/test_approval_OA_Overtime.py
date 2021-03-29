import shelve

from common.contants import basepage_dir, test_approval_OA_Overtime_dir
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
        # 获取basepage.yaml中设置的环境变量
        wm_env =  datas["default"]
        # 根据环境变量取对应的账号和密码
        user_env = datas["user"][wm_env]
        # 根据环境变量取对应的睡眠时间
        sleep_env = datas["sleeps"][wm_env]
        return user_env,sleep_env

def get_data(option):
    '''
    获取yaml测试数据
    '''
    with open(test_approval_OA_Overtime_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Approval_OA_Overtime:


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
                username(self._setup_datas[0]["username"]).password(self._setup_datas[0]["password"]).save(). \
                goto_OA_approval()

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    def test_the_fir_approved_OA_Overtime_not_tips(self):
        '''
        验证OA审批批准,第一行数据,not_tips
        '''
        db = shelve.open("overtimeSn")
        result = self.main. \
            goto_Overtime_approvals().goto_pending_for_approval_OA_Overtime(). \
            goto_details_of_the_fir_OA_Overtime(). \
            approved_OA_Overtime(). \
            goto_approved_OA_Overtime().get_the_status_of_overtimeSn(db["overtimeSn"])
        db.close()
        assert result == "批准"


    @pytest.mark.parametrize("data", get_data("test_not_approved_OA_Overtime"))
    def test_not_approved_OA_Overtime(self, data):
        '''
        验证OA审批不批准
        '''
        result = self.main. \
            goto_Overtime_approvals().goto_pending_for_approval_OA_Overtime(). \
            goto_details_of_overtimeSn_OA_Overtime(data["overtimeSn"]).\
            remark_OA_Overtime(data["remark"]).not_approved_OA_Overtime().\
            goto_approved_OA_Overtime().get_the_status_of_overtimeSn(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_reminder_of_supplement_OA_Overtime"))
    def test_reminder_of_supplement_OA_Overtime(self, data):
        '''
        验证OA审批-提醒资料补充
        '''
        result = self.main. \
            goto_Overtime_approvals().goto_pending_for_approval_OA_Overtime(). \
            goto_details_of_overtimeSn_OA_Overtime(data["overtimeSn"]).\
            reminder_of_supplement_OA_Overtime().close_details_OA_Overtime(). \
            goto_details_of_overtimeSn_OA_Overtime(data["overtimeSn"]). \
            get_approval_history_action()
        assert result == data["expect"]
