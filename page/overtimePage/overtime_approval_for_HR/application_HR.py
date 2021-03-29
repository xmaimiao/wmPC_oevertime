from common.contants import application_HR_dir
from page.basepage import BasePage


class Application_HR(BasePage):
    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def applicant(self,applicant):
        '''
        输入申请人姓名
        '''
        self._params["applicant"] = applicant
        self.step(application_HR_dir,"applicant")
        return self

    def UserTel(self,UserTel):
        '''
        输入申请人电话
        '''
        self._params["UserTel"] = UserTel
        self.step(application_HR_dir,"UserTel")
        return self

    def startDate(self,startDate):
        '''
        输入加班日期
        '''
        self._params["startDate"] = startDate
        self.step(application_HR_dir,"startDate")
        return self

    def starttime(self,starttime):
        '''
        添加加班開始時間
        '''
        self._params["starttime"] = starttime
        self.step(application_HR_dir,"starttime")
        return self

    def endtime(self,endtime):
        '''
        添加加班開始時間
        '''
        self._params["endtime"] = endtime
        self.step(application_HR_dir,"endtime")
        self._driver.switch_to.default_content()
        return self

    def remark(self,remark):
        '''
        添加加班開始時間
        '''
        self._params["remark"] = remark
        self.step(application_HR_dir,"remark")
        return self

    def upload_attachment(self,excel_path):
        '''
        上传附件,install  pywin32
        '''
        self._params["excel_path"] = excel_path
        self.step(application_HR_dir,"upload_attachment")
        self.sleep(1)
        self.upload_file(excel_path)
        self.sleep(1)
        return self

    def save_click(self):
        '''
        1.點擊”保存“按鈕
        2.打開加班協議書
        '''
        self.step(application_HR_dir,"save_click")
        return self

    def IDcard(self,IDcard):
        '''
        添加身份證/護照編號
        '''
        self._params["IDcard"] = IDcard
        self.step(application_HR_dir,"IDcard")
        return self

    def click_tips(self):
        '''
        點擊溫馨提示
        '''
        self.step(application_HR_dir,"click_tips")
        return self

    def back_to_pending(self):
        '''
        返回HR待审批页面
        '''
        from page.overtimePage.overtime_approval_for_HR.pending_for_approval_HR import Pending_For_Approval_HR
        return Pending_For_Approval_HR(self._driver)