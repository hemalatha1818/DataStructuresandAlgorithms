#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        sum=0
        for i in range(K):
            sum+=Arr[i]
        maxi=sum
        for i in range(K,N):
            sum=sum-Arr[i-K]+Arr[i]
            maxi=max(maxi,sum)
        return maxi
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends