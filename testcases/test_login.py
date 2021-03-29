import re

import pytest
from common.contants import basepage_dir
from page.basepage import _get_working
from page.main import Main

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
class Test_Login:

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

    def logout_fir_and_login(self,data):
        result = self.main.logout_for_fir(). \
            username(data).password(self._setup_datas[0]["password"]).save(). \
            get_index_ele_fir()
        assert "首頁" in result

    def logout_oa_and_login(self,data):
        '''在OA审批中退出，并登录账号打开OA审批'''
        result = self.main.logout_for_fir(). \
            username(data).password(self._setup_datas[0]["password"]).save(). \
            goto_OA_approval().get_ele_of_ALL_approvals_OA()
        assert True == result

    def logout_sec_and_login(self,data):
        result = self.main.logout_for_sec(). \
            username(data).password(self._setup_datas[0]["password"]).save(). \
            get_index_ele_sec()
        assert "首頁" in result

    def test_logout_fir_and_test11(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test11")
    def test_logout_fir_and_test12(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test12")

    def test_logout_fir_and_deke1700(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("deke1700")

    def test_logout_fir_and_deke1704(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("deke1704")

    def test_logout_fir_and_deke1703(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("deke1703")

    def test_logout_fir_and_deke1705(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("deke1705")

    def test_logout_fir_and_deke1706(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("deke1706")

    def test_logout_fir_and_deke1707(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("deke1707")
    def test_logout_fir_and_deke1708(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("deke1708")
    def test_logout_fir_and_deke1709(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("deke1709")
    def test_logout_fir_and_deke1710(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("deke1710")


    # uat

    def test_logout_fir_and_test500(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test500")

    def test_logout_fir_and_test501(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test501")

    def test_logout_fir_and_test502(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test502")

    def test_logout_fir_and_test503(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test503")

    def test_logout_fir_and_test504(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test504")

    def test_logout_fir_and_test401(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test401")

    def test_logout_fir_and_test302(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test302")

    def test_logout_fir_and_test301(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test301")

    # 正式站
    def test_logout_fir_and_test41(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test41-test")

    def test_logout_fir_and_test40(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test40-test")

    def test_logout_fir_and_test39(self):
        '''
        验证一期應用退出登錄
        '''
        self.logout_fir_and_login("test39-test")

    # oa登录 dev

    def test_logout_oa_and_deke1700(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("deke1700")

    def test_logout_oa_and_deke1703(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("deke1703")

    def test_logout_oa_and_deke1704(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("deke1704")

    def test_logout_oa_and_deke1705(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("deke1705")

    def test_logout_oa_and_test302(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("test302")

    def test_logout_oa_and_test303(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("test303")

    # oa登录 uat

    def test_logout_oa_and_test401(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("test401")

    def test_logout_oa_and_test400(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("test400")

    def test_logout_oa_and_test502(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("test502")

    def test_logout_oa_and_test503(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("test503")

    # 正式站
    def test_logout_oa_and_test39(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("test39-test")

    def test_logout_oa_and_test40(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("test40-test")

    def test_logout_oa_and_test41(self):
        '''
        验证OA審批-》退出登錄 -》登录账号-》打开OA审批
        '''
        self.logout_oa_and_login("test41-test")



    # 二期登录dev
    def test_logout_sec_and_deke1700(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1700")
    def test_logout_sec_and_deke1701(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1701")
    def test_logout_sec_and_deke1702(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1702")
    def test_logout_sec_and_deke1703(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1703")
    def test_logout_sec_and_deke1704(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1704")
    def test_logout_sec_and_deke1705(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1705")

    def test_logout_sec_and_deke1706(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1706")

    def test_logout_sec_and_deke1707(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1707")
    def test_logout_sec_and_deke1708(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1708")
    def test_logout_sec_and_deke1709(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1709")
    def test_logout_sec_and_deke1710(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("deke1710")

    def test_logout_sec_and_test12(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("test12")

    def test_logout_sec_and_pyyan(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("pyyan")

#     uat
    def test_logout_sec_and_test400(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("test400")
    def test_logout_sec_and_test401(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("test401")
    def test_logout_sec_and_test402(self):
        '''
        验证二期應用退出登錄
        '''
        self.logout_sec_and_login("test402")



