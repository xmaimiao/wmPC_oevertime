from common.contants import approval_settings_dir
from page.basepage import BasePage
from page.overtimePage.approval_settings.approval_group_setting import Approval_Group_Setting
from page.overtimePage.approval_settings.edit_approval_process import Edit_Approval_Process


class Approval_Settings(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def search_user(self,user):
        '''
        查詢人員信息
        '''
        self._params["user"] = user
        self.step(approval_settings_dir,"search_user")
        return self

    def get_the_first_approval_process_T(self):
        '''
        獲取第一行數據的審批流text,返回True  False
        '''
        try:
            result = self.step(approval_settings_dir,"get_the_first_approval_process")
            print(f"該人員的審批流為：{result}")
            return True
        except Exception as e:
            return False

    def get_the_first_approval_process(self):
        '''
        獲取第一行數據的審批流text,返回True  False
        '''
        try:
            result =   self.step(approval_settings_dir,"get_the_first_approval_process")
            print(f"审批流为：{result}")
            return True
        except ellipsis as e:
            return False


    def edit_the_first_approval_process(self,approval_list,action=None):
        '''
        1.编辑第一行数据的审批流,点击“编辑”按钮
        2.若审批流已存在，则报错
        '''
        get_approval = self.step(approval_settings_dir,"get_the_first_approval_process")
        for approval in approval_list:
            if approval in get_approval and action == "edit":
                print("该审批流已存在")
                return
        else:
            self.step(approval_settings_dir,"edit_the_first_approval_process")
            return Edit_Approval_Process(self._driver)

    def edit_the_first_approval_process_repeat(self):
        '''
        1.编辑第一行数据的审批流,点击“编辑”按钮
        2.可以添加多个重复的审批流用
        '''
        self.step(approval_settings_dir,"edit_the_first_approval_process")
        return Edit_Approval_Process(self._driver)

    def goto_approval_group_setting(self):
        '''
        打開審批組設置
        '''
        self.step(approval_settings_dir,"goto_approval_group_setting")
        return Approval_Group_Setting(self._driver)

