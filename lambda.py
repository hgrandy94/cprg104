from time import sleep

# lambdas are anonymous functions
# they are used to create small functions that are not needed later
# they are also used to pass functions as arguments to other functions
# they are also used to return functions from other functions

# def add(x, y):
#     return x + y

# print(add(2, 3))

# alternatively, we could use a lambda function
# lambda functions are defined with the lambda keyword
# print(2 + 3)

# add = lambda x, y: x + y
# print(add(2, 3))


def my_slow_pow(x):
    result = 2 ** x
    sleep(result)
    return result

# slow to show that maps are lazy
# powers_of_two = map(lambda x: my_slow_pow(x), range(4))
# for power in powers_of_two:
#     print(power)

# powers_of_two = map(my_slow_pow, range(4))
# moded_power_of_two = map(lambda x: x % 3, powers_of_two)
# print(list(moded_power_of_two))

# powers_of_two = [my_slow_pow for x in range(4)]
# print(powers_of_two)

powers_of_two = map(lambda x: 2 ** x, range(6))
results_greater_than_10 = filter(lambda x: x > 10, powers_of_two)
print(list(results_greater_than_10))
