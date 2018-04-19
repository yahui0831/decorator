"""闭包使用场景---汇率换算"""

def set_fun(rate):
    def call_fun(money):
        print(rate*money)
    return call_fun

count_usa = set_fun(0.65)
count_usa(1000)

