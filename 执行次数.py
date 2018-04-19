import time

num = 0
def set_run(func):
    def call_run():
        print("----------------------------------------------------")
        print("执行外部操作")
        func()
        global num
        num += 1.
        print("执行次数为%d" %num)
    return call_run

@set_run
def test():
    print("================这是计数的分割线==============")
while True:
    test()
    time.sleep(2)