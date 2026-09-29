from typing import List

def read_integers() -> List[int]:
    numbers = input()
    str_nums = numbers.split(",")
    res = []
    for num in str_nums:
        res.append(int(num))
    return res


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
