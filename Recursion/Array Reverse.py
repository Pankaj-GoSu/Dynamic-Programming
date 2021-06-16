#======= Here i reverse a array using recursion ========

def reverse(array):

    if len(array) == 1 :
        return array
    else:
        temp = array[-1]
        array.pop()
        reverse(array)
        array.insert(0,temp)
        return array

l = [3,4,5,6,7,1]

print(reverse(l))