import math


# 二分法求非线性方程组的根
class Dichotomy:
    def __init__(self):
        self.result = []

    @staticmethod
    def get_value(parameter):
        return math.sin(parameter) - math.pow(parameter, 2) / 4

    def scope_calculate(self, left, right, precision, show=True):
        middle = (left + right) / 2
        while math.fabs(self.get_value(middle)) > math.fabs(precision):
            if show:
                print(self.get_value(middle))
            if self.get_value(middle) * self.get_value(left) < 0:
                right = middle
            else:
                left = middle
            middle = (left + right) / 2
        return middle

    def calculate(self, left, right, precision, step):
        begin = left
        while begin < right:
            if begin + step < right:
                end = begin + step
            else:
                end = right
            if self.get_value(begin) * self.get_value(end) < 0:
                self.result.append(self.scope_calculate(begin, end, precision))
            if begin + step < right:
                begin = begin + step
            else:
                begin = right


if __name__ == "__main__":
    di = Dichotomy()
    di.calculate(-100, 200, 0.001, 0.5)
    print(di.result)
