from common.contants import my_overtime_dir
from page.basepage import BasePage


class My_Overtime(BasePage):
    def get_page_title(self):
        '''
        獲取頁面text"加班明細”
        '''
        return self.step(my_overtime_dir,"get_page_title")