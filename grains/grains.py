def square(number):
    array = list(range(1,65))
    if number in array:
        new_num = 2**(number - 1)
        return new_num
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    return sum(square(i) for i in range(1,65))
       
