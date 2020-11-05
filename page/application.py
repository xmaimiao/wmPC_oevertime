from common.contants import application_dir
from page.basepage import BasePage
from page.overtimePage.overtimePage import OvertimePage


class Application(BasePage):

    def goto_overtime(self, application):
        '''
        進入加班應用
        '''
        self._params["application"] = application
        self.step(application_dir, "overtime")
        return OvertimePage(self._driver)


