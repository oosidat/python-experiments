def partial_list_search(list_of_words, target):
    return filter(lambda x: target in x, list_of_words)

duplicate_s = "Duplicate word: "

def partial_str_search(string_of_words, target):
    str_lst = map(lambda x: x.lower(), string_of_words.split())
    match_list = partial_list_search(str_lst, target)
    return match_list

print partial_str_search('Apples Bananas ORANGES', 'banana')

print partial_str_search('Apples OranGes Bananas ORANGES oranges', 'an')
    
