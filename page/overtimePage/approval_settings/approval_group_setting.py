import json

from common.contants import approval_group_setting_dir
from page.basepage import BasePage
from page.overtimePage.approval_settings.add_or_edit_group import Add_Or_Edit_Group


class Approval_Group_Setting(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def get_approval_group_all(self):
        '''
        輸出所有審批組
        '''
        try:
            ele_len = self.step(approval_group_setting_dir,"get_approval_group_all")
            groups={}
            for i in range(1,ele_len +1):
                self._params["i"] = i
                group_name = self.step(approval_group_setting_dir,"get_group_name")
                group_members = self.step(approval_group_setting_dir,"get_roup_members")
                groups[group_name] = group_members
            print(json.dumps(groups,indent=4,ensure_ascii=False))
            return True
        except Exception as e:
            return False


    def edit_group_for_name(self,group_name):
        '''
        編輯審批組，通過審批組名稱定位到編輯的組
        '''
        self._params["group_name"] = group_name
        self.step(approval_group_setting_dir,"edit_group_for_name")
        return Add_Or_Edit_Group(self._driver)

    def get_members_for_group_name(self,group_name):
        '''
        通過審批組名定位到具體行，輸出該審批組人員,注意只能給出人員的姓名，所以最好用姓名查詢
        '''
        self._params["group_name"] = group_name
        return self.step(approval_group_setting_dir,"get_members_for_group_name")