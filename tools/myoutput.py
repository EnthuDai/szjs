class MyOutput:
    @staticmethod
    def matrix_output(data, columns):
        for i in range(0, len(data)):
            if i % columns == columns - 1:
                print(data[i])
            else:
                print(data[i], end=' ')


if __name__ == "__main__":
    matrix = [1, 2, 3, 4]
    MyOutput.matrix_output(matrix, 2)
