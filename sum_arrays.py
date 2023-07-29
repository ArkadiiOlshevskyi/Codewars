def sum_array(data):
    result = 0
    for number in data:
        result += number
    return result



data_0 = [3]
data_1 = [3, 2.5, 4, 10, 32]
data_2 = [3, 2.5, 9.9, -1, -32]


print(sum_array(data_0))
print(sum_array(data_1))
print(sum_array(data_2))

