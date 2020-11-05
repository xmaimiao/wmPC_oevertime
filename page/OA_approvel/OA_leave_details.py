from common.contants import OA_leave_details_dir
from page.basepage import BasePage


class OA_Leave_Details(BasePage):
    pass
    # def approved(self):
    #     '''
    #     點擊同意
    #     '''
    #     self.step(OA_leave_details_dir,"approved")
    #     return Pending_For_Approval(self._driver)
    #
    # def not_approved(self):
    #     '''
    #     點擊不同意
    #     '''
    #     self.step(OA_leave_details_dir,"not_approved")
    #     return Pending_For_Approval(self._driver)
    #
    # def remarks(self,remarks):
    #     '''
    #     填寫不批准意見
    #     '''
    #     self._params["remarks"] = remarks
    #     self.step(OA_leave_details_dir,"remarks")
    #     return self