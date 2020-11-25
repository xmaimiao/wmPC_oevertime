from common.contants import add_or_edit_group_dir
from page.basepage import BasePage


class Add_Or_Edit_Group(BasePage):
    def edit_group_name(self,group_name):
        '''
        編輯組名
        '''
        self._params["group_name"] = group_name
        self.step(add_or_edit_group_dir,"edit_group_name")
        return self

    def edit_english_name(self,english_name):
        '''
        編輯英文名
        '''
        self._params["english_name"] = english_name
        self.step(add_or_edit_group_dir,"edit_english_name")
        return self

    def del_group_members(self):
        '''
        刪除所有的審批人
        '''
        # 獲取所有的人員的“x”元素
        try:
            ele_len = self.step(add_or_edit_group_dir,"get_group_members_for_del")
            for i in range(1,ele_len+1):
                self.step(add_or_edit_group_dir,"del_group_members")
        except Exception as e:
            pass
        return self

    def edit_group_members(self,members):
        '''
        編輯審批人，members是人員數組
        '''
        try:
            for member in members:
                self._params["member"] = member
                self.step(add_or_edit_group_dir,"edit_group_members")
        except Exception as e:
            raise e
        return self

    def edit_remark(self,remark):
        '''
        編輯備注
        '''
        self._params["remark"] = remark
        self.step(add_or_edit_group_dir,"edit_remark")
        return self

    def click_save(self):
        '''
        編輯英文名
        '''
        self.step(add_or_edit_group_dir,"click_save")
        from page.overtimePage.approval_settings.approval_group_setting import Approval_Group_Setting
        return Approval_Group_Setting(self._driver)
