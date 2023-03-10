def find_max(numbers):
    max = numbers[0]
    for n in numbers[1:]:
        if n>max:
            max = n
    return max

print(find_max([1,2,4,5]))
print(find_max([5,2,7,1,6]))

def find_position(numbers, target):
    size = len(numbers)
    for i in range(0,size):
        if numbers[i]==target:
            return i
    return -1

print(find_position([5,2,7,1,6],5))
print(find_position([5,2,7,1,6],7))
print(find_position([5,2,7,7,7,1,6],7))
print(find_position([5,2,7,1,6],8))
