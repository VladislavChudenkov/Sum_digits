def sum_digits(number):
    result = 0
    for figure in number:
        int(figure)
        result = result + int(figure)
    return result
number = input()
sum_digits(number)
result = sum_digits(number)
print(result)