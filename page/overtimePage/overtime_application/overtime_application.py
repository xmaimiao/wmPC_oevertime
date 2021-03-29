import win32con
import win32gui

from common.contants import overtime_application_dir
from page.basepage import BasePage
from page.overtimePage.my_overtime_records.my_overtime import My_Overtime


class Overtime_Application(BasePage):


    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def edit_UserTel(self,UserTel):
        '''
        填寫電話號碼
        '''
        self._params["UserTel"] = UserTel
        self.step(overtime_application_dir,"edit_UserTel")
        return self

    def edit_startDate(self,startDate):
        '''
        填寫加班日期
        '''
        self._params["startDate"] = startDate
        self.step(overtime_application_dir,"edit_startDate")
        return self

    def edit_starttime(self,starttime):
        '''
        添加加班開始時間
        '''
        self._params["starttime"] = starttime
        self.step(overtime_application_dir,"edit_starttime")
        return self

    def edit_endtime(self,endtime):
        '''
        添加加班開始時間
        '''
        self._params["endtime"] = endtime
        self.step(overtime_application_dir,"edit_endtime")
        self._driver.switch_to.default_content()
        return self

    def edit_remark(self,remark):
        '''
        添加加班開始時間
        '''
        self._params["remark"] = remark
        self.step(overtime_application_dir,"edit_remark")
        return self

    def upload_attachment(self,excel_path):
        '''
        上传附件,install  pywin32
        '''
        self._params["excel_path"] = excel_path
        self.step(overtime_application_dir,"upload_attachment")
        self.sleep(1)
        self.upload_file(excel_path)
        self.sleep(1)
        return self

    def save_click(self):
        '''
        1.點擊”保存“按鈕
        2.打開加班協議書
        '''
        self.step(overtime_application_dir,"save_click")
        return self

    def edit_IDcard(self,IDcard):
        '''
        添加身份證/護照編號
        '''
        self._params["IDcard"] = IDcard
        self.step(overtime_application_dir,"edit_IDcard")
        return self

    def get_IDcard(self):
        '''
        獲取份證/護照編號
        '''
        ele = self.step(overtime_application_dir,"get_IDcard")
        self.step(overtime_application_dir, "close_page")
        return ele.get_attribute("value")

    def get_tips(self):
        '''
        獲取溫馨提示：閣下申請之加班時間段屬於 辦公時間內/周末/公眾假期, 請注意並確認是否繼續申請。
        '''
        try:
            text = self.step(overtime_application_dir,"get_tips")
            print(f"溫馨提示：{text}")
            self.step(overtime_application_dir, "close_tips")
            return True
        except Exception as e:
            return False

    def click_tips(self):
        '''
        點擊溫馨提示
        '''
        try:
            self.step(overtime_application_dir,"click_tips")
            return self
        except Exception as e:
            print("没有tips！")
            raise

    def goto_my_overtime(self):
        '''
        打開我的加班-加班明細頁面
        '''
        return My_Overtime(self._driver)
