from common.contants import approval_detail_dir, overtime_approval_dir, pending_for_approval_dir
from page.basepage import BasePage


class Approval_Detail(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def click_reminder_of_supplement(self):
        '''
        点击提醒资料补充
        '''
        self.step(approval_detail_dir,"click_reminder_of_supplement")
        return self

    def click_approved(self):
        '''
        点击批准
        '''
        self.step(approval_detail_dir,"click_approved")
        return self

    def click_tips_confirm(self):
        '''
        批准，點擊加班時間屬於 辦公時間 彈出的溫馨提示
        '''
        self.step(pending_for_approval_dir, "click_tips_confirm")
        return self

    def click_not_approved(self):
        '''
        点击不批准
        '''
        self.step(approval_detail_dir,"click_not_approved")
        return self

    def get_reminder_toast(self):
        '''
        获取“提醒成功”的toast,点击“取消”按钮关闭页面
        '''
        toast = self.step(approval_detail_dir,"get_reminder_toast")
        # 弹出的toast会遮挡“X”，需等待3s
        self.sleep(3)
        self.step(approval_detail_dir, "click_cancel")
        return toast

    def close_poppage(self):
        '''
        关闭弹出页面
        '''
        self.step(approval_detail_dir,"close_poppage")
        from page.overtimePage.overtime_approval.pending_for_approval import Pending_For_Approval
        return Pending_For_Approval(self._driver)

    def get_approval_history_action(self):
        '''
        获取审批历史最后一行数据的操作text,前提：点击提醒后必须关闭页面
        '''
        action_text =  (self.step(approval_detail_dir,"get_approval_history_action")).text
        # 弹出的toast会遮挡“X”，需等待3s
        self.sleep(3)
        self.step(approval_detail_dir, "close_poppage")
        return action_text

    def goto_approved(self):
        '''
        打開已審批頁面
        '''
        self.step(overtime_approval_dir, "goto_approved")
        from page.overtimePage.overtime_approval.approved import Approved
        return Approved(self._driver)

    def goto_pending_for_approval(self):
        '''
        返回待審批頁面
        '''
        from page.overtimePage.overtime_approval.pending_for_approval import Pending_For_Approval
        return Pending_For_Approval(self._driver)