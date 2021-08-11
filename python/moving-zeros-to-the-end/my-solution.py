def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(0)
            array.append(0)
    return array


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))