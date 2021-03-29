from common.contants import pending_for_approval_HR_dir, overtime_approval_for_HR_dir
from page.basepage import BasePage
from page.overtimePage.overtime_approval_for_HR.application_HR import Application_HR
from page.overtimePage.overtime_approval_for_HR.approved_HR import Approved_HR


class Pending_For_Approval_HR(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def the_overtimeSn_for_approved_HR(self, overtimeSn):
        '''
        1.通過加班單號去 批准 該申請
        :param overtimeSn: 加班單號
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_HR_dir, "the_overtimeSn_for_approved_HR")
        return self

    def the_fir_for_approved_HR(self):
        '''
        1. 批准 第一行申請
        '''
        self.step(pending_for_approval_HR_dir, "the_fir_for_approved_HR")
        return self

    def click_tips_confirm_HR(self):
        '''
        批准，點擊加班時間屬於 辦公時間 彈出的溫馨提示
        '''
        self.step(pending_for_approval_HR_dir, "click_tips_confirm_HR")
        return self

    def the_overtimeSn_for_not_approved_HR(self, overtimeSn):
        '''
        1.通過加班單號去 不批准 該申請
        :param overtimeSn: 加班單號
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_HR_dir, "the_overtimeSn_for_not_approved_HR")
        return self

    def the_fir_for_not_approved_HR(self):
        '''
        1. 不批准 第一行申請
        '''
        self.step(pending_for_approval_HR_dir, "the_fir_for_not_approved_HR")
        return self

    def goto_approved_HR(self):
        '''
        打開已審批頁面
        '''
        self.step(overtime_approval_for_HR_dir,"goto_approved_HR")
        return Approved_HR(self._driver)

    def goto_the_fir_approval_detail_HR(self):
        '''
        打开第一行待审批详情页
        '''
        self.step(pending_for_approval_HR_dir, "goto_the_fir_approval_detail_HR")
        from page.overtimePage.overtime_approval_for_HR.approval_detail_HR import Approval_Detail_HR
        return Approval_Detail_HR(self._driver)


    def goto_application_HR(self):
        '''
        打開代加班頁面-》录入申请
        '''
        self.step(pending_for_approval_HR_dir,"goto_application_HR")
        return Application_HR(self._driver)

    def get_ele_of_application(self):
        '''
        获取“录取申请”元素，验证代申请成功
        '''
        try:
            self.step(pending_for_approval_HR_dir, "get_ele_of_application")
            return True
        except Exception as e:
            return False

    def batch_agree_HR(self):
        '''
        批量批准
        '''
        self.step(pending_for_approval_HR_dir,"batch_agree_HR")
        return Application_HR(self._driver)