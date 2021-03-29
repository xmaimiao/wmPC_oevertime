from common.contants import approved_dir
from page.basepage import BasePage


class Approved(BasePage):

    def wait_sleep(self,slepps):
        self.sleep(slepps)
        return self

    def get_the_overtimeSn_status(self, overtimeSn):
        '''
        通過加班單號獲取該狀態
        :param overtimeSn: 加班單號
        '''
        self._params["overtimeSn"] = overtimeSn
        return self.step(approved_dir, "get_the_overtimeSn_status")

    def get_the_fir_status(self):
        '''
        第一行数据，獲取該狀態
        '''
        return self.step(approved_dir, "get_the_fir_status")