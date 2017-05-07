#  拉格朗日差值多项式
import numpy as np
import matplotlib.pyplot as plt


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
    key = [0.1, 0.2, 0.3, 0.4, 0.5]
    value = [1.1052, 1.2214, 1.3499, 1.4918, 1.6487]
    lag = Lagrange(key, value, 1, 2)
    print(lag.calculate(0.285))
    t = np.arange(0.1, 0.6, 0.01)

    lag = Lagrange(key, value, 1, 2)

    # red dashes, blue squares and green triangles
    plt.plot(t, np.math.e ** t, 'g', t, lag.getValueArray(t), 'r')
    l = plt.axvline(x=0.2, ymin=0, linewidth=1, color='b', ls='--')
    l = plt.axvline(x=0.3, ymin=0, linewidth=1, color='b', ls='--')
    plt.show()

