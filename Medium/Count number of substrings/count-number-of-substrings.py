#User function Template for python3
from collections import defaultdict
class Solution:
    def count(self,s,k):
        i=0
        j=0
        ans=0
        c=0
        d=[0]*26
        for i in range(len(s)):
            if d[ord(s[i])-ord('a')]>0:
                d[ord(s[i])-ord('a')]+=1
            else:
                d[ord(s[i])-ord('a')]=1
                c+=1
            while(c>k):
                d[ord(s[j])-ord('a')]-=1
               
                if d[ord(s[j])-ord('a')]==0:
                    c-=1
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