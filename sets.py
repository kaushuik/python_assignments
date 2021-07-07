# Remove duplicate values of a list a=[1,2,3,4,1,2,3,10]
from typing import List


def assign_1():
    a = [1, 2, 3, 4, 1, 2, 3, 10]
    m = list[set(a)]
    print("the list without the repeated values is: ", m)
    # #or else using loops
    list1 = []  # need detailing on this approach of defining the ist with input types
    print(len(list1))
    a1 = [1, 2, 3, 4, 1, 2, 3, 10]
    for i in range(len(a1)):
        count = 0
        for j in range(i + 1):
            if a1[i] == a1[j]:
                count = count + 1
        if count == 1:
            list1.append(a1[i])
    print("the updated list is : ", list1)


def assign_2():

    s1 = set([7, 9, 12, 7, 9])

    s2 = set(['abc', 12, 'b', 'car', 7, 10, 12])

    s3 = set([12, 14, 12, 'ab'])
    print(s1, s2, s3)
    print("Intersection s1 and s2 is : ", s1 & s2)

    print(s1 | s2)
    print('b' in s2)
    print('ab' in s2)
    print('ab' in s3)
    print(s2.discard(12))
    print((s1 & s2) ^ s3)


assign_2()

