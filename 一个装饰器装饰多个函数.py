def set_fun(func):
    print("执行外部函数")
    def call_fun():
        print("执行内部函数")
        func()
    return call_fun

@set_fun
def test1():
    print("这是在测试1")
test1()

@set_fun
def test2():
    print("这是在测试2")

test2()


# def set_fun(func):
#     print("执行外部函数")
#     def call_fun():
#         func()
#         print("执行内部函数")
#     return call_fun
#
# @set_fun
# def test1():
#     print("这是在测试1")
#
# @set_fun
# def test2():
#     print("这是在测试2")
#
# test1()
# test2()