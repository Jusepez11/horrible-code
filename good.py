#Recives an array of numbers and outputs the sum of them
def sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

print(sum([10,10,2,1,3,4]))

#Recives an array of numbers and outputs the difference of them
def subs(nums):
    total = 0
    for i in nums:
        total -= i
    return total

print(sum([10,10,2,1,3,4]))

#Recives an array of numbers and outputs the multiplication of them
def multiply(nums):
    total = 0
    for i in nums:
        total *= i
    return total

print(sum([10,10,2,1,3,4]))