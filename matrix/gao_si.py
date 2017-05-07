from tools.mymatrix import MyMatrix

"""高斯消元"""


class GaoSi:
    def __init__(self, index=0):
        self.matrix = MyMatrix(index)
        self.rows = self.matrix.rows
        self.columns = self.matrix.columns
        self.result = []

    """顺序消元
    is_liezhuyuan: 是否采用列主元
    """

    def sequence(self, is_liezhuyuan=False, show=False):
        if not is_liezhuyuan:
            print("--顺序消元--")
        else:
            print("--列主元消元--")
        count = 1
        for i in range(0, self.matrix.rows):
            if is_liezhuyuan:
                max_num = abs(self.matrix.get(i, i))
                max_index = i
                for k in range(i + 1, self.matrix.rows):
                    if abs(self.matrix.get(k, i)) > max_num:
                        max_index = k
                if max_index != i:
                    self.matrix.rows_change(i, max_index)
            for j in range(i + 1, self.matrix.rows):
                if abs(self.matrix.get(i, i)) >= 0.000001:
                    m = self.matrix.get(j, i) / self.matrix.get(i, i)
                    self.matrix.rows_operate(j, '-', i, m)
                    if show:
                        print("第", count, "次消元结果：")
                        self.matrix.output()
                        count += 1
                    print()
                else:
                    print("det A=0,无解")
                    return
        self.matrix.set_precision('%.3f')
        result = []
        for i in range(0, self.rows):
            tmp_sum = 0
            for j in range(0, i):
                tmp_sum += self.matrix.get(self.rows - 1 - i, self.columns - 1 - j - 1) * result[j]
            result.append((self.matrix.get(self.rows - i - 1, self.columns - 1) - tmp_sum) / self.matrix.get(
                self.rows - i - 1, self.columns - 2 - i))
        result.reverse()
        self.result = result


if __name__ == "__main__":
    gao_si = GaoSi(3)

    print("增广矩阵为")
    gao_si.matrix.output()

    gao_si.sequence(True, True)

    print("消元结果为")
    gao_si.matrix.output()

    print("最终结果为")
    print(gao_si.result)
