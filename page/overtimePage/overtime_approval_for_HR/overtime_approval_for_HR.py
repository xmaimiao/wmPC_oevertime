from common.contants import overtime_approval_for_HR_dir
from page.basepage import BasePage
from page.overtimePage.overtime_approval_for_HR.approved_HR import Approved_HR
from page.overtimePage.overtime_approval_for_HR.pending_for_approval_HR import Pending_For_Approval_HR


class Overtime_Approval_For_HR(BasePage):
    def goto_pending_for_approval_HR(self):
        '''
        打開待審批頁面
        '''
        self.step(overtime_approval_for_HR_dir,"goto_pending_for_approval_HR")
        return Pending_For_Approval_HR(self._driver)

    def goto_approved_HR(self):
        '''
        打開待審批頁面
        '''
        self.step(overtime_approval_for_HR_dir,"goto_approved_HR")
        return Approved_HR(self._driver)
