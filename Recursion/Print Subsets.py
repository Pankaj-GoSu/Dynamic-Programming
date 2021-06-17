# ======== Here We PrintSubset of any string ==========

# like {ab:"",a,b,ab} these 4 are subset of ab string.

inp = "abc" # test input

op ="" # we initialize output
def print_subset(inp,out):
    
    if len(inp) == 0: # base condition
        print(out)
        return
    
    elif len(inp)> 1:
        op1 = out
        op2 = out
        op2 = op2 + inp[0]
        inp = inp[1:len(inp)]
        print_subset(inp,op1)
        print_subset(inp,op2)
    else: # this is when length of input is 1 
        op1 = out
        op2 = out
        op2 = op2 + inp[0]
        inp = ""
        print_subset(inp,op1)
        print_subset(inp,op2)

print("subsets Are:")
print_subset(inp,op)