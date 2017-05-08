#  雅可比迭代法求方程组的根
import math

from tools.mymatrix import MyMatrix


class Jacobi:
    def __init__(self, yuanshu, xishu, changshu):
        self.xishu = xishu
        self.changshu = changshu
        self.yuanshu = yuanshu

    def calculate(self, it_num, precision, is_show=False):
        count = 1
        if is_show:
            print("初始迭代参数为：", it_num.data)
        if len(it_num.data) != self.yuanshu:
            raise Exception("初始迭代值长度与方程组元数不匹配")
        result = MyMatrix.add(MyMatrix.multiply(self.xishu, it_num), self.changshu)
        while not Jacobi.check_precision(it_num.data, result.data, precision):
            if is_show:
                print("第", count, "次迭代结果为：", result.data)
                count += 1
            it_num = result
            result = MyMatrix.add(MyMatrix.multiply(self.xishu, it_num), self.changshu)
        if is_show:
            print("第", count, "次迭代结果为：", result.data)
        return result

    @staticmethod
    def check_precision(data1, data2, precision):
        for i in range(0, len(data1)):
            if math.fabs(data1[i] - data2[i]) > precision:
                return False
        return True

if __name__ == "__main__":
    xishu = MyMatrix(-1)
    xishu.data = [0, -2, -3, 0]
    xishu.rows = 2
    xishu.columns = 2

    changshu = MyMatrix(-1)
    changshu.data = [5, 5]
    changshu.rows = 2
    changshu.columns = 1

    it_num = MyMatrix(-1)
    it_num.columns = 1
    it_num.rows = 2
    it_num.data = [0, 0]

    jac = Jacobi(2, xishu, changshu)
    result = jac.calculate(it_num, 0.001, True)
    print("最终结果为：", result.data)

    # xishu = MyMatrix(-1)
    # xishu.data = [0, 1, -1/2, -1/3, 0, 2/3, -1, -1, 0]
    # xishu.rows = 3
    # xishu.columns = 3
    #
    # changshu = MyMatrix(-1)
    # changshu.data = [1/2, 1/3, 6]
    # changshu.rows = 3
    # changshu.columns = 1
    #
    # it_num = MyMatrix(-1)
    # it_num.columns = 1
    # it_num.rows = 3
    # it_num.data = [0, 0, 0]
    #
    # jac = Jacobi(3, xishu, changshu)
    # result = jac.calculate(it_num, 0.001, True)
    # print("最终结果为：", result.data)

