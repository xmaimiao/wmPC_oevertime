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
    with open(test_overtime_approval_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Overtime_Approval:

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

    # 操作第一行数据
    def test_the_fir_for_approved(self):
        '''
        第一行数据：審批通過（列表页批准）
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            the_fir_for_approved(). \
            goto_approved(). \
            get_the_fir_status()
        assert result == "批准"

    def test_the_fir_for_approved_detail(self):
        '''
        第一行数据：審批通過（详情页批准）
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            goto_the_fir_approval_detail(). \
            click_approved().goto_approved().\
            get_the_fir_status()
        assert result == "批准"

    def test_the_fir_for_approved_detail_tips(self):
        '''
        第一行数据：審批通過，有tips（详情页批准）
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            goto_the_fir_approval_detail(). \
            click_approved().\
            click_tips_confirm().goto_approved().\
            get_the_fir_status()
        assert result == "批准"

    def test_the_fir_for_approved_tips(self):
        '''
        第一行数据：審批通過，有tips（列表页批准）
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            the_fir_for_approved(). \
            click_tips_confirm().goto_approved(). \
            get_the_fir_status()
        assert result == "批准"


    def test_the_fir_for_not_approved(self):
        '''
        第一行数据：審批不批准（列表页）
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            the_fir_for_not_approved(). \
            goto_approved(). \
            get_the_fir_status()
        assert result == "不批准"

    def test_the_fir_for_not_approved_detail(self):
        '''
        第一行数据：審批不批准（详情页）
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            goto_the_fir_approval_detail(). \
            click_not_approved(). \
            goto_approved(). \
            get_the_fir_status()
        assert result == "不批准"

    def test_the_fir_reminder_of_supplement(self):
        '''
        第一行数据：补充资料提醒操作
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval().goto_the_fir_approval_detail().\
            click_reminder_of_supplement().close_poppage(). \
            get_approval_history_action()
        assert result == "補充資料提醒"

    def test_check_all_batch_agree(self):
        '''
        全选，批量批准，有tips
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval().check_all().\
            click_tips_confirm().batch_agree()
        assert result == True


    # 根据加班单号操作

    @pytest.mark.parametrize("data", get_data("test_the_overtimeSn_for_approved"))
    def test_the_overtimeSn_for_approved(self,data):
        '''
        根據加班單號進行審批：審批通過（列表页批准）
        '''
        result = self.main. \
            goto_overtime_approval().\
            goto_pending_for_approval().\
            the_overtimeSn_for_approved(data["overtimeSn"]). \
            goto_approved().\
            get_the_overtimeSn_status(data["overtimeSn"])
        assert result == data["expect"]


    @pytest.mark.parametrize("data", get_data("test_the_overtimeSn_for_approved"))
    def test_the_overtimeSn_for_approved_tips(self,data):
        '''
        根據加班單號進行審批：審批通過，有tips（列表页批准）
        '''
        result = self.main. \
            goto_overtime_approval().\
            goto_pending_for_approval().\
            the_overtimeSn_for_approved(data["overtimeSn"]). \
            click_tips_confirm().goto_approved().\
            get_the_overtimeSn_status(data["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_the_overtimeSn_for_not_approved"))
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

    @pytest.mark.parametrize("data", get_data("test_reminder_of_supplement"))
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

