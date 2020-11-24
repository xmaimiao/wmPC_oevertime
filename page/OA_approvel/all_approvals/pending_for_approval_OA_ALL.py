from common.contants import pending_for_approval_OA_ALL_dir
from page.OA_approvel.all_approvals.details_of_overtimeSn_OA_ALL import Details_Of_OvertimeSn_OA_ALL
from page.basepage import BasePage


class Pending_For_Approval_OA_ALL(BasePage):

    def goto_details_of_overtimeSn_OA_ALL(self,overtimeSn):
        '''
        根据“加班单号”打开加班详情页面
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_OA_ALL_dir,"goto_details_of_overtimeSn_OA_ALL")
        return Details_Of_OvertimeSn_OA_ALL(self._driver)