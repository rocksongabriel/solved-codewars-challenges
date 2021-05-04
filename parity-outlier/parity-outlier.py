def find_outlier(integers):
    odd_numbers = [num for num in integers if is_odd(num)]
    even_numbers = [num for num in integers if is_even(num)]
    return odd_numbers[0] if len(odd_numbers) < len(even_numbers) else even_numbers[0]

def is_even(number):
    """check if a number is even"""
    return number % 2 == 0

def is_odd(number):
    """check if a number is odd"""
    return number % 2 != 0


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))