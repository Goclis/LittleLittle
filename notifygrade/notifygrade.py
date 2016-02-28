#!/usr/bin/env python
# -*- coding:utf-8 -*-

import crawler
import timeoututil
import emailutil
import config

class GradeNotifier:
    """定期获取成绩，当成绩发生变化时邮件提醒"""

    def __init__(self):
        # 初始化获取一次
        self.crawler = crawler.GradeCrawler(config.username, config.password)
        self.gradeList = None

    def start(self):
        """开始监听成绩变化"""
        timeoututil.setInterval(self._update, 5)

    def _update(self):
        newGradeList = self.crawler.getGrade()
        if self.gradeList != newGradeList:
            self.gradeList = newGradeList

            # 邮件通知
            emailContent = ''
            for c in self.gradeList:
                emailContent += u"{0} {1} {2}\n".format(c[0], c[1], c[2])
            emailutil.sendEmail(config.emailUsername, config.emailPassword, 'GradeNotifier', emailContent)


def main():
    notifier = GradeNotifier()
    notifier.start()


if __name__ == '__main__':
    main()
