from common.contants import overtime_approvals_dir
from page.OA_approvel.overtime_approvals.approved_OA_Overtime import Approved_OA_Overtime
from page.OA_approvel.overtime_approvals.pending_for_approval_OA_Overtime import Pending_For_Approval_OA_Overtime
from page.basepage import BasePage


class Overtime_Approvals(BasePage):

    def goto_pending_for_approval_OA_Overtime(self):
        '''
        打開待審批頁面
        '''
        self.step(overtime_approvals_dir,"goto_pending_for_approval_OA_Overtime")
        return Pending_For_Approval_OA_Overtime(self._driver)

    def goto_approved_OA_Overtime(self):
        '''
        打開已審批頁面
        '''
        self.step(overtime_approvals_dir,"goto_approved_OA_Overtime")
        return Approved_OA_Overtime(self._driver)