# ======= Here we sort an array ========

# array = input("Enter Your array seprate by ,")
# array =array.split(",")
array1 = [2,1,4,3,5] # let this is our array 

# print(array1)
# Desire Output after sorting is -> [1,2,3,4,5]

def insert(array,element):
    if len(array) == 0 or element >= array[-1]:
        array.append(element)
        return 
    else:
        val = array[-1]
        array.pop()
        insert(array,element)
        array.append(val)
    

def sort(array):

    if len(array) == 1:
        return 
    
    else:
        temp = array[-1]
        array.pop()
            # print(array)
        sort(array)
        insert(array,temp)
        return array      



        
        
        
        

# def insert(array,element):
#     if len(array) == 0 or element > array[len(array)-1]:
#         array.append(element)
#         return 
#     else:
#         temp = array[len(array)-1]
#         array.pop()
#         insert(array,temp)
#         array.append(temp)
#         return array
   
# def sorting(arr):

#     #Base Condition
#     if len(arr) == 1:
#         return
#     else:
#     #Induction
#         last_num = arr[-1]
#         arr.pop()
#         sorting(arr)
#         insert(arr, last_num)

#     return arr

# def insert(arr, last_num):

#     #Base Condition
#     if len(arr) == 0 or arr[-1] <= last_num:
#         arr.append(last_num)
#         return
#     else:
#     #Induction
#         val = arr[-1]
#         arr.pop()
#         insert(arr, last_num)
#         arr.append(val)
        


print(sort(array1))