#User function Template for python3

import math
class Solution:
    def permutationCoeff(self,n, k):
        # Code here
        N=math.factorial(n)
        r=math.factorial(n-k)
        val=N//r
        return(val%1000000007)
