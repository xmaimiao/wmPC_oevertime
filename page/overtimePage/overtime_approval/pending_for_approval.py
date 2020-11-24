from common.contants import pending_for_approval_dir, overtime_approval_dir
from page.basepage import BasePage
from page.overtimePage.overtime_approval.approval_detail import Approval_Detail
from page.overtimePage.overtime_approval.approved import Approved


class Pending_For_Approval(BasePage):
    def the_overtimeSn_for_approved(self, overtimeSn):
        '''
        1.通過加班單號去 批准 該申請
        :param overtimeSn: 加班單號
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_dir, "the_overtimeSn_for_approved")
        return self

    def the_overtimeSn_for_not_approved(self, overtimeSn):
        '''
        1.通過加班單號去 不批准 該申請
        :param overtimeSn: 加班單號
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_dir, "the_overtimeSn_for_not_approved")
        return self

    def goto_approved(self):
        '''
        打開已審批頁面
        '''
        self.step(overtime_approval_dir, "goto_approved")
        return Approved(self._driver)

    def goto_approval_detail(self,overtimeSn):
        '''
        通过加班单号，打开待审批详情页
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_dir, "goto_approval_detail")
        return Approval_Detail(self._driver)
