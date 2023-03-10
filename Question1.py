def find_max(numbers):
    max = numbers[0]
    for n in numbers[1:]:
        if n>max:
            max = n
    return max

def find_position(numbers, target):
    size = len(numbers)
    for i in range(0,size):
        if numbers[i]==target:
            return i
    return -1

print(find_max([1, 2, 4, 5]) ); # should print 5 
print(find_max([5, 2, 7, 1, 6]) ); # should print 7 
print(find_position([5, 2, 7, 1, 6], 5)) # should print 0 
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2 
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one) 
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1