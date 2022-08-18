def fib(n):
    a, b = 0, 1

    while a < n:
        a, b = b, a+b
        print(a)


fib(2000)

word = 'time'
print(word[0])
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
cat_tup = tup1 + tup2
print(cat_tup)
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
new_list = list_1 + list_2
sum_list = sum(list_1) + sum(list_2)
print(new_list)
print(sum_list)


def sum_list_element(first, second):
    new_list = []
    if len(first) == len(second):
        for i in range(0, len(first)):
            new_list.append(first[i]+second[i])
        return new_list


print(sum_list_element(list_1, list_2))
