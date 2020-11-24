from common.contants import details_of_overtimeSn_OA_Overtime_dir, overtime_approvals_dir
from page.basepage import BasePage

class Details_Of_OvertimeSn_OA_Overtime(BasePage):
    def agree_overtime_work_agreement(self):
        '''
        同意超時工作協議書
        '''
        self.step(details_of_overtimeSn_OA_Overtime_dir,"agree_overtime_work_agreement")
        return self

    def approved_OA_Overtime(self):
        '''
        点击“批准”
        '''
        self.step(details_of_overtimeSn_OA_Overtime_dir,"approved_OA_Overtime")
        return self

    def not_approved_OA_Overtime(self):
        '''
        点击“不批准”
        '''
        self.step(details_of_overtimeSn_OA_Overtime_dir,"not_approved_OA_Overtime")
        return self

    def remark_OA_Overtime(self,remark):
        '''
        点击“不批准”
        '''
        self._params["remark"] = remark
        self.step(details_of_overtimeSn_OA_Overtime_dir,"remark_OA_Overtime")
        return self

    def reminder_of_supplement_OA_Overtime(self):
        '''
        点击“补充资料提醒”
        '''
        self.step(details_of_overtimeSn_OA_Overtime_dir,"reminder_of_supplement_OA_Overtime")
        return self

    def close_details_OA_Overtime(self):
        '''
        点击“关闭详情”按钮
        '''
        self.step(details_of_overtimeSn_OA_Overtime_dir,"close_details_OA_Overtime")
        from page.OA_approvel.overtime_approvals.pending_for_approval_OA_Overtime import \
            Pending_For_Approval_OA_Overtime
        return Pending_For_Approval_OA_Overtime(self._driver)

    def get_approval_history_action(self):
        '''
        获取最后一行历史操作文本text
        '''
        history_action = self.step(details_of_overtimeSn_OA_Overtime_dir,"get_approval_history_action").text
        # 弹出的toast会遮挡“X”，需等待3s
        self.sleep(3)
        self.step(details_of_overtimeSn_OA_Overtime_dir,"close_details_OA_Overtime")
        return history_action

    def goto_approved_OA_Overtime(self):
        self.step(overtime_approvals_dir,"goto_approved_OA_Overtime")
        from page.OA_approvel.overtime_approvals.approved_OA_Overtime import Approved_OA_Overtime
        return Approved_OA_Overtime(self._driver)
