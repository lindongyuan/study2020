"""    通过selenium 实现刷课程序
        超星平台
    url： http://passport2.chaoxing.com/login?fid=&refer=http://i.mooc.chaoxing.com
"""
from selenium import webdriver
import requests
import yun_code
import time
import random
import easygui as g


class chaoxing_spider():

    def __init__(self, user_name, user_password, school_name, class_name):
        self.url = "http://passport2.chaoxing.com/login?fid=&refer=http://i.mooc.chaoxing.com"
        self.user_name = user_name
        self.user_password = user_password
        self.school_name = school_name
        self.class_name = class_name

        #  设置无界面参数
        # 创建chrome参数对象
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')  # 非沙盒模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options, executable_path="Chrome/chromedriver.exe")
        print("运行")

    #  登录账号细节
    def _sign(self):
        self.driver.get(self.url)
        # 1、获取验证码url，  返回图片内容和cookies
        img = self.driver.find_element_by_id("numVerCode").get_attribute("src")
        # 2、请求验证码url
        ans = requests.get(img)
        # 3、照片cookies
        ans_cookies = []
        for item in ans.cookies:
            ans_cookies.append({'name': item.name, 'value': item.value})

        # 4、将验证码写到jpg里
        with open(b"file/011.jpg", "wb")  as f:
            f.write(ans.content)

        # 5、利用云打码获取验证码
        code = yun_code.get_code(1004, b'file/011.jpg')

        # 选择学校
        self.driver.find_element_by_link_text("选择单位").click()
        self.driver.find_element_by_id("searchSchool1").send_keys(self.school_name)
        self.driver.find_element_by_class_name("zw_t_btn").click()
        #  此处有加载过程，需要尝试
        for i in range(10):
            try:
                self.driver.find_element_by_link_text(self.school_name).click()
                break
            except:
                time.sleep(1)

        # 填写账号、密码、验证码
        self.driver.find_element_by_id("unameId").send_keys(self.user_name)
        self.driver.find_element_by_id("passwordId").send_keys(self.user_password)
        # 6、填写验证码
        self.driver.find_element_by_id("numcode").send_keys(code)
        # 7、将验证码cookies添加到driver
        for item in ans_cookies:
            self.driver.add_cookie(item)
        # 8、登录
        self.driver.find_element_by_xpath("//*[@id='form']/table/tbody/tr[7]/td[2]/label/input").click()

    # 登录账号、对外接口
    def sign(self):
        for i in range(10):
            print("第{}登录。。。。".format(i + 1))
            try:
                self._sign()
                print("\t登录成功！")
                return True
            except:
                time.sleep(1)
        return False

    # 选择课程, 返回当前课程地址
    def selected_class(self):
        print("选择课程。。。。。")
        self.driver.get(self.driver.current_url)
        #  切换到iframe
        for i in range(10):
            try:
                self.driver.switch_to.frame("frame_content")
            except:
                time.sleep(1)
        # 发现课程，点击课程
        self.driver.find_element_by_partial_link_text(self.class_name).click()
        # self.driver.get(  self.driver.current_url )

        ##  n = window.handle 获取当前页面左右的句柄
        ##  switch_to_window( n[0]) 切换到最前的一页
        ##  todo 解决问题： 点击超链接（ target="_blank"）后current_url 和page_souce本页没有改变
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("\t选择成功！")
        return self.driver.current_url

    # 获取某一章节的视频url
    def open_class(self, url):
        self.driver.get(url)
        self.driver.refresh()  # 更新界面
        time.sleep(2)
        self.driver.find_element_by_xpath("*//div[5]/div[1]/div[2]/div[3]/div[1]/div[1]/h3/span[3]/a").click()
        # 获取 章节对象
        part_list = []
        part_list = self.driver.find_elements_by_xpath(" //*[@id='coursetree']//h4")
        for item in part_list:
            ans = item.find_element_by_xpath("span[2]").text
            # print( ans )
            if ans:
                for i in range(5):
                    try:
                        item.find_element_by_xpath("a").click()
                        print("章节：", str(item.find_element_by_xpath("*//span").text).strip())
                        break
                    except:
                        time.sleep(1)
                break
        # 获取当页视频、有加载过程，需要等待
        for i in range(10):
            try:
                video__url = self.driver.find_element_by_xpath("*//iframe[@id='iframe']").get_attribute("src")
                return video__url
            except  Exception as e:
                time.sleep(1)
        return ""

    # 看视频
    def view_video(self, url):
        self.driver.get(url)
        iframe = []
        for i in range(10):
            iframe = self.driver.find_elements_by_xpath("*//iframe")
            if iframe:
                break
            time.sleep(1)
        # 如果是图片，则不存在iframe
        if not iframe:
            print("这是图片，不看了")
            return
        index = 1
        for item in iframe:
            self.driver.switch_to.frame(item)
            print("\t正在看第{}个视频".format(index))
            for i in range(10):
                try:  # todo 这个切换一定注意
                    self.driver.find_element_by_xpath("*//div[@id='reader']").click()
                    time.sleep(1)
                    # 视频时长
                    time_leng = self.driver.find_element_by_xpath("//*[@id='video']/div[4]/div[4]/span[2]").text
                    time_num = int(str(time_leng).split(":")[0].strip()) * 60 + int(
                        str(time_leng).split(":")[1].strip())
                    print("\t\t时长：", time_num)
                    time.sleep(int(time_num))
                    break
                except Exception as e:
                    print(i, e)
                    time.sleep(1)
            print("\t\t第{}个视频结束了".format(index))
            # 回到默认页面
            self.driver.switch_to.default_content()
            index += 1

    # 逻辑实现
    def run(self):
        if not self.sign():
            print("登录失败！")
            return
        class_url = self.selected_class()
        while True:
            video_url = self.open_class(class_url)
            if video_url:
                self.view_video(video_url)
                time.sleep(random.randint(1, 10))
            else:
                break


if __name__ == '__main__':
    ans = g.multenterbox(msg='输入信息！', fields=['账号', '密码', '学校信息', '课程'],
                         values=["账号", "密码", "学校名称", "新型冠状病毒"])
    if len(ans) == 4:
        account = ans[0]
        password = ans[1]
        school_name = ans[2]
        class_name = ans[3]
        spider = chaoxing_spider(account, password, school_name, class_name)
        spider.run()