def set_fun1(func1):
    print("执行外部操作1")
    def call_fun1():
        print("执行内部操作1")
        func1()
    return call_fun1


def set_fun2(func2):
    print("执行外部操作2")
    def call_fun2():
        print("执行内部操作2")
        func2()

    return call_fun2

@set_fun2
@set_fun1
def test():
    print("这是在测试")
test()