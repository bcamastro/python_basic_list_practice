# Given a list, write a Python program to swap first and last element of the list.
# ex: Input : [12, 35, 9, 56, 24] Output : [24, 35, 9, 56, 12] Input : [1, 2, 3] Output : [3, 2, 1]

def first_last(alist):
    alist[0] , alist[-1] = alist[-1], alist[0]
    return alist

alist = [1,2,3,4,5]
print (first_last(alist))

#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 
#ex: Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

def swap_elements(swap_list, pos1, pos2):
    pos1 = pos1-1
    pos2 = pos2-1
    swap_list[pos1], swap_list[pos2] = swap_list[pos2], swap_list [pos1]
    return swap_list

swap_list = [23,65,19,90] 
pos1 = 1 
pos2 = 3
print(swap_elements(swap_list, pos1, pos2))