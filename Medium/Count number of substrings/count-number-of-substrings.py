#User function Template for python3
from collections import defaultdict
class Solution:
    def count(self,s,k):
        i=0
        j=0
        ans=0
        d={}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
            while(len(d)>k):
                d[s[j]]-=1
                if d[s[j]]==0:
                    d.pop(s[j])
                j+=1
           
            ans=ans+i-j+1
        return ans
    def substrCount (self,s, k):
        # your code here
       
        return self.count(s,k)-self.count(s,k-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends