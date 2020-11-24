from common.contants import application_detail_dir
from page.basepage import BasePage


class Application_Detail(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def upload_supplementary_meterials(self, excel_path):
        '''
        上传补充资料,install  pywin32
        '''
        self._params["excel_path"] = excel_path
        self.step(application_detail_dir, "upload_supplementary_meterials")
        self.sleep(2)
        self.upload_file(excel_path)
        self.sleep(2)
        # 上传页面点击“确认”按钮
        self.step(application_detail_dir, "upload_save_click")
        return self

    def get_approval_history_action(self):
        '''
        获取审批历史最后一行数据的操作text
        '''
        action_text =  (self.step(application_detail_dir,"get_approval_history_action")).text
        self.step(application_detail_dir, "close_poppage")
        return action_text

    def close_poppage(self):
        '''
        关闭弹出页面
        '''
        self.step(application_detail_dir,"close_poppage")
        from page.overtimePage.my_overtime_records.my_overtime import My_Overtime
        return My_Overtime(self._driver)