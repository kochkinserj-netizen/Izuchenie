# Множества в циклах и функциях

langs = {'Java', 'Python', 'Ruby', 'C#', 'PHP', 'Kotlin'}

print(langs)

for lang in langs:
    print(lang)


tools = ['DevTools','Github','Linux','Jira','Confluence','Figma']

print(len(tools) == len(set(tools))) # проверка длин списка и множества из этого списка

tools_set = set(tools)
print(tools_set)
tools_list = list(tools)
print(tools_list)
print(tools.sort() == tools_list.sort())



def show_set(set_values):
    print(set_values)
    for leng in set_values:
        print(leng)




show_set(langs)


numbers = {1,2,3,4,5,6,7,8,9,0}

def set_filter(nums):
    big_numbers = [n for n in nums if n >=5]
    return set(big_numbers)
    # big_numbers = set()
    # for num in nums:
    #     if num > 5:
    #         big_numbers.add(num)
    # return big_numbers


print(set_filter(numbers))