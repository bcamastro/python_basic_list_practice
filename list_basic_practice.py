# Given a list, write a Python program to swap first and last element of the list.
# ex: Input : [12, 35, 9, 56, 24] Output : [24, 35, 9, 56, 12] Input : [1, 2, 3] Output : [3, 2, 1]

def firstLast(alist):
    alist[0] , alist[-1] = alist[-1], alist[0]
    return alist

alist = [1,2,3,4,5]
print (firstLast(alist))

#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 
#ex: Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

def swapElements(swap_list, pos1, pos2):
    pos1 = pos1-1
    pos2 = pos2-1
    swap_list[pos1], swap_list[pos2] = swap_list[pos2], swap_list [pos1]
    return swap_list

swap_list = [23,65,19,90] 
pos1 = 1 
pos2 = 3
print(swapElements(swap_list, pos1, pos2))

# find maximum of two numbers
# ex: a = 2 b = 6 
# max = 6
#ex: a = -1 b = -5
#max = -1

def max(a,b):
    if a > b:
        return a
    else:
        return b
    
print(max(-3,-1))


#Find minimum of two numbers
#ex: a = 1 b = 3 min = 1
#ex  a = -1 b = -7 min = -7

def min(c,d):
    if c < d:
        return c
    else:
        return d

print(min(250,-100))

#check if element is in list

elementList = [1,2,3,4,5,6,7,6,5,45,100]

i = 10
if i in elementList:
    print("in list")
else:
    print('not in list')

