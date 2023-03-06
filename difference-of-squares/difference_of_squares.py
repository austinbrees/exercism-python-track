def square_of_sum(number):
    array = list(range(1,number + 1))
    total = 0
    
    for number in array:
        total += number
        new_total = total**2
    
    return new_total
    
        
def sum_of_squares(number):
    array = list(range(1,number + 1))
    total = 0
    
    for number in array:
        total += number**2
        
    return total


def difference_of_squares(number):
    diff = square_of_sum(number) - sum_of_squares(number)
    return diff


