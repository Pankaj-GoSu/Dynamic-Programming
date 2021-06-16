# ======= Here we sort an array ========

array = input("""Enter Your array seprate by "," """)
array =array.split(",")
# array1 = [2,1,4,3,5] # let this is our array 

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

   
print(f"Your sort array is {sort(array)}")