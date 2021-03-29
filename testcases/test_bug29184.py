import shelve
from common.contants import basepage_dir, test_bug29184_dir
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
    with open(test_bug29184_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Bug29184:


    _setup_datas = get_env()
    _working = _get_working()
    if _working == "port":
        def setup(self):
            '''
            開啓調試端口啓用
            '''
            self.main = Main()

    else:
        def setup(self):
            '''
            非調試端口用
            '''
            self.main = Main()
            # 讀取數據庫
            self.db = shelve.open("overtimeSn")

        def teardown(self):
            '''
            非調試端口啓用
            '''
            self.main.close()
            self.db.close()

    # A申请加班
    @pytest.mark.parametrize("data", get_data("test_overtime_application"))
    def test_overtime_application(self,data):
        '''
        验证非-C人員申請加班,工作、休息日、公衆假時間内加班
        '''
        result = self.main.goto_login(). \
            username(data["username"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]).goto_overtime_application(). \
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]). \
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]). \
            save_click().wait_sleep(data["sleeps"]).click_tips().wait_sleep(data["sleeps"]).edit_IDcard(data["IDcard"]).\
            wait_sleep(2).goto_my_overtime().get_page_title()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_superior_reminder_and_not_approved_not_tips"))
    def test_superior_reminder_and_not_approved_not_tips(self, data):
        '''
        验证申請加班，上级提醒补充资料，上级在详情页中不批准
        '''

        result = self.main.goto_login(). \
            username(data["applicant"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]). goto_overtime_application().\
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]).\
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]).\
            save_click().wait_sleep(data["sleeps"]).edit_IDcard(data["IDcard"]).goto_my_overtime().get_the_fir_overtimeSn().\
            goto_main().logout_for_index().username(data["superior"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]).goto_overtime_approval().\
            goto_pending_for_approval(). goto_approval_detail(self.db["overtimeSn"]). click_reminder_of_supplement().wait_sleep(3).\
            click_not_approved().goto_approved(). get_the_overtimeSn_status(self.db["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_supervisor_reminder_and_not_approved_not_tips"))
    def test_supervisor_reminder_and_not_approved_not_tips(self, data):
        '''
        验证申請加班，主管提醒补充资料，主管详情页批准
        '''

        result = self.main.goto_login(). \
            username(data["applicant"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]). goto_overtime_application().\
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]).\
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]).\
            save_click().wait_sleep(data["sleeps"]).edit_IDcard(data["IDcard"]).goto_my_overtime().get_the_fir_overtimeSn().\
            goto_main().logout_for_index().username(data["superior"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]).goto_overtime_approval().\
            goto_pending_for_approval(). goto_approval_detail(self.db["overtimeSn"]). click_approved().goto_pending_for_approval().\
            goto_main().logout_for_index().username(data["supervisor"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]).goto_overtime_approval(). \
            goto_pending_for_approval().goto_approval_detail(
            self.db["overtimeSn"]).click_reminder_of_supplement().wait_sleep(3). \
            click_approved().goto_approved(). get_the_overtimeSn_status(self.db["overtimeSn"])
        assert result == data["expect"]


    @pytest.mark.parametrize("data", get_data("test_HR_reminder_and_not_approved_not_tips"))
    def test_HR_reminder_and_not_approved_not_tips(self, data):
        '''
        验证申請加班，HR提醒补充资料，HR详情页批准
        '''

        result = self.main.goto_login(). \
            username(data["applicant"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]). goto_overtime_application().\
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]).\
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]).\
            save_click().wait_sleep(data["sleeps"]).edit_IDcard(data["IDcard"]).goto_my_overtime().get_the_fir_overtimeSn().\
            goto_main().logout_for_index().username(data["superior"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]).goto_overtime_approval().\
            goto_pending_for_approval(). goto_approval_detail(self.db["overtimeSn"]). click_approved().goto_pending_for_approval().\
            goto_main().wait_sleep(3).logout_for_index().username(data["supervisor"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]).goto_overtime_approval(). \
            goto_pending_for_approval().goto_approval_detail(self.db["overtimeSn"]).click_approved().goto_pending_for_approval(). \
            goto_main().wait_sleep(3).logout_for_index().username(data["HR"]).password(self._setup_datas[0]["password"]).save(). \
            goto_application().goto_overtime(data["application"]).goto_overtime_approval(). \
            goto_pending_for_approval_HR().goto_approval_detail_HR(self.db["overtimeSn"]).click_reminder_of_supplement_HR().wait_sleep(3). \
            click_approved_HR().goto_approved_HR(). get_the_overtimeSn_status_HR(self.db["overtimeSn"])
        assert result == data["expect"]



