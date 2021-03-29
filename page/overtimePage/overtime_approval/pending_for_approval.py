import re

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

    def the_fir_for_approved(self):
        '''
        1. 批准 第一行申請
        '''
        self.step(pending_for_approval_dir, "the_fir_for_approved")
        return self

    def click_tips_confirm(self):
        '''
        批准，點擊加班時間屬於 辦公時間 彈出的溫馨提示
        '''
        self.step(pending_for_approval_dir, "click_tips_confirm")
        return self

    def the_overtimeSn_for_not_approved(self, overtimeSn):
        '''
        1.通過加班單號去 不批准 該申請
        :param overtimeSn: 加班單號
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_dir, "the_overtimeSn_for_not_approved")
        return self

    def the_fir_for_not_approved(self):
        '''
        1. 不批准 第一行申請
        '''
        self.step(pending_for_approval_dir, "the_fir_for_not_approved")
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

    def goto_the_fir_approval_detail(self):
        '''
        打开第一行待审批详情页
        '''
        self.step(pending_for_approval_dir, "goto_the_fir_approval_detail")
        return Approval_Detail(self._driver)

    def check_all(self):
        '''
        勾选 全选
        '''
        self.step(pending_for_approval_dir, "check_all")
        return self

    def batch_agree(self):
        '''
        批量批准
        '''
        get_before_total = self.step(pending_for_approval_dir, "get_total")
        before_total = int(re.search("(\d+).*?(\d+).*", get_before_total).group(1))
        self.step(pending_for_approval_dir, "batch_agree")
        get_after_total = self.step(pending_for_approval_dir, "get_total")
        after_total = int(re.search("(\d+).*?(\d+).*", get_after_total).group(1))
        if before_total > after_total:
            return True
        else:
            return False

    def goto_main(self):
        '''
        用于更换账号跑流程
        '''
        from page.main import Main
        return Main(self._driver)

