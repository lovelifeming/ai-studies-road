#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/16 15:45
# @Author : zengsm
# @File : global_interpreter_lock
# 参考资料 https://www.cnblogs.com/welan/p/10009638.html
import sys
import threading
import time
import traceback


class HookThread(threading.Thread):
    """ 钩子线程，主线程获取子线程异常 """

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        if kwargs is None:
            kwargs = {}
        self.__target = target
        self.__args = args
        self.__kwargs = kwargs

    def run(self):
        self.exc = None
        try:
            if self.__target:
                self.__target(*self.__args, **self.__kwargs)
        except Exception as e:
            self.exc = sys.exc_info()
        finally:
            del self.__target, self.__args, self.__kwargs

    def join(self):
        threading.Thread.join(self)
        if self.exc:
            msg = "Thread '%s' threw an exception: %s" % (self.getName(), self.exc[1])
            new_exc = Exception(msg)
            raise new_exc.with_traceback(self.exc[2])

def test1():
    for i in range(2):
        print('{},{}'.format(threading.current_thread().getName(), i))
        time.sleep(5)
    raise Exception('这是子线程1中抛出的异常!')


def test2():
    for i in range(5):
        print('{},{}'.format(threading.current_thread().getName(), i))
        time.sleep(1)
    raise Exception('这是子线程2中抛出的异常!')


if __name__ == '__main__':
    exe_tip = 'sys和traceback回溯异常信息'
    sth = 'hello world'
    # th = HookThread(target=test1, name='钩子线程1')
    # th2 = HookThread(target=test2, name='钩子线程2')
    th = threading.Thread(target=test1, name='钩子线程1')
    th2 = threading.Thread(target=test2, name='钩子线程2')
    try:
        th.start()

    # except Exception as e:
    #     traceback.print_exc()
    # try:
        th2.start()
        th.join()
        th2.join()
    except Exception as e:
        print("打印异常信息")
        traceback.print_exc()
    # while True:
    #     if not th.is_alive() and not th2.is_alive():
    #         break
    print('Done')
