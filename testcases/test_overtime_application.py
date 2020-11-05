from common.contants import basepage_dir, test_overtime_application_dir
from page.basepage import  _get_working
from page.main import Main
import pytest
import yaml

def get_env():
    '''
    获取环境变量：uat、dev、mo正式站
    '''
    with open(basepage_dir, encoding="utf-8") as f:
        return yaml.safe_load(f)["default"]

class Test_Overtime_Application:
    with open(test_overtime_application_dir, encoding="utf-8") as f:

        datas = yaml.safe_load(f)
        setup_datas = datas[get_env()]
        test_overtime_application_datas = datas["test_overtime_application"]

    _working = _get_working()
    if _working:
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
                username(self.setup_datas["username"]).password(self.setup_datas["password"]).save(). \
                goto_application(). \
                goto_overtime(self.setup_datas["application"])

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data", test_overtime_application_datas)
    def test_overtime_application(self, data):
        '''
        验证HR代请假,result是Html页面，验证正确调整休假审批（HR）-代请假记录页面
        '''
        result = self.main.goto_overtime_application().\
            edit_UserTel(data["UserTel"]).edit_startDate(data["startDate"]).\
            edit_starttime(data["starttime"]).edit_endtime(data["endtime"]).edit_remark(data["remark"]).\
            save_click().edit_IDcard(data["IDcard"]).get_page_title()
        assert result == data["expect"]