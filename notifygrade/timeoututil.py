# -*- coding:utf-8 -*-

import threading

def setInterval(func, sec):
    """Python setInterval

    用法类似于Javascript的setInterval。

    :param func: 定期执行的方法。
    :param sec:  定时的时间，秒为单位。
    """
    def func_wrapper():
        setInterval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
