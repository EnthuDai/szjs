class StringToList:
    @staticmethod
    def to_int_list(data, split_character=' '):
        data = data.strip()
        str_list = data.split(split_character)
        res_list = []
        for value in str_list:
            res_list.append(int(value))
        return res_list

    @staticmethod
    def to_float_list(data, split_character=' '):
        data = data.strip()
        str_list = data.split(split_character)
        res_list = []
        for value in str_list:
            res_list.append(float(value))
        return res_list

    @staticmethod
    def to_str_list(data, split_character=' '):
        data = data.strip()
        str_list = data.split(split_character)
        return str_list
