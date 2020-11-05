import yaml
from common.contants import main1_dir, basepage_dir, overtimePage_dir
from page.OA_approvel.OA_approvalPage import OA_Approval
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
        打開首頁
        '''
        return Index(self._driver)


    def goto_OA_Approval(self):
        '''
        在請假中進入OA審批
        '''
        self.step(main1_dir,"goto_OA_Approval")
        return OA_Approval(self._driver)


    # def goto_my_overtime(self):
    #     '''
    #     打開”我的加班“頁面
    #     '''
    #     self.step(main1_dir,"goto_OA_Approval")
    #     return My_Overtime(self._driver)

    def goto_overtime_application(self):
        '''
        打開”加班申請“頁面
        '''
        self.step(overtimePage_dir,"goto_overtime_application")
        from page.overtimePage.overtime_application.overtime_application import Overtime_Application
        return Overtime_Application(self._driver)

    def goto_my_overrtime(self):
        '''
        打開”我的加班“頁面
        '''
        self.step(overtimePage_dir,"goto_my_overtime")
        from page.overtimePage.my_overtime_records.my_overtime import My_Overtime
        return My_Overtime(self._driver)

