import yaml
from common.contants import main1_dir, basepage_dir, overtimePage_dir, index_dir, OA_approvalPage_dir
from page.OA_approvel.OA_approvalPage import OA_Approval
from page.OA_approvel.all_approvals.all_approvals import ALL_Approvals
from page.OA_approvel.overtime_approvals.overtime_approvals import Overtime_Approvals
from page.basepage import BasePage, _get_working
from page.index import Index
from page.loginpage import Login

class Main(BasePage):
    '''
    首頁面po
    '''
    _working = _get_working()

    with open(basepage_dir, encoding="utf-8") as f:
        env = yaml.safe_load(f)
        if _working != "port":
            _base_url = env["docker_env"][env["default"]]

    def goto_login(self):
        '''
        進去登錄頁面
        :return:
        '''
        return Login(self._driver)

    def goto_index(self):
        '''
        在應用中打開打開首頁
        '''
        self.step(main1_dir,"goto_index")
        return Index(self._driver)


    def goto_OA_Approval(self):
        '''
        在XX應用中進入OA審批
        '''
        self.step(main1_dir,"goto_OA_Approval")
        return OA_Approval(self._driver)

    def goto_overtime_application(self):
        '''
        打開”加班申請“頁面
        '''
        self.step(overtimePage_dir,"goto_overtime_application")
        from page.overtimePage.overtime_application.overtime_application import Overtime_Application
        return Overtime_Application(self._driver)

    def goto_my_overtime_records(self):
        '''
        打開”我的加班“頁面
        '''
        self.step(overtimePage_dir,"goto_my_overtime_records")
        from page.overtimePage.my_overtime_records.my_overtime import My_Overtime
        return My_Overtime(self._driver)

    def goto_overtime_approval(self):
        '''
        打開”加班審批“頁面
        '''
        self.step(overtimePage_dir, "goto_overtime_approval")
        from page.overtimePage.overtime_approval.overtime_approval import Overtime_Approval
        return Overtime_Approval(self._driver)

    def goto_overtime_approval_for_HR(self):
        '''
        打開”加班審批HR“頁面
        '''
        self.step(overtimePage_dir,"goto_overtime_approvalfor_HR")
        from page.overtimePage.overtime_approval_for_HR.overtime_approval_for_HR import Overtime_Approval_For_HR
        return Overtime_Approval_For_HR(self._driver)

    def goto_approval_settings(self):
        '''
        打開”審批设置“頁面
        '''
        self.step(overtimePage_dir,"goto_approval_settings")
        from page.overtimePage.approval_settings.approval_settings import Approval_Settings
        return Approval_Settings(self._driver)

    def goto_news_list(self):
        '''
        在首页打开消息中心列表
        '''
        self.step(index_dir,"goto_news_list")
        from page.news_list.news_list import News_List
        return News_List(self._driver)

    def goto_news_list_in_application(self):
        '''
        在应用中打开消息中心列表
        '''
        self.step(main1_dir,"goto_news_list_in_application")
        from page.news_list.news_list import News_List
        return News_List(self._driver)

    def goto_OA_approval(self):
        '''
        在首页中心打开OA审批
        '''
        self.step(index_dir,"goto_OA_approval")
        return OA_Approval(self._driver)

    def goto_ALL_approvals(self):
        '''
        打開全部審批菜單
        '''
        self.step(OA_approvalPage_dir,"goto_ALL_approvals")
        return ALL_Approvals(self._driver)

    def goto_Overtime_approvals(self):
        '''
        打開加班審批菜單
        '''
        self.step(OA_approvalPage_dir,"goto_Overtime_approvals")
        return Overtime_Approvals(self._driver)

    def get_news(self,new_numlist):
        '''
        根據傳進來的序號獲取第N條消息文本text
        :param num: 序號
        '''
        news_liat =[]
        try:
            for new_num in new_numlist:
                self._params["new_num"] = new_num
                text = self.step(index_dir,"get_news")
                news_liat.append(text)
                print(f"獲取到的消息是：{text}")
            return news_liat
        except Exception as e:
            raise e

    def goto_overtime_for_news(self,new_num):
        '''
        根據傳進來的序號獲取第N條消息並點擊進入改應用
        驗證進入了加班應用，返回”加班詳情“text
        '''
        self._params["new_num"] = new_num
        # 點擊第N條信息
        self.step(index_dir, "goto_overtime_for_news")
        all_pages = self._driver.window_handles  # 获得所有窗口句柄
        self._driver.switch_to.window(all_pages[-1])  # 切换至最后一个窗口
        return (self.step(index_dir,"get_overtime_title")).text

