from tools import StringToList
from tools import myoutput


class MyInput:
    @staticmethod
    # 输入矩阵
    # 返回一个列表，列表第一项为以一维存储的数据，第二项是数组行数，第三项为数组列数
    def matrix_input():
        print("请输入矩阵的行数列数,输入示例：4 4")
        para = StringToList.StringToList.to_int_list(input())
        while len(para) != 2:
            print("参数错误请重新输入！")
            para = StringToList.StringToList.to_int_list(input())
        print("请逐行输入数据")
        data = [0]*para[0]*para[1]
        for i in range(0, para[0]):
            row = StringToList.StringToList.to_int_list(input())
            for j in range(0, min(para[1], len(row))):
                data[i*para[1]+j] = row[j]
        print("矩阵打印：")
        myoutput.MyOutput.matrix_output(data, para[1])
        return [data, para[0], para[1]]


if __name__ == '__main__':
    MyInput.matrix_input()
