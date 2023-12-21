#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        # code here
        d={}
        maxi=0
        sum=0
        for i in range(len(arr)):
            if arr[i]==0:
                arr[i]=-1
        for i in range(len(arr)):
            sum=sum+arr[i]
            if sum==0:
                maxi=i+1
            elif sum in d:
                maxi=max(maxi,i-d[sum])
            else:
                d[sum]=i
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends