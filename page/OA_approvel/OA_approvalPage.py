from common.contants import OA_approvalPage_dir
from page.OA_approvel.all_approvals import ALL_Approvals
from page.basepage import BasePage


class OA_Approval(BasePage):

    def goto_ALL_approvals(self):
        '''
        打開全部審批菜單
        '''
        self.step(OA_approvalPage_dir,"goto_ALL_approvals")
        return ALL_Approvals(self._driver)

