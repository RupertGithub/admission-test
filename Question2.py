def count(input):
    word_count_dict = {}
    for c in input:
        if c in word_count_dict:
            word_count_dict[c]=word_count_dict[c]+1
        else:
            word_count_dict.update({c:1})
    return word_count_dict

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x'] 
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1} 



def group_by_key(input): 
    word_count_dict = {}
    for word_dict in input:
        if word_dict['key'] in word_count_dict:
            word_count_dict[word_dict['key']]=word_count_dict[word_dict['key']]+word_dict['value']
        else:
            word_count_dict.update({word_dict['key']:word_dict['value']})
    return word_count_dict

input2 = [ 
{'key': 'a', 'value': 3}, 
{'key': 'b', 'value': 1}, 
{'key': 'c', 'value': 2}, 
{'key': 'a', 'value': 3}, 
{'key': 'c', 'value': 5} 
] 
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}