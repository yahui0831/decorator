def set_fun(func):
    print("执行了外部操作")
    def call_fun(*args, **kwargs):
        print("执行了内部操作")
        return func(*args, **kwargs)
    return call_fun


@set_fun  # test = set_fun(test)
def test(*args, **kwargs):
    print(args)
    print(kwargs)
    return 100
test()
# test(123, a=111)
# test (1111,222,333,a=121)
#
# print(test(123, a=111))
# print(test (1111,222,333,a=121))
