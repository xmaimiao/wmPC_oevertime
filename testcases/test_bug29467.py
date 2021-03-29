import shelve

from common.contants import basepage_dir, test_bug29467_dir
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
    with open(test_bug29467_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Bug29467:

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
        result = self.main.logout_for_fir(). \
            username(data).password(self._setup_datas[0]["password"]).save(). \
            get_index_ele_fir()
        assert "首頁" in result


    def overtime_application_not_tips(self,UserTel,startDate,starttime,endtime,remark,sleeps,IDcard):
        result = self.main.goto_overtime_application(). \
            edit_UserTel(UserTel).edit_startDate(startDate). \
            edit_starttime(starttime).edit_endtime(endtime).edit_remark(remark). \
            save_click().wait_sleep(sleeps).edit_IDcard(IDcard).\
            goto_my_overtime().get_the_fir_overtimeSn().get_page_title()
        assert result == True

    def approved_OA_ALL_not_tips(self):
        '''
        验证OA审批-all批准
        '''
        db=shelve.open("overtimeSn")
        result = self.main.goto_ALL_approvals().\
            goto_pending_for_approval_OA_ALL().\
            goto_details_of_overtimeSn_OA_ALL(db["overtimeSn"]).\
            approved_OA_ALL().\
            goto_approved_OA_ALL().get_the_status_of_overtimeSn(db["overtimeSn"])
        db.close()
        assert result == "批准"

    def the_fir_approved_OA_Overtime_not_tips(self):
        '''
        验证OA-加班审批批准,第一行数据,not_tips
        '''
        db = shelve.open("overtimeSn")
        result = self.main. \
            goto_Overtime_approvals().goto_pending_for_approval_OA_Overtime(). \
            goto_details_of_overtimeSn_OA_Overtime(db["overtimeSn"]). \
            approved_OA_Overtime(). \
            goto_approved_OA_Overtime().get_the_status_of_overtimeSn(db["overtimeSn"])
        db.close()
        assert result == "批准"

    def the_fir_approved_OA_Overtime_not_tips_HR(self):
        '''
        验证OA-加班审批（HR)批准,第一行数据,not_tips
        '''
        db = shelve.open("overtimeSn")
        result = self.main. \
            goto_Overtime_approvals_HR().goto_pending_for_approval_OA_Overtime_HR(). \
            goto_details_of_overtimeSn_OA_Overtime_HR(db["overtimeSn"]). \
            approved_OA_Overtime_HR(). \
            goto_approved_OA_Overtime_HR().get_the_status_of_overtimeSn_HR(db["overtimeSn"])
        db.close()
        assert result == "批准"

    def logout_oa_and_login(self,data):
        '''在OA审批/一期应用中退出，并登录账号打开OA审批'''
        result = self.main.logout_for_fir(). \
            username(data).password(self._setup_datas[0]["password"]).save(). \
            goto_OA_approval().get_ele_of_ALL_approvals_OA()
        assert True == result

    def my_overtime_to_OA(self):
        '''在加班应用打开OA审批'''
        result = self.main.goto_my_overtime_records(). \
            wait_sleep(2).goto_main().goto_OA_Approval().get_ele_of_ALL_approvals_OA()
        assert True == result

    def OA_to_my_overtime(self,application):
        '''在OA审批打开加班应用'''
        result = self.main.goto_index(). \
            goto_application().goto_overtime(application).goto_my_overtime_records().get_page_title()
        assert True == result


    # OA全部审批-获取加班单号
    def get_the_fir_applicant_OA_ALL(self,applicant):
        result = self.main.goto_ALL_approvals().\
            goto_pending_for_approval_OA_ALL().wait_sleep(1).get_the_fir_applicant_OA_ALL()
        assert applicant == result

    # OA加班审批-获取加班单号
    def get_the_fir_applicant_OA_Overtime(self,applicant):
        result = self.main.goto_Overtime_approvals(). \
            goto_pending_for_approval_OA_Overtime().wait_sleep(1).get_the_fir_applicant_OA_Overtime()
        assert applicant == result

    # OA加班审批(HR)-获取加班单号
    def get_the_fir_applicant_OA_Overtime_HR(self,applicant):
        result = self.main.goto_Overtime_approvals_HR(). \
            goto_pending_for_approval_OA_Overtime_HR().wait_sleep(1).get_the_fir_applicant_OA_Overtime_HR()
        assert applicant == result

    # port调试端口用例

    # OA全部审批
    @pytest.mark.parametrize("data", get_data("test_overtime_application_not_tips_ALL"))
    def test_overtime_application_not_tips_ALL(self, data):
        '''
        验证申請加班，非輪班人員下班時間加班，輪班人員全時段加班
        上级、主管、HR在OA中审批，申请人不变
        '''
        # self.logout_fir_and_login(data["applicant"])
        # self.overtime_application_not_tips(data["UserTel"], data["startDate"], data["starttime"],
        #                           data["endtime"], data["remark"], data["sleeps"], data["IDcard"])
        # self.logout_fir_and_login(data["superior"])
        # self.my_overtime_to_OA()
        # self.get_the_fir_applicant_OA_ALL(data["applicant_zh"])
        # self.the_fir_approved_OA_Overtime_not_tips()
        self.logout_oa_and_login(data["supervisor"])
        self.get_the_fir_applicant_OA_ALL(data["applicant_zh"])
        self.the_fir_approved_OA_Overtime_not_tips()
        self.logout_oa_and_login(data["HR"])


        # self.get_the_fir_applicant_OA_ALL(data["applicant_zh"])
        # self.approved_OA_ALL_not_tips()
        # self.OA_to_my_overtime(data["application"])

    # 用于加班自己审批流
    @pytest.mark.parametrize("data", get_data("test_overtime_application_not_tips_ALL"))
    def test_overtime_application_not_tips_ALL(self, data):
        '''
        验证申請加班，非輪班人員下班時間加班，輪班人員全時段加班
        上级、主管、HR在OA中审批，申请人不变
        '''
        self.logout_fir_and_login(data["applicant"])
        self.overtime_application_not_tips(data["UserTel"], data["startDate"], data["starttime"],
                                  data["endtime"], data["remark"], data["sleeps"], data["IDcard"])
        self.logout_fir_and_login(data["superior"])
        self.my_overtime_to_OA()
        self.get_the_fir_applicant_OA_ALL(data["applicant_zh"])
        self.the_fir_approved_OA_Overtime_not_tips()
        self.logout_oa_and_login(data["supervisor"])
        self.get_the_fir_applicant_OA_ALL(data["applicant_zh"])
        self.the_fir_approved_OA_Overtime_not_tips()
        self.OA_to_my_overtime(data["application"])

#     OA加班审批/加班审批（HR）
    @pytest.mark.parametrize("data", get_data("test_overtime_application_not_tips"))
    def test_overtime_application_not_tips(self, data):
        '''
        验证申請加班，非輪班人員下班時間加班，輪班人員全時段加班
        上级、主管、HR在OA中审批，申请人不变
        '''
        self.logout_fir_and_login(data["applicant"])
        self.overtime_application_not_tips(data["UserTel"], data["startDate"], data["starttime"],
                                  data["endtime"], data["remark"], data["sleeps"], data["IDcard"])
        self.logout_fir_and_login(data["superior"])
        self.my_overtime_to_OA()
        self.get_the_fir_applicant_OA_Overtime(data["applicant_zh"])
        self.approved_OA_ALL_not_tips()
        self.logout_oa_and_login(data["supervisor"])
        self.get_the_fir_applicant_OA_Overtime(data["applicant_zh"])
        self.approved_OA_ALL_not_tips()
        self.logout_oa_and_login(data["HR"])
        self.get_the_fir_applicant_OA_Overtime_HR(data["applicant_zh"])
        self.the_fir_approved_OA_Overtime_not_tips_HR()
        self.OA_to_my_overtime(data["application"])


