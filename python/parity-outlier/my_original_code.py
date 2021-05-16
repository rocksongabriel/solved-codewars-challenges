def find_outlier(integers):
    #  checking for an even number
    if get_operation_type(integers) == False:
        map_result = map(is_even, integers)
        map_result_list = [value for value in map_result]
        position_of_outlier = map_result_list.index(True)
        return integers[position_of_outlier]
    # checking for an odd number
    elif get_operation_type(integers) == True:
        map_result = map(is_odd, integers)
        map_result_list = [value for value in map_result]
        position_of_outlier = map_result_list.index(True)
        return integers[position_of_outlier]

def get_operation_type(numbers):
    # testing first 3 numbers to know which type of check to do
    even_num = 0
    odd_num = 0
    for number in numbers[:3]:
        if is_even(number):
            even_num += 1
    for number in numbers[:3]:
        if is_odd(number):
            odd_num += 1
    
    if even_num >= 2:
        return True # if it returns True, we will be checking for an odd number
    elif odd_num >= 2:
        return False # if it returns False, we will be checking for an even number

def is_even(number):
    """check if a number is even"""
    return number % 2 == 0

def is_odd(number):
    """check if a number is odd"""
    return number % 2 != 0


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))