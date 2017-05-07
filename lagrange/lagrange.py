#  拉格朗日差值多项式
import numpy as np
import matplotlib.pyplot as plt
import math


class Lagrange:
    def __init__(self, key, value, begin, size):
        self.size = size
        self.begin = begin
        self.key = key
        self.value = value

    def calculate(self, parameter):
        if self.size < 2:
            raise (Exception, "点数必须大于等于2")
        sum = 0
        for i in range(self.begin, self.begin + self.size):
            j = 0
            tmp = self.value[i]
            for j in range(0, self.size):
                if j != i - self.begin:
                    tmp *= (parameter - self.key[j + self.begin]) / (self.key[i] - self.key[j + self.begin])
            sum += tmp
        return sum

    def getValueArray(self, key_array):
        data = []
        for i in key_array:
            data.append(self.calculate(i))
        return data


if __name__ == "__main__":
    key = [1, 2, 3, 4, 5]
    value = [math.sin(1), math.sin(2), math.sin(3), math.sin(4), math.sin(5)]
    lag = Lagrange(key, value, 1, 3)
    print(lag.calculate(2.5))

    t = np.arange(-0.5, 8, 0.1)
    data = []
    for item in t:
        data.append(math.sin(item))
    # red dashes, blue squares and green triangles
    plt.plot(t, data, label="sin(x)", color="green", linewidth=1)
    plt.plot(t, lag.getValueArray(t), 'r', label="pao wu")
    plt.axvline(x=2, ymin=0, ymax=4, linewidth=1, color='b', ls='--')
    plt.axvline(x=3, ymin=0, ymax=9, linewidth=1, color='b', ls='--')
    plt.axvline(x=4, ymin=0, ymax=9, linewidth=1, color='b', ls='--')
    plt.axvline(x=2.5, ymin=0, ymax=9, linewidth=1, color='y', ls='--')
    plt.axhline(y=0, linewidth=1)

    # Y轴的范围
    plt.ylim(-1.2, 1.2)

    # 显示图示
    plt.legend()
    plt.show()
