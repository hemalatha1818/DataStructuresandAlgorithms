#User function Template for python3
from collections import defaultdict
class Solution:
    def countOfSubstrings(self, S, K):
        # code here
        ans=0
        d=defaultdict(int)
        for i in range(K):
            d[S[i]]+=1
            
        if len(d)==K-1:
            ans+=1
            
        for j in range(K,len(S)):
            if d[S[j-K]]!=1:
                d[S[j-K]]-=1
            else:
                del d[S[j-K]]
            d[S[j]]+=1
            if len(d)==K-1:
                ans+=1
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        K=int(input())
        
        ob = Solution()
        print(ob.countOfSubstrings(S,K))
# } Driver Code Ends