# 迭代法求非线性方程组的根
import math


class Iteration:
    def __init__(self):
        self.result = []

    @staticmethod
    def get_value(parameter):
        # return 0.5 * (10 - parameter ** 3) ** (1 / 2.0)
        return (parameter+1)**(1/3)

    def calculate(self, parameter, precision, show=True):
        tmp = self.get_value(parameter)
        count = 0
        if show:
            print("第", count, "次迭代结果：", parameter)
            count += 1
            print("第", count, "次迭代结果：", tmp)
            count += 1
        while math.fabs(tmp - parameter) > precision:
            parameter = tmp
            tmp = self.get_value(parameter)
            if show:
                print("第", count, "次迭代结果：", tmp)
                count += 1
        self.result.append(tmp)

if __name__ == "__main__":
    iter = Iteration()
    iter.calculate(1.5, 0.00001)
    print("求根结果为x=", iter.result)
