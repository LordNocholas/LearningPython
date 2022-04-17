import numpy as np

x = 100

# list()

my_list = list(range(x))


# for loop
my_list1 = []

for i in range(x):
    my_list1.append(i)
    
# list comprehension
my_list2 = [i for i in range(x)]

# list multiplication
my_list3 = [2] * x

# numpy array

my_list4 = np.arange(x)

print(my_list3)


