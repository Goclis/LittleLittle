# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

class GradeCrawler:
    """从信息门户获取成绩列表的爬虫

    :param username: 用户名
    :param password: 密码
    """

    def __init__(self, username, password):
        self.loginUrl = u'http://202.119.4.150/nstudent/login.aspx'
        self.gradeUrl = u'http://202.119.4.150/nstudent/grgl/xskccjcx.aspx'
        self.username = username
        self.password = password

    def getGrade(self):
        """获取成绩列表

        :return gradeList: 列表，每一项为一个三元组(课程名,原始成绩,规格化成绩)
        """
        # 获取cookie
        cookies = dict(requests.get(self.loginUrl).cookies)

        # 登陆
        loginPayload = {
            '__VIEWSTATE': 'dDw2Nzg5Mjk2NTY7O2w8b2s7Pj48MknpZN4t3xVYoaVlFnNMsdAYgA==',
            'txt_user': self.username,
            'txt_password': self.password,
            'ok.x': 0,
            'ok.y': 0
        }
        loginPage = requests.post(self.loginUrl, cookies=cookies, data=loginPayload)

        # 访问成绩页面
        gradePage = requests.get(self.gradeUrl, cookies=cookies)
        return self._parseGradePage(gradePage.text)

    def _parseGradePage(self, pageText):
        """解析成绩页面获取成绩列表

        :param pageText: 要解析的内容

        :return list: 列表，每一项为一个三元组(课程名,原始成绩,规格化成绩)
        """
        # 避免传入的内容不正确
        try:
            gradeList = []
            soup = BeautifulSoup(pageText, 'lxml')

            # 学位课 id="dgData"，非学位课 id="Datagrid1"
            for course in (soup.find(id="dgData").find_all("tr")[1:] \
                    + soup.find(id="Datagrid1").find_all("tr")[1:]):
                infos = course.find_all("td")
                gradeList.append((infos[0].string, infos[3].string, infos[4].string))
        
            return gradeList
        except:
            return []
