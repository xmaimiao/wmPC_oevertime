from common.contants import pending_for_approval_HR_dir
from page.basepage import BasePage
from page.overtimePage.overtime_approval_for_HR.approved_HR import Approved_HR


class Pending_For_Approval_HR(BasePage):
    def the_overtimeSn_for_approved_HR(self, overtimeSn):
        '''
        1.通過加班單號去 批准 該申請
        :param overtimeSn: 加班單號
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_HR_dir, "the_overtimeSn_for_approved_HR")
        return self

    def the_overtimeSn_for_not_approved_HR(self, overtimeSn):
        '''
        1.通過加班單號去 不批准 該申請
        :param overtimeSn: 加班單號
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_HR_dir, "the_overtimeSn_for_not_approved_HR")
        return self

    def goto_approved_HR(self):
        '''
        打開已審批頁面
        '''
        self.step(pending_for_approval_HR_dir, "goto_approved_HR")
        return Approved_HR(self._driver)