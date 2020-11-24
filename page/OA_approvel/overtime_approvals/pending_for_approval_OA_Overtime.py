from common.contants import pending_for_approval_OA_Overtime_dir
from page.OA_approvel.overtime_approvals.details_of_overtimeSn_OA_Overtime import Details_Of_OvertimeSn_OA_Overtime
from page.basepage import BasePage


class Pending_For_Approval_OA_Overtime(BasePage):
    def goto_details_of_overtimeSn_OA_Overtime(self,overtimeSn):
        '''
        根据“加班单号”打开加班详情页面
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_OA_Overtime_dir,"goto_details_of_overtimeSn_OA_Overtime")
        return Details_Of_OvertimeSn_OA_Overtime(self._driver)