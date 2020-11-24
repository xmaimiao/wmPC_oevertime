from common.contants import approved_HR_dir
from page.basepage import BasePage


class Approved_HR(BasePage):
    def get_the_overtimeSn_status_HR(self, overtimeSn):
        '''
        通過加班單號獲取該狀態
        :param overtimeSn: 加班單號
        '''
        self._params["overtimeSn"] = overtimeSn
        return self.step(approved_HR_dir, "get_the_overtimeSn_status_HR")