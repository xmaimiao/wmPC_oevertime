import shelve

from common.contants import pending_for_approval_OA_Overtime_dir, pending_for_approval_OA_Overtime_HR_dir
from page.OA_approvel.overtime_approvals.details_of_overtimeSn_OA_Overtime import Details_Of_OvertimeSn_OA_Overtime
from page.OA_approvel.overtime_approvals_for_HR.details_of_overtimeSn_OA_Overtime_HR import \
    Details_Of_OvertimeSn_OA_Overtime_HR
from page.basepage import BasePage


class Pending_For_Approval_OA_Overtime_HR(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def goto_details_of_overtimeSn_OA_Overtime_HR(self,overtimeSn):
        '''
        根据“加班单号”打开加班详情页面
        '''
        self._params["overtimeSn"] = overtimeSn
        self.step(pending_for_approval_OA_Overtime_HR_dir,"goto_details_of_overtimeSn_OA_Overtime_HR")
        return Details_Of_OvertimeSn_OA_Overtime_HR(self._driver)

    def goto_details_of_the_fir_OA_Overtime_HR(self):
        '''
        打开第一行数据加班详情页面
        '''
        self.step(pending_for_approval_OA_Overtime_HR_dir,"goto_details_of_the_fir_OA_Overtime_HR")
        # 获取加班单号
        db = shelve.open("overtimeSn")
        db["overtimeSn"] = self.step(pending_for_approval_OA_Overtime_HR_dir,"get_the_OTid_fir_OA_Overtime_HR")
        db.close()
        return Details_Of_OvertimeSn_OA_Overtime_HR(self._driver)

    def get_the_fir_applicant_OA_Overtime_HR(self):
        '''
        获取第一行数据的申请人姓名，验证bug用
        '''
        return self.step(pending_for_approval_OA_Overtime_HR_dir,"get_the_fir_applicant_OA_Overtime_HR")

    def back_to_main(self):
        from page.main import Main
        return Main(self._driver)