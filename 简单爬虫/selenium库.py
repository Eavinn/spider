from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaiduSpider(object):
    def __init__(self):
        op = Options()
        op.headless = False
        self.driver = webdriver.Chrome(options=op)
        self.driver.maximize_window()

    def __del__(self):
        # self.driver.close()
        try:
            self.driver.quit()
        except ImportError:
            pass

    def input_kw(self):
        self.switch_handle()
        self.driver.find_element_by_id("kw").send_keys("传智播客")
        self.driver.find_element_by_id("su").click()
        print(self.driver.current_url)
        print(self.driver.get_cookies())
        self.driver.implicitly_wait(3)

    def switch_handle(self):
        for handle in self.driver.window_handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                break

    def skip_to_hao123(self):
        el = self.driver.find_element_by_link_text('hao123')
        el.click()
        self.switch_handle()
        self.driver.implicitly_wait(3)
        self.driver.save_screenshot("hao123.png")

    def run(self):
        self.driver.get("https://www.baidu.com")
        self.skip_to_hao123()
        self.input_kw()


if __name__ == '__main__':
    bds = BaiduSpider()
    bds.run()



