from common.contants import approved_OA_Overtime_dir
from page.basepage import BasePage


class Approved_OA_Overtime(BasePage):

    def get_the_status_of_overtimeSn(self,overtimeSn):
        '''
        根据加班单号获取该订单的状态
        '''
        self._params["overtimeSn"] = overtimeSn
        return self.step(approved_OA_Overtime_dir,"get_the_status_of_overtimeSn")