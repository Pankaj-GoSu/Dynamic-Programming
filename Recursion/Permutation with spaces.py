# ======== Permuatation with spaces ====

'''
# Here problem stamenet is 
Let suppose we have string "abc" -->  it gives {a bc , ab c, a b c , abc } 

So we Make Recursion Tree for this String.

'''
inp = "abc"
out = "" + inp[0] # Here we add first element of string already becoz it is not come under recursion ut run only 1 time.
inp = inp[1:len(inp)] # we remove first element as it already include in output.
def Print_with_spaces(inp,out):

    if len(inp) == 0:
        print(out)
    elif len(inp) > 1 :
        op1 = out + " " + inp[0]
        op2 = out + inp[0]
        inp = inp[1:len(inp)]
        Print_with_spaces(inp,op1)
        Print_with_spaces(inp,op2)
    else:
        op1 = out + " " +inp[0]
        op2 = out + inp[0]
        inp = ""
        Print_with_spaces(inp,op1)
        Print_with_spaces(inp,op2)

Print_with_spaces(inp,out)



