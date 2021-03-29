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
    with open(test_approval_settings_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas
    
class Test_Approval_Settings:

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

    @pytest.mark.parametrize("data", get_data("test_the_fir_approval"))
    def test_the_fir_approval(self, data):
        '''
        验证xxx账号的审批流是 未配置 或其他
        '''
        result = self.main.goto_approval_settings().\
            search_user(data["user"]).\
            get_the_first_approval_process()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_edit_the_fir_approval"))
    def test_edit_the_fir_approval(self,data):
        '''
        验证编辑1级审批流，注意此用例中审批流不可重复
        '''
        result = self.main.goto_approval_settings().\
            search_user(data["user"]).\
            edit_the_first_approval_process(data["approvals"],data["action"]).\
            edit_the_fir_approval(data["approvals"][0]).save_click().\
            search_user(data["user"]).wait_sleep(data["sleeps"]).get_the_first_approval_process()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_edit_the_sec_approval"))
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
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_del_the_fir_approval"))
    def test_del_the_fir_approval(self,data):
        '''
        验证删除1级审批流
        '''
        result = self.main.goto_approval_settings().\
            search_user(data["user"]).\
            edit_the_first_approval_process(data["approvals"]).\
            del_the_fir_approval().save_click(). \
            search_user(data["user"]).wait_sleep(1).\
            get_the_first_approval_process_T()
        assert result == True


    def test_get_approval_group(self):
        '''
        验证獲取審批組和其審批人員
        '''
        result = self.main.goto_approval_settings().\
            goto_approval_group_setting().get_approval_group_all()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_del_and_add_approval_group_members"))
    def test_del_and_add_approval_group_members(self,data):
        '''
        验证刪除審批組中的全部人員，再添加新人員
        '''
        result = self.main.goto_approval_settings().\
            goto_approval_group_setting().edit_group_for_name(data["group_name"]).\
            del_group_members().edit_group_members(data["members"]).\
            click_save().wait_sleep(1).get_members_for_group_name(data["group_name"])
        for member in data["members"]:
            assert member in result

    @pytest.mark.parametrize("data", get_data("test_add_approval_group_members"))
    def test_add_approval_group_members(self,data):
        '''
        验证刪除審批組中的全部人員，再添加新人員
        '''
        result = self.main.goto_approval_settings().\
            goto_approval_group_setting().edit_group_for_name(data["group_name"]).\
            edit_group_members(data["members"]).click_save().\
            wait_sleep(1).get_members_for_group_name(data["group_name"])
        for member in data["members"]:
            assert member in result


