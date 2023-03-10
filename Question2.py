def count(input):
    word_count_dict = {}
    for c in input:
        if c in word_count_dict:
            word_count_dict[c]=word_count_dict[c]+1
        else:
            word_count_dict.update({c:1})
    return word_count_dict

input1 = ['a','b','c','a','c','a','x']
print(count(input1))