import shelve
from common.contants import basepage_dir, test_approval_dir
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

class Test_Approval:

    with open(test_approval_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_overtime_application_datas = datas["test_overtime_application"]
        test_reminder_of_supplement_B_datas = datas["test_reminder_of_supplement_B"]
        test_reminder_of_supplement_C_datas = datas["test_reminder_of_supplement_C"]
        test_the_overtimeSn_for_approved_datas = datas["test_the_overtimeSn_for_approved"]
        test_the_overtimeSn_for_not_approved_datas = datas["test_the_overtimeSn_for_not_approved"]
        test_applicator_the_fir_status_datas = datas["test_applicator_the_fir_status"]
        test_upload_supplementary_meterials_1_datas = datas["test_upload_supplementary_meterials_1"]
        test_upload_supplementary_meterials_datas = datas["test_upload_supplementary_meterials"]
        test_get_the_news_datas = datas["test_get_the_news"]
        test_goto_overtime_for_news_datas = datas["test_goto_overtime_for_news"]

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
    @pytest.mark.parametrize("data", test_overtime_application_datas)
    def test_overtime_application(self, data):
        '''
        验证申請加班
        '''
        result = self.main. \
            goto_login(). \
            username(data["username"]).password(self._setup_datas["password"]).save(). \
            goto_application(). \
            goto_overtime(data["application"]). \
            goto_overtime_application(). \
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]). \
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]). \
            save_click().wait_sleep(data["sleeps"]).edit_IDcard(data["IDcard"]).get_the_fir_overtimeSn().get_page_title()
        assert result == data["expect"]

    # B提醒补充资料
    @pytest.mark.parametrize("data", test_reminder_of_supplement_B_datas)
    def test_reminder_of_supplement_B(self, data):
        '''
        根據加班單號進行补充资料提醒操作
        '''

        result = self.main. \
            goto_login(). \
            username(data["username"]).password(data["password"]).save(). \
            goto_application(). \
            goto_overtime(data["application"]). \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            goto_approval_detail(self.db["overtimeSn"]). \
            click_reminder_of_supplement().close_poppage().\
            goto_approval_detail(self.db["overtimeSn"]).get_approval_history_action()
        assert result == data["expect"]

    # A补充资料-注意必須在有界面的瀏覽器中才能上傳文件
    @pytest.mark.parametrize("data", test_upload_supplementary_meterials_1_datas)
    def test_upload_supplementary_meterials_1(self,data):
        '''
        验证根据加班单号进行资料补充操作
        '''
        result = self.main. \
            goto_login(). \
            username(data["username"]).password(data["password"]).save(). \
            goto_application(). \
            goto_overtime(data["application"]). \
            goto_my_overtime_records().\
            goto_application_detail(self.db["overtimeSn"]).\
            upload_supplementary_meterials(data["excel_path"]).\
            get_approval_history_action()
        assert result == data["expect"]

    # B审批通过
    @pytest.mark.parametrize("data", test_the_overtimeSn_for_approved_datas)
    def test_the_overtimeSn_for_approved(self,data):
        '''
        根據加班單號進行審批：審批通過
        :return:
        '''
        result = self.main. \
            goto_login(). \
            username(data["username"]).password(data["password"]).save(). \
            goto_application(). \
            goto_overtime(data["application"]). \
            goto_overtime_approval().\
            goto_pending_for_approval().\
            the_overtimeSn_for_approved(self.db["overtimeSn"]). \
            goto_approved().\
            get_the_overtimeSn_status(self.db["overtimeSn"])
        assert result == data["expect"]

    # C提醒补充资料
    @pytest.mark.parametrize("data", test_reminder_of_supplement_C_datas)
    def test_reminder_of_supplement_C(self, data):
        '''
        根據加班單號進行补充资料提醒操作
        '''
        result = self.main. \
            goto_login(). \
            username(data["username"]).password(data["password"]).save(). \
            goto_application(). \
            goto_overtime(data["application"]). \
            goto_overtime_approval(). \
            goto_pending_for_approval(). \
            goto_approval_detail(self.db["overtimeSn"]). \
            click_reminder_of_supplement().close_poppage().\
            goto_approval_detail(self.db["overtimeSn"]).get_approval_history_action()
        assert result == data["expect"]

    # A补充资料-注意必須在有界面的瀏覽器中才能上傳文件
    @pytest.mark.parametrize("data", test_upload_supplementary_meterials_datas)
    def test_upload_supplementary_meterials(self,data):
        '''
        验证根据加班单号进行资料补充操作
        '''
        result = self.main. \
            goto_login(). \
            username(data["username"]).password(data["password"]).save(). \
            goto_application(). \
            goto_overtime(data["application"]). \
            goto_my_overtime_records().\
            goto_application_detail(self.db["overtimeSn"]).\
            upload_supplementary_meterials(data["excel_path"]).\
            get_approval_history_action()
        assert result == data["expect"]

    # C审批不通过
    @pytest.mark.parametrize("data", test_the_overtimeSn_for_not_approved_datas)
    def test_the_overtimeSn_for_not_approved(self,data):
        '''
        根據加班單號進行審批：審批不批准
        '''
        result = self.main. \
            goto_login(). \
            username(data["username"]).password(data["password"]).save(). \
            goto_application(). \
            goto_overtime(data["application"]). \
            goto_overtime_approval().\
            goto_pending_for_approval().\
            the_overtimeSn_for_not_approved(self.db["overtimeSn"]).\
            goto_approved().\
            get_the_overtimeSn_status(self.db["overtimeSn"])
        assert result == data["expect"]

    # A查看申请状态
    @pytest.mark.parametrize("data", test_applicator_the_fir_status_datas)
    def test_applicator_the_fir_status(self,data):
        '''
        驗證申請人第一單的狀態為：批准/不批准，其他
        '''
        result = self.main. \
            goto_login(). \
            username(data["username"]).password(data["password"]).save(). \
            goto_application(). \
            goto_overtime(data["application"]).\
            goto_my_overtime_records().get_the_fir_status(self.db["overtimeSn"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_get_the_news_datas)
    def test_get_the_news(self, data):
        '''
        验证從首頁-系統消息獲取消息文本
        '''
        results = self.main.goto_login(). \
            username(data["username"]).password(data["password"]).save(). \
            get_news(data["new_num"])
        # 驗證返回的消息數組正確
        i = 0
        for result in results:
            pytest.assume(data["expect" + str(i)] in result)
            i += 1

    @pytest.mark.parametrize("data", test_goto_overtime_for_news_datas)
    def test_goto_overtime_for_news(self, data):
        '''
        验证從首頁-系統消息打開加班應用
        '''
        result = self.main.goto_login(). \
            username(data["username"]).password(data["password"]).save(). \
            goto_overtime_for_news(data["new_num"])
        assert result == data["expect"]