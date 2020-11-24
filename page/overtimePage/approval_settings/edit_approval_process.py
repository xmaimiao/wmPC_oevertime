from common.contants import edit_approval_process_dir
from page.basepage import BasePage


class Edit_Approval_Process(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def edit_the_fir_approval(self,approval1):
        '''
        添加1级审批
        '''
        self._params["approval1"] = approval1
        self.step(edit_approval_process_dir,"edit_the_fir_approval")
        return self


    def edit_the_sec_approval(self,approval2):
        '''
        添加2级审批
        '''
        self._params["approval2"] = approval2
        self.step(edit_approval_process_dir,"edit_the_sec_approval")
        return self

    def del_the_fir_approval(self):
        '''
        删除1级审批
        '''
        self.step(edit_approval_process_dir,"del_the_fir_approval")
        return self

    def del_the_sec_approval(self):
        '''
        删除2级审批
        '''
        self.step(edit_approval_process_dir,"del_the_sec_approval")
        return self


    def save_click(self):
        self.step(edit_approval_process_dir,"save_click")
        from page.overtimePage.approval_settings.approval_settings import Approval_Settings
        return Approval_Settings(self._driver)