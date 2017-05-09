from matrix.gao_si import GaoSi
from tools.mymatrix import MyMatrix
import numpy as np
import matplotlib.pyplot as plt


class ZuiXiaoErCheng:
    def __init__(self, key, value):
        if len(key) != len(value):
            raise Exception("key的长度与value长度不一致")
        self.data = key + value
        self.key = key
        self.value = value
        self.result = []

    def calculate(self, is_show=False):
        tmp1 = 0
        tmp2 = 0
        tmp3 = 0
        tmp4 = 0
        for i in range(0, len(self.key)):
            tmp1 += self.key[i]
            tmp2 += self.key[i] ** 2
            tmp3 += self.value[i]
            tmp4 += self.value[i] * self.key[i]
        matrix = MyMatrix(-1)
        matrix.rows = 2
        matrix.columns = 3
        matrix.data = [len(self.key), tmp1, tmp3, tmp1, tmp2, tmp4]

        gaosi = GaoSi(matrix)
        gaosi.sequence(True, is_show)
        # print(gaosi.result)
        self.result = gaosi.result

    def output(self, x="x", y="y"):
        print("一次多项拟合结果：", self.get_expression(x, y))

    def get_expression(self, x="x", y="y"):
        return str(y)+"=" + str(self.result[0]) + "+" + str(self.result[1]) + str(x)

    def set_result_precision(self, pre):
        for i in range(0, len(self.result)):
            self.result[i] = float(pre % self.result[i])


if __name__ == "__main__":
    key = [1, 2, 4, 6, 8, 10]
    value = [1.8, 3.7, 8.2, 12.0, 15.8, 20.2]
    # key = [36.9, 46.7, 63.7, 77.8, 84.0, 87.5]
    # value = [181, 197, 235, 270, 283, 292]
    test = ZuiXiaoErCheng(key, value)
    test.calculate()
    test.set_result_precision("%.3f")
    test.output("i", "V")

    #  绘制图像
    t = np.arange(key[0] - 1, key[-1] + 1, 0.2)

    plt.plot(t, test.result[0] + t * test.result[1], label=test.get_expression("i", "V"), color="green", linewidth=1)
    plt.plot(key, value, 'ro')
    plt.legend()
    plt.show()
