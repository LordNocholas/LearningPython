
my_dict = {}

my_set = set()

my_set1 = {'dog', 'cat', 'dog'}
my_set2 = {'dog', 'car'}

print(my_set1 & my_set2)

set1 = set('camels')
set2 = set('cats')

# print(set1)
# print(set2)

# letters in set1 but not set2
print(set1 - set2)
# letters in set1 or set2
print(set1 | set2)
# letters in set1 and set2
print(set1 & set2)
# letters in set1 or set2 but not both
print(set1 ^ set2)
