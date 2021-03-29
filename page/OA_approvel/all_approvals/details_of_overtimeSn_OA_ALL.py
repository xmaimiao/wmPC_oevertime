from common.contants import details_of_overtimeSn_OA_ALL_dir, all_approvals_dir
from page.OA_approvel.all_approvals.approved_OA_ALL import Approved_OA_ALL
from page.basepage import BasePage


class Details_Of_OvertimeSn_OA_ALL(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def agree_overtime_work_agreement(self):
        '''
        同意超時工作協議書
        '''
        self.step(details_of_overtimeSn_OA_ALL_dir,"agree_overtime_work_agreement")
        return self

    def approved_OA_ALL(self):
        '''
        点击“批准”
        '''
        self.step(details_of_overtimeSn_OA_ALL_dir,"approved_OA_ALL")
        return self

    def not_approved_OA_ALL(self):
        '''
        点击“不批准”
        '''
        self.step(details_of_overtimeSn_OA_ALL_dir,"not_approved_OA_ALL")
        return self

    def remark_OA_ALL(self,remark):
        '''
        点击“不批准”
        '''
        self._params["remark"] = remark
        self.step(details_of_overtimeSn_OA_ALL_dir,"remark_OA_ALL")
        return self

    def reminder_of_supplement_OA_ALL(self):
        '''
        点击“补充资料提醒”
        '''
        self.step(details_of_overtimeSn_OA_ALL_dir,"reminder_of_supplement_OA_ALL")
        return self

    def close_details_OA_ALL(self):
        '''
        点击“关闭详情”按钮
        '''
        self.step(details_of_overtimeSn_OA_ALL_dir,"close_details_OA_ALL")
        from page.OA_approvel.all_approvals.pending_for_approval_OA_ALL import Pending_For_Approval_OA_ALL
        return Pending_For_Approval_OA_ALL(self._driver)

    def get_approval_history_action(self):
        '''
        获取最后一行历史操作文本text
        '''
        history_action = self.step(details_of_overtimeSn_OA_ALL_dir,"get_approval_history_action").text
        # 弹出的toast会遮挡“X”，需等待3s
        self.sleep(3)
        self.step(details_of_overtimeSn_OA_ALL_dir,"close_details_OA_ALL")
        return history_action

    def goto_approved_OA_ALL(self):
        self.step(all_approvals_dir,"goto_approved_OA_ALL")
        return Approved_OA_ALL(self._driver)

    def back_to_pending_for_approval_OA_ALL(self):
        '''
        打開待審批頁面
        '''
        self.step(all_approvals_dir, "goto_pending_for_approval_OA_ALL")
        from page.OA_approvel.all_approvals.pending_for_approval_OA_ALL import Pending_For_Approval_OA_ALL
        return Pending_For_Approval_OA_ALL(self._driver)

