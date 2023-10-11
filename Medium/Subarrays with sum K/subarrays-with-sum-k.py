#User function Template for python3
from collections import defaultdict
class Solution:
    def findSubArraySum(self, Arr, N, k):
        # code here
        sum=0
        c=0
        d=defaultdict(int)
        d[0]=1
        for i in range(len(Arr)):
            sum=sum+Arr[i]
            c+=d[sum-k]
            d[sum]+=1
        return c
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends