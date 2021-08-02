"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

https://www.codewars.com/kata/515e271a311df0350d00000f

"""
def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum = sum + int(i**2)
    return sum

"""
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
"""