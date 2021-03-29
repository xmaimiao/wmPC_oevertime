from common.contants import approval_detail_HR_dir,overtime_approval_for_HR_dir
from page.basepage import BasePage


class Approval_Detail_HR(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def click_reminder_of_supplement_HR(self):
        '''
        点击提醒资料补充
        '''
        self.step(approval_detail_HR_dir,"click_reminder_of_supplement_HR")
        return self
    def get_reminder_toast_HR(self):
        '''
        获取“提醒成功”的toast,点击“取消”按钮关闭页面
        '''
        toast = self.step(approval_detail_HR_dir,"get_reminder_toast_HR")
        # 弹出的toast会遮挡“X”，需等待3s
        self.sleep(3)
        self.step(approval_detail_HR_dir, "click_cancel_HR")
        return toast

    def click_approved_HR(self):
        '''
        点击批准
        '''
        self.step(approval_detail_HR_dir,"click_approved_HR")
        return self

    def click_not_approved_HR(self):
        '''
        点击不批准
        '''
        self.step(approval_detail_HR_dir,"click_not_approved_HR")
        return self

    def close_poppage_HR(self):
        '''
        关闭弹出页面
        '''
        self.step(approval_detail_HR_dir,"close_poppage_HR")
        from page.overtimePage.overtime_approval_for_HR.pending_for_approval_HR import Pending_For_Approval_HR
        return Pending_For_Approval_HR(self._driver)

    def get_approval_history_action_HR(self):
        '''
        获取审批历史最后一行数据的操作text,前提：点击提醒后必须关闭页面
        '''
        action_text =  (self.step(approval_detail_HR_dir,"get_approval_history_action_HR")).text
        # 弹出的toast会遮挡“X”，需等待3s
        self.sleep(3)
        self.step(approval_detail_HR_dir, "close_poppage_HR")
        return action_text

    def goto_approved_HR(self):
        '''
        打開已審批頁面
        '''
        self.step(overtime_approval_for_HR_dir, "goto_approved")
        from page.overtimePage.overtime_approval_for_HR.approved_HR import Approved_HR
        return Approved_HR(self._driver)