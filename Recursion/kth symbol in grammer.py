
# ======= Here we just find kth symbol from this grammer ===
# grammer is when N=1 and K=1 then it is 0.
#if N-1 is 0 then it is  0 1 
#if N-1 is 1 it is 1 0

def kth_symbol(N,K):

    if N==1 and K==1:
        return 0
    else:
        mid = (2**(N-1))/2

        if K > mid :
            a = kth_symbol(N-1,K-mid)
            return 1-a # here we take complement of our result bcoz here k > mid so here matching is complementry.
                
            
        else:
           return kth_symbol(N-1,K)
    
print(kth_symbol(4,8))
