from common.contants import overtime_approvals_HR_dir
from page.OA_approvel.overtime_approvals_for_HR.approved_OA_Overtime_HR import Approved_OA_Overtime_HR
from page.OA_approvel.overtime_approvals_for_HR.pending_for_approval_OA_Overtime_HR import \
    Pending_For_Approval_OA_Overtime_HR
from page.basepage import BasePage


class Overtime_Approvals_HR(BasePage):

    def goto_pending_for_approval_OA_Overtime_HR(self):
        '''
        打開待審批頁面
        '''
        self.step(overtime_approvals_HR_dir,"goto_pending_for_approval_OA_Overtime_HR")
        return Pending_For_Approval_OA_Overtime_HR(self._driver)

    def goto_approved_OA_Overtime_HR(self):
        '''
        打開已審批頁面
        '''
        self.step(overtime_approvals_HR_dir,"goto_approved_OA_Overtime_HR")
        return Approved_OA_Overtime_HR(self._driver)