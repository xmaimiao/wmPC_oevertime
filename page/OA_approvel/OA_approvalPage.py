from common.contants import OA_approvalPage_dir
from page.OA_approvel.all_approvals.all_approvals import ALL_Approvals
from page.OA_approvel.overtime_approvals.overtime_approvals import Overtime_Approvals
from page.basepage import BasePage


class OA_Approval(BasePage):

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

