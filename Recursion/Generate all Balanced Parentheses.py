# ======= Generate all Balanced Parentheses =========

'''
Problem Statement:

We have to Generate all Balanced Parentheses.
--> Input -> n = 2 output -> we have 4 brackets(two open , two close) and we have to put these 
                        brackets in such a way that we get balanced parentheses like (()) or ()().

'''
inp = 3
out = ""
c = inp
o = inp
def Balanced_Parentheses(o,c,out):
    ''' 
    Here i observe that when open and close brackets are equal we have only one output that is 
        we print open bracket ,now when open bracket less then close bracket we have two choices 
        we can print open bracket or close bracket. 
     ----> here mainly for Balanced Parantheses we do not make close bracket count (c) less then
            open bracket count so as both are equal i print open bracket and decrease its count
            of open bracket so again it is less then close bracket.
    '''
    
    if o == 0 and c == 0:
        print(out)

    else:

        if c > o and o != 0: 
            op1  = out + "("
            o = o - 1
            op2 = out + ")"
            c = c - 1
            Balanced_Parentheses(o,c+1,op1)
            Balanced_Parentheses(o+1,c,op2)
        elif c > o and o == 0:
            op = out + ")"
            c = c - 1
            Balanced_Parentheses(o,c,op)
        else:
            op = out + "("
            o = o - 1
            Balanced_Parentheses(o,c,op)
          

Balanced_Parentheses(o,c,out)