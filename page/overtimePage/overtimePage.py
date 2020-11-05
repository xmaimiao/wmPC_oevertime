from common.contants import overtimePage_dir
from page.basepage import BasePage
from page.overtimePage.my_overtime_records.my_overtime import My_Overtime
from page.overtimePage.overtime_application.overtime_application import Overtime_Application


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


