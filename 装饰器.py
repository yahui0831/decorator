def set_fun(func):
    print("执行了外部函数")
    def call_fun():
        print("执行了内部函数")
        print('即将执行test')
        func()
        print("func指向test，test执行完毕")
    return call_fun


@set_fun  # 相当于test = set_fun(test)
def test():
    print("==========这是测试的分割线==========")
test()