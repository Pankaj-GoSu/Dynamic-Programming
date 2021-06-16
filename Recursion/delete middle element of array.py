# Here i writing program for deleting middle element of array.

# for Middle element k = (len(array)//2) + 1



def delete_mid(array,k):
    
    if k == 1 :
        array.pop()
        return
    else:
        temp = array[-1]
        array.pop()
        delete_mid(array,k-1)
        array.append(temp)
        return array

array = [2,3,4,5,6,5,6]
if len(array) % 2 == 0:
    k = (len(array)//2)
else:
    k = (len(array)//2) + 1

print(delete_mid(array,k))