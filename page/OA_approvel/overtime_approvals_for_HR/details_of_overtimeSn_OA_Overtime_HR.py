from common.contants import details_of_overtimeSn_OA_Overtime_HR_dir, overtime_approvals_HR_dir
from page.basepage import BasePage

class Details_Of_OvertimeSn_OA_Overtime_HR(BasePage):
    def agree_overtime_work_agreement_HR(self):
        '''
        同意超時工作協議書
        '''
        self.step(details_of_overtimeSn_OA_Overtime_HR_dir,"agree_overtime_work_agreement_HR")
        return self

    def approved_OA_Overtime_HR(self):
        '''
        点击“批准”
        '''
        self.step(details_of_overtimeSn_OA_Overtime_HR_dir,"approved_OA_Overtime_HR")
        return self

    def not_approved_OA_Overtime_HR(self):
        '''
        点击“不批准”
        '''
        self.step(details_of_overtimeSn_OA_Overtime_HR_dir,"not_approved_OA_Overtime_HR")
        return self

    def remark_OA_Overtime_HR(self,remark):
        '''
        点击“不批准”
        '''
        self._params["remark"] = remark
        self.step(details_of_overtimeSn_OA_Overtime_HR_dir,"remark_OA_Overtime_HR")
        return self

    def reminder_of_supplement_OA_Overtime_HR(self):
        '''
        点击“补充资料提醒”
        '''
        self.step(details_of_overtimeSn_OA_Overtime_HR_dir,"reminder_of_supplement_OA_Overtime_HR")
        return self

    def close_details_OA_Overtime_HR(self):
        '''
        点击“关闭详情”按钮
        '''
        self.step(details_of_overtimeSn_OA_Overtime_HR_dir,"close_details_OA_Overtime_HR")
        from page.OA_approvel.overtime_approvals_for_HR.pending_for_approval_OA_Overtime_HR import \
            Pending_For_Approval_OA_Overtime_HR
        return Pending_For_Approval_OA_Overtime_HR(self._driver)

    def get_approval_history_action_HR(self):
        '''
        获取最后一行历史操作文本text
        '''
        history_action = self.step(details_of_overtimeSn_OA_Overtime_HR_dir,"get_approval_history_action_HR").text
        # 弹出的toast会遮挡“X”，需等待3s
        self.sleep(3)
        self.step(details_of_overtimeSn_OA_Overtime_HR_dir,"close_details_OA_Overtime_HR")
        return history_action

    def goto_approved_OA_Overtime_HR(self):
        self.step(overtime_approvals_HR_dir,"goto_approved_OA_Overtime_HR")
        from page.OA_approvel.overtime_approvals_for_HR.approved_OA_Overtime_HR import Approved_OA_Overtime_HR
        return Approved_OA_Overtime_HR(self._driver)
