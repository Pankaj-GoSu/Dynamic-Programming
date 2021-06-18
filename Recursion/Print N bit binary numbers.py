#==== Print N bit binary numbers having more 1's than 0's and equal to  for any prefix ======

'''
Problem statement : 
Here we have to generate those strings whose prefixs are contain 1's greater then or equal to
no. of zeros .

Here --> Input - 3 Output -> {111,110,101} 
         Input -4 Output -> {1111,1110,1101,1100,1011,1010}

Here we generate string which has equal or greater number of 1's So that when we make 
prifix of these generated digits we will find that its prifix always has equal or greater no. of 1's

'''

# ===== With This Code I get 3 digit numbers which contain equal or greater no. of 1's ====
# inp = 4
# out = ""
# zero_count = 0
# one_count = 0

# def Print_Binary_Number(inp,out,one_count,zero_count):

#     if inp == 0:
#         print(out)

#     elif one_count > zero_count :
#         op1 = out + "1"
#         one_count = one_count + 1
#         op2 = out + "0"
#         zero_count = zero_count + 1
#         inp = inp - 1
#         Print_Binary_Number(inp,op1,one_count,zero_count-1)
#         Print_Binary_Number(inp,op2,one_count-1,zero_count)
#     elif one_count == zero_count and inp == 1:
#         op = out + "1"
#         one_count = one_count + 1
#         inp = inp - 1
#         Print_Binary_Number(inp,op,one_count,zero_count)
    
#     elif zero_count > one_count:
#         op = out + "1"
#         one_count = one_count + 1
#         inp = inp - 1
#         Print_Binary_Number(inp,op,one_count,zero_count)

#     elif one_count == zero_count and inp > 1:
#         op1 = out + "1"
#         one_count = one_count + 1
#         op2 = out + "0"
#         zero_count = zero_count + 1
#         inp = inp - 1
#         Print_Binary_Number(inp,op1,one_count,zero_count-1)
#         Print_Binary_Number(inp,op2,one_count-1,zero_count)
    

# Print_Binary_Number(inp,out,one_count,zero_count)
        

# ====== Code For Our Problem Statement ==============

inp = 4
out = "" 
zero_count = 0
one_count = 0

def Print_Numbers_For_Prefix(inp,out,one_count,zero_count):

    if inp == 0:
        print(out)
    
    elif one_count > zero_count:
        op1 = out + "1"
        # one_count = one_count + 1
        op2 = out + "0"
        # zero_count = zero_count + 1
        inp = inp - 1
        Print_Numbers_For_Prefix(inp,op1,one_count+1,zero_count)
        Print_Numbers_For_Prefix(inp,op2,one_count,zero_count+1)

    elif one_count == zero_count  :
        op = out + "1"
        # one_count = one_count + 1
        inp = inp - 1
        Print_Numbers_For_Prefix(inp,op,one_count+1,zero_count)

Print_Numbers_For_Prefix(inp,out,one_count,zero_count)