from common.contants import read_dir, index_dir
from page.basepage import BasePage


class Read(BasePage):
    def get_the_news_read(self, new_numlist):
        '''
        根据传进来的nums去取第几条信息
        获取第一行信息的text
        '''
        news_liat =[]
        try:
            for new_num in new_numlist:
                self._params["new_num"] = new_num
                text = (self.step(read_dir,"get_the_news_read")).text
                news_liat.append(text)
                print(f"獲取到的消息是：{text}")
            return news_liat
        except Exception as e:
            raise e


    def goto_overtime_for_news_read(self,new_num):
        '''
        根據傳進來的序號獲取第N條消息並點擊進入改應用
        驗證進入了加班應用，返回”加班詳情“text
        '''
        self._params["new_num"] = new_num
        # 點擊第N條信息
        self.step(read_dir, "goto_overtime_for_news_read")
        return (self.step(index_dir,"get_overtime_title")).text