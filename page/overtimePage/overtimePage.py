from common.contants import overtimePage_dir
from page.basepage import BasePage
from page.overtimePage.approval_settings.approval_settings import Approval_Settings
from page.overtimePage.my_overtime_records.my_overtime import My_Overtime
from page.overtimePage.overtime_application.overtime_application import Overtime_Application
from page.overtimePage.overtime_approval.overtime_approval import Overtime_Approval
from page.overtimePage.overtime_approval_for_HR.overtime_approval_for_HR import Overtime_Approval_For_HR


class OvertimePage(BasePage):
    def goto_my_overtime_records(self):
        '''
        打開”我的加班“頁面
        '''
        self.step(overtimePage_dir,"goto_my_overtime_records")
        return My_Overtime(self._driver)

    def goto_overtime_application(self):
        '''
        打開”加班申請“頁面
        '''
        self.step(overtimePage_dir,"goto_overtime_application")
        return Overtime_Application(self._driver)

    def goto_overtime_approval(self):
        '''
        打開”加班審批“頁面
        '''
        self.step(overtimePage_dir,"goto_overtime_approval")
        return Overtime_Approval(self._driver)

    def goto_overtime_approval_for_HR(self):
        '''
        打開”加班審批HR“頁面
        '''
        self.step(overtimePage_dir,"goto_overtime_approval_for_HR")
        return Overtime_Approval_For_HR(self._driver)

    def goto_approval_settings(self):
        '''
        打開”審批设置“頁面
        '''
        self.step(overtimePage_dir,"goto_approval_settings")
        return Approval_Settings(self._driver)

