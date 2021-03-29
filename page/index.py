from common.contants import index_dir
from page.OA_approvel.OA_approvalPage import OA_Approval
from page.application import Application
from page.basepage import BasePage
from page.news_list.news_list import News_List


class Index(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def goto_application(self):
        self.step(index_dir,"goto_application")
        return Application(self._driver)


    def quit(self):
        '''
        推出當前登陸賬號
        :return:
        '''
        self.step(index_dir,"quit")

    def goto_news_list(self):
        '''
        打开消息中心列表
        '''
        self.step(index_dir,"goto_news_list")
        return News_List(self._driver)

    def goto_OA_approval(self):
        '''
        在首页中心打开OA审批
        '''
        self.step(index_dir,"goto_OA_approval")
        return OA_Approval(self._driver)

    def get_news(self,new_numlist):
        '''
        根據傳進來的序號獲取第N條消息文本text
        :param num: 序號
        '''
        news_liat =[]
        try:
            for new_num in new_numlist:
                self._params["new_num"] = new_num
                text = self.step(index_dir,"get_news")
                news_liat.append(text)
                print(f"獲取到的消息是：{text}")
            return news_liat
        except Exception as e:
            raise e

    def goto_overtime_for_news(self,new_num):
        '''
        根據傳進來的序號獲取第N條消息並點擊進入改應用
        驗證進入了加班應用，返回”加班詳情“text
        '''
        self._params["new_num"] = new_num
        # 點擊第N條信息
        self.step(index_dir, "goto_overtime_for_news")
        all_pages = self._driver.window_handles  # 获得所有窗口句柄
        self._driver.switch_to.window(all_pages[-1])  # 切换至最后一个窗口
        return (self.step(index_dir,"get_overtime_title")).text

    def get_index_ele_fir(self):
        '''
        獲取應用-“首頁”元素，驗證登錄成功，一期
        '''
        return self.step(index_dir, "get_index_ele_fir")

    def get_index_ele_sec(self):
        '''
        獲取應用-“首頁”元素，驗證登錄成功，二期
        '''
        return self.step(index_dir, "get_index_ele_sec")

