# ====== Here we print unique subsets.===========

inp = "aab" # test input 
# {this give us {"",b,a,ab,a,ab,aa,aab} here we se wee get subsets are repeating}
op = ""
subset_list = [] # in this list we store unique subset
def print_unique_subset(inp,out):

    if len(inp)  == 0:
        if out in subset_list:
            pass
        else:
            subset_list.append(out)
    
    elif len(inp) > 1:
        op1 = out 
        op2 = out
        op2 = op2 + inp[0]
        inp = inp[1:len(inp)]
        print_unique_subset(inp,op1)
        print_unique_subset(inp,op2)
    
    else: # Here length of input is 0.
        op1 = out 
        op2 = out
        op2 = op2 + inp[0]
        inp = ""
        print_unique_subset(inp,op1)
        print_unique_subset(inp,op2)

print_unique_subset(inp,op)

for i in subset_list:
    print(i)


# Powerset : all subset of a set.
'''
substring : continues part like in {abc: a ,b, c, ab , bc,abc -> These all are substrings} { ac --> this is not substring bcoz not continues}

subsequence : here we also take{ac(which we not take in substring)} but here order is important like {ca} is not allowed

subset : here order is allowed .

'''
