"""计算某函数的执行时间"""
import time


def set_run(func):
    print("即将外部执行")
    def call_run():
        print("这里是内部执行")
        func()
        print(time.time())
    return call_run

@set_run
def test():
    print("============这是计算时间的分割线============")
test()