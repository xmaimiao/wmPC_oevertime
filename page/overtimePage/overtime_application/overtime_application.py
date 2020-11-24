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
        return My_Overtime(self._driver)