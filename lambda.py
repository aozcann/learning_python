# def square(num): return num **2
square = lambda num : num ** 2

numbers = [1,3,5,9,11,10,4,8]

# result = list (map(square,numbers))
# result = list (map(lambda num : num ** 2,numbers))
# result = list (map(square,numbers))

# def check_even(num): return num %2 == 0
check_even = lambda num : num%2==0

# result = list(filter(check_even,numbers))
# result = list(filter(lambda num : num%2==0,numbers))
# result = list(filter(check_even,numbers))

result = check_even(numbers[2])

print(result)