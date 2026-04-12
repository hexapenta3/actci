import os


# 1から10までの数字をlistで返す関数
def get_numbers():
    """
        1から10までの数字をlistで返す関数
    """
    print('func: get_numbers')
    return list(range(1, 11))




if __name__ == "__main__":
    numbers = get_numbers()
    print(numbers)