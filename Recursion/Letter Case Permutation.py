# ======== Letter Case Permutation =========

'''
Problem Statement is :
Here we get any thing in input inclueded characters and numbers
let we have input -> {a1B2} We get Output -> {a1b2,a1B2,A1b2,A1B2}

'''
inp = "a1B2" # Test Input

# for i in digits:
#     if i == x[1]:
#         print("not allowed")

out = "" # here we initialize our output.

def Print_Letter_Case(inp,out):
    digits = ["0","1","2","3","4","5","6","7","8","9"]

    if len(inp) == 0:
        print(out)

    elif len(inp) > 1:
        if inp[0] in digits: # if it is digit 
            op = out + inp[0]
            inp = inp[1:len(inp)]
            Print_Letter_Case(inp,op)

        else:
            op1 = out + inp[0].lower()
            op2 = out + inp[0].upper()
            inp = inp[1:len(inp)]
            Print_Letter_Case(inp,op1)
            Print_Letter_Case(inp,op2)
    else:
        if inp[0] in digits:
            op = out + inp[0]
            inp = ""
            Print_Letter_Case(inp,op)

        else:
            op1 = out + inp[0].lower()
            op2 = out + inp[0].upper()
            inp = ""
            Print_Letter_Case(inp,op1)
            Print_Letter_Case(inp,op2)

Print_Letter_Case(inp,out)
            
