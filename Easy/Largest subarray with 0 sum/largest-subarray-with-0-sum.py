#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        maxi=0
        sum=0
        d={}
        for i in range(len(arr)):
            sum=sum+arr[i]
            if sum==0:
                maxi=max(maxi,i+1)
            if sum in d:
                maxi=max(maxi,i-d[sum])
            else:
                d[sum]=i
        return maxi


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends