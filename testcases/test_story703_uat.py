from common.contants import basepage_dir,test_story703_uat_dir
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
    with open(test_story703_uat_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Story703_Uat:

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

    @pytest.mark.parametrize("data", get_data("test_get_IDcard"))
    def test_get_IDcard(self, data):
        '''
        验证獲取ID編號
        '''
        # 申請加班成功
        result = self.main.goto_overtime_application().\
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]).\
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]).\
            save_click().wait_sleep(data["sleeps"]).edit_IDcard(data["IDcard"]).get_page_title()
        assert result == data["expect"]
        # 獲取上一單ID編號
        result = self.main.goto_overtime_application().\
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]).\
            edit_starttime(data["starttime2"]).edit_endtime(data["endtime2"]).edit_remark(data["remark"]).\
            save_click().wait_sleep(data["sleeps"]).get_IDcard()
        assert result == data["IDcard"]
        # 撤銷第一行加班申請
        result = self.main.goto_my_overtime_records().\
            the_first_overtime_cancel()
        assert result == "已撤銷"

    @pytest.mark.parametrize("data", get_data("test_overtime_application_C"))
    def test_overtime_application_C(self, data):
        '''
        验证申請加班
        '''
        result = self.main.goto_overtime_application(). \
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]). \
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]). \
            save_click().wait_sleep(data["sleeps"]).edit_IDcard(data["IDcard"]).goto_my_overtime().get_page_title()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_overtime_application"))
    def test_overtime_application(self, data):
        '''
        验证非-C人員申請加班
        '''
        result = self.main.goto_overtime_application(). \
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]). \
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]). \
            save_click().click_tips().wait_sleep(data["sleeps"]).edit_IDcard(
            data["IDcard"]).goto_my_overtime().get_page_title()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_overtime_application_get_tips"))
    def test_overtime_application_get_tips(self, data):
        '''
        验证非-C人員申請加班,獲取溫馨提示
        '''
        result = self.main.goto_overtime_application(). \
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]). \
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]). \
            save_click().get_tips()
        assert result == True
