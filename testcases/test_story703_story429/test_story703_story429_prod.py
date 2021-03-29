from common.contants import basepage_dir,test_story703_story429_prod_dir
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
    with open(test_story703_story429_prod_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Story703_Story429_Prod:

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
                username(self._setup_datas[0]["username"]).password(self._setup_datas[0]["password"]).save(). \
                goto_application(). \
                goto_overtime(self._setup_datas[0]["application"])

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            # self.db.close()
            self.main.close()

    def logout_fir_and_login(self,data):
        '''
        登入/登出
        '''
        result = self.main.logout_for_fir(). \
            username(data).password(self._setup_datas[0]["password"]).save(). \
            get_index_ele_fir()
        assert "首頁" in result

    def overtime_application(self,UserTel,startDate,starttime,endtime,remark,sleeps,IDcard):
        '''
        有tips
        '''
        result = self.main.goto_overtime_application(). \
            edit_UserTel(UserTel).edit_startDate(startDate). \
            edit_starttime(starttime).edit_endtime(endtime).edit_remark(remark). \
            save_click().click_tips().wait_sleep(sleeps).edit_IDcard(IDcard).\
            wait_sleep(2).goto_my_overtime().get_page_title()
        assert result == True

    def overtime_application_not_tips(self,UserTel,startDate,starttime,endtime,remark,sleeps,IDcard):
        '''
        无tips
        '''
        result = self.main.goto_overtime_application(). \
            edit_UserTel(UserTel).edit_startDate(startDate). \
            edit_starttime(starttime).edit_endtime(endtime).edit_remark(remark). \
            save_click().wait_sleep(sleeps).edit_IDcard(IDcard).\
            goto_my_overtime().get_page_title()
        assert result == True

    def the_fir_reminder_of_supplement(self):
        '''
        第一行数据：补充资料提醒操作
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval().goto_the_fir_approval_detail().\
            click_reminder_of_supplement(). \
            get_reminder_toast()
        assert result == True

    def the_fir_for_approved(self):
        '''
        第一行数据：審批通過，无tips
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            the_fir_for_approved(). \
            goto_approved(). \
            get_the_fir_status()
        assert result == "批准"

    def the_fir_for_approved_tips(self):
        '''
        第一行数据：審批通過，有tips
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            the_fir_for_approved(). \
            click_tips_confirm().\
            goto_approved(). \
            get_the_fir_status()
        assert result == "批准"

    def the_fir_for_approved_detail(self):
        '''
        第一行数据：審批通過，无tips（详情页）
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            goto_the_fir_approval_detail(). \
            click_approved(). \
            goto_approved(). \
            get_the_fir_status()
        assert result == "批准"

    def the_fir_for_approved_tips_detail(self):
        '''
        第一行数据：審批通過，有tips（详情页）
        '''
        result = self.main. \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            goto_the_fir_approval_detail(). \
            click_approved(). \
            click_tips_confirm().\
            goto_approved(). \
            get_the_fir_status()
        assert result == "批准"

    def the_fir_for_not_approved(self):
        '''
        第一行数据：審批不批准
        '''
        result = self.main.goto_overtime_approval().\
            goto_pending_for_approval().\
            the_fir_for_not_approved().\
            goto_approved().\
            get_the_fir_status()
        assert result == "不批准"
    def the_fir_for_not_approved_detail(self):
        '''
        第一行数据：審批不批准（详情页）
        '''
        result = self.main.goto_overtime_approval().\
            goto_pending_for_approval(). \
            goto_the_fir_approval_detail(). \
            click_not_approved(). \
            goto_approved().\
            get_the_fir_status()
        assert result == "不批准"

    def the_fir_for_approved_HR(self):
        '''
        第一行数据：HR審批通過，无tips
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            the_fir_for_approved_HR().goto_approved_HR().\
            wait_sleep(1).get_the_fir_status_HR()
        assert result == "批准"

    def the_fir_for_approved_HR_tips(self):
        '''
        第一行数据：審批通過，有tips
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            the_fir_for_approved_HR().\
            click_tips_confirm_HR().goto_approved_HR().\
            wait_sleep(1).get_the_fir_status_HR()
        assert result == "批准"

    def the_fir_for_not_approved_HR(self):
        '''
        第一行数据：HR審批不通過
        '''
        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR().\
            the_fir_for_not_approved_HR().goto_approved_HR().\
            wait_sleep(1).get_the_fir_status_HR()
        assert result == "不批准"

    def the_fir_reminder_of_supplement_HR(self):
        '''
        第一行数据：HR补充资料提醒
        '''

        result = self.main. \
            goto_overtime_approval_for_HR().goto_pending_for_approval_HR(). \
            goto_the_fir_approval_detail_HR(). \
            click_reminder_of_supplement_HR().get_reminder_toast_HR()
        assert result == True


    '''port调试端口用例'''

    @pytest.mark.parametrize("data", get_data("test_superior_reminder_and_not_approved_not_tips"))
    def test_superior_reminder_and_not_approved_not_tips(self, data):
        '''
        验证上级提醒补充资料且不批准，非輪班人員下班時間加班，輪班人員全時段加班（无tips）、列表页操作不批准
        '''
        self.logout_fir_and_login(data["applicant"])
        self.overtime_application_not_tips(data["UserTel"], data["startDate"], data["starttime"],
                                           data["endtime"], data["remark"], data["sleeps"], data["IDcard"])
        self.logout_fir_and_login(data["superior"])
        self.the_fir_reminder_of_supplement()
        self.the_fir_for_not_approved()

    @pytest.mark.parametrize("data", get_data("test_supervisor_reminder_and_not_approved_not_tips"))
    def test_supervisor_reminder_and_not_approved_not_tips(self, data):
        '''
        验证主管提醒补充资料且不批准，非輪班人員下班時間加班，輪班人員全時段加班（无tips）、列表页操作不批准
        '''
        self.logout_fir_and_login(data["applicant"])
        self.overtime_application_not_tips(data["UserTel"], data["startDate"], data["starttime"],
                                           data["endtime"], data["remark"], data["sleeps"], data["IDcard"])
        self.logout_fir_and_login(data["superior"])
        self.the_fir_for_approved()
        self.logout_fir_and_login(data["supervisor"])
        self.the_fir_reminder_of_supplement()
        self.the_fir_for_not_approved()

    @pytest.mark.parametrize("data", get_data("test_supervisor_reminder_and_not_approved"))
    def test_supervisor_reminder_and_not_approved(self, data):
        '''
        验证主管提醒补充资料且不批准，非輪班人員下班時間加班，輪班人員全時段加班（有tips）、列表页操作不批准
        '''
        self.logout_fir_and_login(data["applicant"])
        self.overtime_application_not_tips(data["UserTel"],data["startDate"],data["starttime"],
                                           data["endtime"],data["remark"],data["sleeps"],data["IDcard"])
        self.logout_fir_and_login(data["superior"])
        self.the_fir_for_approved_tips()
        self.logout_fir_and_login(data["supervisor"])
        self.the_fir_reminder_of_supplement()
        self.the_fir_for_not_approved()

    # bug29212 HR审批和上级主管审批。详情页点击审批按钮无效
    @pytest.mark.parametrize("data", get_data("test_supervisor_reminder_and_not_approved_not_tips_detail"))
    def test_supervisor_reminder_and_not_approved_not_tips_detail(self, data):
        '''
        验证主管提醒补充资料且不批准，非輪班人員下班時間加班，輪班人員全時段加班（无tips）、详情页操作批准、不批准
        '''
        # self.logout_fir_and_login(data["applicant"])
        self.overtime_application_not_tips(data["UserTel"], data["startDate"], data["starttime"],
                                           data["endtime"], data["remark"], data["sleeps"], data["IDcard"])
        self.logout_fir_and_login(data["superior"])
        self.the_fir_for_approved_detail()
        self.logout_fir_and_login(data["supervisor"])
        self.the_fir_for_not_approved_detail()


    @pytest.mark.parametrize("data", get_data("test_HR_reminder_and_approved"))
    def test_HR_reminder_and_approved(self, data):
        '''
        验证HR提醒补充资料且不批准，非輪班人員下班時間加班，輪班人員全時段加班（有tips）
        '''
        self.logout_fir_and_login(data["applicant"])
        self.overtime_application(data["UserTel"],data["startDate"],data["starttime"],
                                           data["endtime"],data["remark"],data["sleeps"],data["IDcard"])
        self.logout_fir_and_login(data["superior"])
        self.the_fir_for_approved_tips_detail()
        self.logout_fir_and_login(data["supervisor"])
        self.the_fir_for_approved_tips_detail()
        self.logout_fir_and_login(data["HR"])
        self.the_fir_reminder_of_supplement_HR()
        self.the_fir_for_approved_HR_tips()

    @pytest.mark.parametrize("data", get_data("test_overtime_application"))
    def test_overtime_application(self, data):
        '''
        验证非-C人員申請加班,工作、休息日、公衆假時間内加班
        '''
        self.overtime_application(data["UserTel"],data["startDate"],data["starttime"],
                                           data["endtime"],data["remark"],data["sleeps"],data["IDcard"])