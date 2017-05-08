from tools import StringToList

"""自定义矩阵类"""


class MyMatrix:
    def __init__(self, index=0):
        self.data = []
        self.rows = 0
        self.columns = 0
        if index == -1:
            pass
        elif index == 0:
            self.input()
        elif index == 1:
            self.rows = 3
            self.columns = 4
            self.data = [0.001, 2, 3, 1, -1, 3.712, 4.623, 2, -2, 1.072, 5.643, 3]
        elif index == 2:
            self.rows = 3
            self.columns = 4
            self.data = [1, 1, 1, 6, 1, 3, -2, 1, 2, -2, 1, 1]
        elif index == 3:
            self.rows = 2
            self.columns = 3
            self.data = [0.00001, 2, 1, 2, 3, 2]

    def input(self):
        print("请输入矩阵的行数列数,输入示例：4 4")
        para = StringToList.StringToList.to_int_list(input())
        while len(para) != 2:
            print("参数错误请重新输入！")
            para = StringToList.StringToList.to_int_list(input())
        print("请逐行输入数据")
        data = [0] * para[0] * para[1]
        for i in range(0, para[0]):
            row = StringToList.StringToList.to_float_list(input())
            for j in range(0, min(para[1], len(row))):
                data[i * para[1] + j] = row[j]
        self.data = data
        self.rows = para[0]
        self.columns = para[1]

    def output(self):
        for i in range(0, len(self.data)):
            # if i % self.columns == self.columns - 1:
            #     if self.data[i]%1 !=0:
            #         print("%-.2f" % self.data[i])
            #     else:
            #         print("%-5d" % self.data[i])
            # else:
            #     if self.data[i]%1 != 0:
            #         print("%-.2f" % self.data[i], end=' ')
            #     else:
            #         print("%-5d" % self.data[i], end=' ')

            if i % self.columns == self.columns - 1:
                print(self.data[i])
            else:
                print(self.data[i], end=' ')

    def get(self, row, column):
        if self.rows > row >= 0 and self.columns > column >= 0:
            return self.data[row * self.columns + column]
        else:
            print("get 操作，行号列号超出范围")
            return 0

    def get_row(self, row):
        if self.rows > row >= 0:
            return self.data[row * self.columns:row * self.columns + self.columns]
        else:
            print("行号不符合要求")
            return []

    """指定某一行进行加减乘除一个给定的数
    row 为行号
    oper为操作符号，有 + - * /
    para为要操作的值"""

    def row_operate(self, row, oper, para):
        if self.rows > row >= 0:
            for i in range(row * self.columns, (row + 1) * self.columns):
                if oper == '+':
                    self.data[i] += para
                elif oper == '-':
                    self.data[i] -= para
                elif oper == '*':
                    self.data[i] *= para
                elif oper == '/':
                    if para == 0:
                        print("row_operate 行操作，除数不能为零")
                    else:
                        self.data[i] /= para
                else:
                    print("row_operate 操作符只能为+ - * /")
                    return
        else:
            print("row_operate 行号不符合要求")

    """row1 整体 加减乘 row2*para
    row1 被操作的行
    oper 操作类型，有 + - * 三种
    row2 需要用到的行
    para 默认为1
    """

    def rows_operate(self, row1, oper, row2, para=1):
        if self.rows > row1 >= 0 and self.rows > row2 >= 0:
            for i in range(0, self.columns):
                if oper == '+':
                    self.data[row1 * self.columns + i] += para * self.data[row2 * self.columns + i]
                elif oper == '-':
                    self.data[row1 * self.columns + i] -= para * self.data[row2 * self.columns + i]
                elif oper == '*':
                    self.data[row1 * self.columns + i] *= para * self.data[row2 * self.columns + i]
                else:
                    print("rows_operate 暂不支持" + oper + "操作")
                    return
        else:
            print("rows_operate 行号不符合要求")

    """设置数值的精度，传入采用标准输出格式"""

    def set_precision(self, pre):
        for i in range(0, self.rows * self.columns):
            self.data[i] = float(pre % self.data[i])

    """交换指定的两行数据"""

    def rows_change(self, row1, row2):
        for i in range(0, self.columns):
            tmp = self.get(row1, i)
            self.data[row1 * self.columns + i] = self.data[row2 * self.columns + i]
            self.data[row2 * self.columns + i] = tmp

    """两个矩阵相乘"""

    @staticmethod
    def multiply(matrix1, matrix2):
        if not (isinstance(matrix1, MyMatrix) and isinstance(matrix2, MyMatrix)):
            raise Exception("非矩阵类型无法相乘")
        if matrix1.columns != matrix2.rows:
            raise Exception("此两个矩阵无法相乘")
        data = [0]*matrix1.rows*matrix2.columns
        for i in range(0, matrix2.columns):
            for j in range(0, matrix1.rows):
                tmp = 0
                for k in range(0, matrix1.columns):
                    tmp += matrix1.get(j, k)*matrix2.get(k, i)
                data[j*matrix2.columns+i] = tmp
        result = MyMatrix(-1)
        result.data = data
        result.rows = matrix1.rows
        result.columns = matrix2.columns
        return result

    """矩阵加法"""
    @staticmethod
    def add(matrix1, matrix2):
        if matrix1.columns != matrix2.columns:
            raise Exception("加法操作--矩阵列数不同")
        if matrix1.rows != matrix2.rows:
            raise Exception("加法操作--矩阵行数不同")
        result = MyMatrix(-1)
        result.rows = matrix2.rows
        result.columns = matrix2.columns
        data = [0]*matrix2.columns*matrix2.rows
        for i in range(0, matrix2.rows*matrix1.columns):
            data[i] = matrix1.data[i] + matrix2.data[i]
        result.data = data
        return result

if __name__ == "__main__":
    matrix = MyMatrix(-1)
    matrix.columns = 2
    matrix.rows = 2
    matrix.data = [0, -2, -3, 0]

    matrix2 = MyMatrix(-1)
    matrix2.columns = 1
    matrix2.rows = 2
    matrix2.data = [0, 0]

    matrix3 = MyMatrix(-1)
    matrix3.columns = 1
    matrix3.rows = 2
    matrix3.data = [5, 5]

    MyMatrix.add(MyMatrix.multiply(matrix, matrix2), matrix3).output()
