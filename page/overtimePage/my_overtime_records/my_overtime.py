import shelve

from common.contants import my_overtime_dir
from page.basepage import BasePage
from page.overtimePage.my_overtime_records.application_detail import Application_Detail


class My_Overtime(BasePage):
    def get_page_title(self):
        '''
        獲取頁面text"加班明細”
        '''
        return self.step(my_overtime_dir,"get_page_title")

    def the_first_overtime_cancel(self):
        '''
        1.撤銷第一條加班申請
        2.驗證第一條申請狀態：已撤銷
        '''
        return self.step(my_overtime_dir,"the_first_overtime_cancel")

    def the_overtimeSn_for_cancel(self,overtimeSn):
        '''
        1.根據加班申請單號撤銷申請
        2.驗證該單號申請狀態：已撤銷
        '''
        self._params["overtimeSn"] = overtimeSn
        return self.step(my_overtime_dir,"the_overtimeSn_for_cancel")

    def get_the_fir_status(self,overtimeSn):
        '''
        獲取第一條數據的狀態
        '''
        self._params["overtimeSn"] = overtimeSn
        return self.step(my_overtime_dir,"get_the_fir_status")

    def get_the_fir_overtimeSn(self):
        '''
        獲取第一條數據的申請單號
        '''
        db = shelve.open("overtimeSn")
        overtimeSn = self.step(my_overtime_dir,"get_the_fir_overtimeSn")
        db["overtimeSn"] = overtimeSn
        db.close()
        print(f"overtimeSn:{overtimeSn}")
        return self

    def goto_application_detail(self,overtimeSn):
        '''
        通过加班申请单号，打开申请详情页
        '''
        try:
            self._params["overtimeSn"] = overtimeSn
            self.step(my_overtime_dir,"goto_application_detail")
            return Application_Detail(self._driver)
        except Exception as e:
            print(f"加班单号不存在：{overtimeSn}")