from common.contants import overtime_approval_dir
from page.basepage import BasePage
from page.overtimePage.overtime_approval.approved import Approved
from page.overtimePage.overtime_approval.pending_for_approval import Pending_For_Approval


class Overtime_Approval(BasePage):

    def goto_pending_for_approval(self):
        '''
        打開待審批頁面
        '''
        # self.step(overtime_approval_dir,"goto_pending_for_approval")
        return Pending_For_Approval(self._driver)

    def goto_approved(self):
        '''
        打開已審批頁面
        '''
        self.step(overtime_approval_dir,"goto_approved")
        return Approved(self._driver)