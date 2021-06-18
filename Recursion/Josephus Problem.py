# ========= Josephus Problem =======

'''
Problem Statement :
input -> We have two input n -> total no. of people
                           k -> no. of count who will we died
            output -> Print safe Position.

'''



n = 4
k = 8
out = []
for i in range(n):
    out.append(i+1)

print(out)

i = 0
k = k-1
l = k

def Josephus_Problem(k,out):
    global l
    if len(out) == 1 :
        print(f"{out} number person is saved")
    
    else:
        if n > l:
            index = k
            del out[index]
            k = (l + index) % len(out)

            Josephus_Problem(k,out)
        else:
            k = k % len(out)
            del out[k]
            Josephus_Problem(k,out)


   
Josephus_Problem(k,out)