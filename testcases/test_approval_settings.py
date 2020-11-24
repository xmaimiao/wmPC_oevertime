from common.contants import basepage_dir,test_approval_settings_dir
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

class Test_Approval_Settings:

    with open(test_approval_settings_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_the_fir_approval_datas = datas["test_the_fir_approval"]
        test_edit_the_fir_approval_datas = datas["test_edit_the_fir_approval"]
        test_edit_the_sec_approval_datas = datas["test_edit_the_sec_approval"]
        test_del_the_fir_approval_datas = datas["test_del_the_fir_approval"]

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
                username(self._setup_datas["username"]).password(self._setup_datas["password"]).save(). \
                goto_application(). \
                goto_overtime(self._setup_datas["application"])

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data", test_the_fir_approval_datas)
    def test_the_fir_approval(self, data):
        '''
        验证xxx账号的审批流是 未配置 或其他
        '''
        result = self.main.goto_approval_settings().\
            search_user(data["user"]).\
            get_the_first_approval_process()
        assert result == True

    @pytest.mark.parametrize("data", test_edit_the_fir_approval_datas)
    def test_edit_the_fir_approval(self,data):
        '''
        验证编辑1级审批流，注意此用例中审批流不可重复
        '''
        result = self.main.goto_approval_settings().\
            search_user(data["user"]).\
            edit_the_first_approval_process(data["approvals"],data["action"]).\
            edit_the_fir_approval(data["approvals"][0]).save_click().\
            search_user(data["user"]).wait_sleep(data["sleeps"]).get_the_first_approval_process()
        assert result in data["expect"]

    @pytest.mark.parametrize("data", test_edit_the_sec_approval_datas)
    def test_edit_the_sec_approval(self,data):
        '''
        验证编辑2级审批流，注意：
        1）此用例中审批流不可重复
        2）已有1级审批流存在
        '''
        result = self.main.goto_approval_settings().\
            search_user(data["user"]).\
            edit_the_first_approval_process(data["approvals"],data["action"]).\
            edit_the_sec_approval(data["approvals"][0]).save_click().\
            search_user(data["user"]).wait_sleep(data["sleeps"]).get_the_first_approval_process()
        assert result in data["expect"]

    @pytest.mark.parametrize("data", test_del_the_fir_approval_datas)
    def test_del_the_fir_approval(self,data):
        '''
        验证删除1级审批流
        '''
        result = self.main.goto_approval_settings().\
            search_user(data["user"]).\
            edit_the_first_approval_process(data["approvals"]).\
            del_the_fir_approval().save_click(). \
            search_user(data["user"]).wait_sleep(data["sleeps"]).\
            get_the_first_approval_process_T()
        assert result in data["expect"]
