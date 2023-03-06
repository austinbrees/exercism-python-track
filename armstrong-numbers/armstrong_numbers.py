def is_armstrong_number(number):
    str_value = str(number)
    length = len(str_value)
    return (number == sum(int(digit) ** length for digit in str_value))

print(is_armstrong_number(9474))