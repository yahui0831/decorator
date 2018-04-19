# 函数的情况
    # 1.无参无返回
    # 2.有参无返回
    # 3.无参有返回
    # 4.有参有返回


# """无参无返回"""
# def set_fun(func):
#     def call_fun():
#         print("执行了内部函数")
#         func()
#     return call_fun
#
# # @set_fun
# def test():
#     print("测试已完成")
#     print("=========这是完成的分割线======")
#
# #装饰前的test是func指向的
# #装饰后的test是call_fun指向
# test()



# """有参无返回"""
# def set_fun(func):
# 	def call_fun(*args,**kwargs):
# 		func(*args,**kwargs)
# 	return call_fun
#
# @set_fun # test = set_fun(test)
# def test(*args,**kwargs):
# 	print(args)
# 	print(kwargs)
# test(123, a=5)


# """无参有返回"""
# def set_fun(func):
#     def call_fun():
#         return func
#     return call_fun
#
# def test():
#     return 100
#
# print(test())


"""有参有返回"""
def set_fun(func):
    def call_fun(*args, **kwargs):
        print("执行内部操作")
        return func(*args, **kwargs)
    return call_fun

def test(*args, **kwargs):
    print(args)
    print(kwargs)
    return args
test(1111, a=9)
