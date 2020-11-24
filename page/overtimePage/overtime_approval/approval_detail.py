from common.contants import approval_detail_dir
from page.basepage import BasePage


class Approval_Detail(BasePage):

    def click_reminder_of_supplement(self):
        '''
        点击提醒资料补充
        '''
        self.step(approval_detail_dir,"click_reminder_of_supplement")
        return self


    def close_poppage(self):
        '''
        关闭弹出页面
        '''
        self.step(approval_detail_dir,"close_poppage")
        from page.overtimePage.overtime_approval.pending_for_approval import Pending_For_Approval
        return Pending_For_Approval(self._driver)

    def get_approval_history_action(self):
        '''
        获取审批历史最后一行数据的操作text
        '''
        action_text =  (self.step(approval_detail_dir,"get_approval_history_action")).text
        # 弹出的toast会遮挡“X”，需等待3s
        self.sleep(3)
        self.step(approval_detail_dir, "close_poppage")
        return action_text