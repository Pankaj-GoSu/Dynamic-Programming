# ======== Permutauion With Case Change ==========

'''
# Problem statement is:
--> Input is string "ab" And Ouput for this string is  {ab,aB,Ab,AB}. 

'''

inp = "abc" # this is test input
out = "" # we initializing output


def Print_Case_Change(inp,out):
   
    if len(inp) == 0:
        print(out)
    
    elif len(inp) > 1:

        op1 = out + inp[0]
        op2 = out + inp[0].upper()
        inp = inp[1:len(inp)]
        Print_Case_Change(inp,op1)
        Print_Case_Change(inp,op2)
    else:
        op1 = out + inp[0]
        op2 = out + inp[0].upper()
        inp = ""
        Print_Case_Change(inp,op1)
        Print_Case_Change(inp,op2)

Print_Case_Change(inp,out)