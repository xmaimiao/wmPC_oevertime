from common.contants import basepage_dir, test_news_list_dir
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

class Test_News_List:

    with open(test_news_list_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_get_the_news_datas = datas["test_get_the_news"]
        test_goto_overtime_for_news_datas = datas["test_goto_overtime_for_news"]
        test_get_the_read_news_of_application_datas = datas["test_get_the_read_news_of_application"]

    _setup_datas = get_env()
    _working = _get_working()
    if _working == "port":
        def setup(self):
            '''
            開啓調試端口啓用
            '''
            self.main = Main().goto_index()

    else:
        def setup(self):
            '''
            非調試端口用
            '''
            self.main = Main().goto_login(). \
                username(self._setup_datas["username"]).password(self._setup_datas["password"]).save()

        def teardown(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data", test_get_the_news_datas)
    def test_get_the_news(self, data):
        '''
        验证從首頁-系統消息獲取消息文本
        '''
        result = self.main.get_news(data["new_num"])
        assert result == True

    @pytest.mark.parametrize("data", test_goto_overtime_for_news_datas)
    def test_goto_overtime_for_news(self, data):
        '''
        验证從首頁-系統消息打開加班應用
        '''
        result = self.main.goto_overtime_for_news(data["new_num"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_get_the_read_news_of_application_datas)
    def test_get_the_read_news_of_application(self, data):
        '''
        验证從應用中打開-消息中心-已讀獲取消息文本
        '''
        results = self.main. \
            wait_sleep(1).goto_news_list().\
            goto_read().get_the_news_read(data["new_num"])
        # 驗證返回的消息數組正確
        i = 0
        for result in results:
            pytest.assume(data["expect" + str(i)] in result)
            i += 1