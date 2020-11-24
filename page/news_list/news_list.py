from common.contants import news_list_dir
from page.basepage import BasePage
from page.news_list.read import Read


class News_List(BasePage):
    def goto_all_news(self):
        '''
        打開“全部”tab
        '''
        self.step(news_list_dir,"goto_all_news")
        return self

    def get_the_news(self,new_numlist):
      '''
      根据传进来的num去取第几条信息
      获取第一行信息的text
      '''
      news_liat = []
      try:
          for new_num in new_numlist:
              self._params["new_num"] = new_num
              text = (self.step(news_list_dir, "get_the_news_read")).text
              news_liat.append(text)
              print(f"獲取到的消息是：{text}")
          return news_liat
      except Exception as e:
          raise e

    def goto_read(self):
        '''
        打開“已讀”tab
        '''
        self.step(news_list_dir,"goto_read")
        return Read(self._driver)