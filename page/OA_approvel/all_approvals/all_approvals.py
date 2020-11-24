from common.contants import all_approvals_dir
from page.OA_approvel.all_approvals.approved_OA_ALL import Approved_OA_ALL
from page.OA_approvel.all_approvals.pending_for_approval_OA_ALL import Pending_For_Approval_OA_ALL
from page.basepage import BasePage


class ALL_Approvals(BasePage):

    def goto_pending_for_approval_OA_ALL(self):
        '''
        打開待審批頁面
        '''
        self.step(all_approvals_dir,"goto_pending_for_approval_OA_ALL")
        return Pending_For_Approval_OA_ALL(self._driver)

    def goto_approved_OA_ALL(self):
        '''
        打開已審批頁面
        '''
        self.step(all_approvals_dir,"goto_approved_OA_ALL")
        return Approved_OA_ALL(self._driver)