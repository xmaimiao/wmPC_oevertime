from common.contants import basepage_dir, test_overtime_approval_HR_dir
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
    with open(test_overtime_approval_HR_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Overtime_Approval_HR:

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
                username(self._setup_datas[0]["username"]).password(self._setup_datas[0]["password"]).save(). \
                goto_application(). \
                goto_overtime(self._setup_datas[0]["application"])

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    # 第一行数据操作
    def test_the_fir_for_approved_HR_tips(self):
        '''
        第一行数据：審批通過，有tips
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            the_fir_for_approved_HR().\
            click_tips_confirm_HR().goto_approved_HR().\
            wait_sleep(1).get_the_fir_status_HR()
        assert result == "批准"

    def test_the_fir_for_approved_HR(self):
        '''
        第一行数据:審批通過
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            the_firfor_approved_HR().goto_approved_HR().\
            wait_sleep(1).get_the_fir_status_HR()
        assert result == "批准"

    def test_the_fir_for_not_approved_HR(self):
        '''
        第一行数据：審批不通過
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            the_fir_for_not_approved_HR().goto_approved_HR().\
            wait_sleep(1).get_the_fir_status_HR()
        assert result == "不批准"

    def test_the_fir_reminder_of_supplement_HR(self):
        '''
        第一行数据：补充资料提醒
        '''

        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            goto_the_fir_approval_detail_HR(). \
            click_reminder_of_supplement_HR().get_reminder_toast_HR()
        assert result == True

    # 根据加班单号进行操作

    @pytest.mark.parametrize("data", get_data("test_the_overtimeSn_for_approved_HR_tips"))
    def test_the_overtimeSn_for_approved_HR_tips(self,data):
        '''
        根據加班單號進行審批：審批通過，有tips
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            the_overtimeSn_for_approved_HR(data["overtimeSn"]).\
            click_tips_confirm_HR().goto_approved_HR().\
            wait_sleep(1).get_the_overtimeSn_status_HR(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_the_overtimeSn_for_approved_HR"))
    def test_the_overtimeSn_for_approved_HR(self,data):
        '''
        根據加班單號進行審批：審批通過
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            the_overtimeSn_for_approved_HR(data["overtimeSn"]).goto_approved_HR().\
            wait_sleep(1).get_the_overtimeSn_status_HR(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_the_overtimeSn_for_not_approved_HR"))
    def test_the_overtimeSn_for_not_approved_HR(self,data):
        '''
        根據加班單號進行審批：審批不通過
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            the_overtimeSn_for_not_approved_HR(data["overtimeSn"]).goto_approved_HR().\
            wait_sleep(1).get_the_overtimeSn_status_HR(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_the_application_HR_tips"))
    def test_the_application_HR_tips(self,data):
        '''
        HR代申请,有tips
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().goto_application_HR().\
            applicant(data["applicant"]).UserTel(data["UserTel"]).\
            startDate(data["startDate"]).starttime(data["starttime"]).endtime(data["endtime"]).remark(data["remark"]).\
            save_click().click_tips().IDcard(data["IDcard"]).back_to_pending().wait_sleep(1).get_ele_of_application()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_the_application_HR_tips"))
    def test_the_application_HR(self,data):
        '''
        HR代申请,无tips
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().goto_application_HR().\
            applicant(data["applicant"]).UserTel(data["UserTel"]).\
            startDate(data["startDate"]).starttime(data["starttime"]).endtime(data["endtime"]).remark(data["remark"]).\
            save_click().IDcard(data["IDcard"]).back_to_pending().wait_sleep(1).get_ele_of_application()
        assert result == True

