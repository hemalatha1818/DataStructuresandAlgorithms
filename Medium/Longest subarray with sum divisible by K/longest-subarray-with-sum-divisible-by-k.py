#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
		d={}
		c=0
		sum=0
		maxi=0
		for i in range(len(arr)):
		    sum+=arr[i]
		    if sum%K==0:
		        maxi=i+1
		    if sum%K in d:
		        maxi=max(maxi,i-d[sum%K])
		    else:
		        d[sum%K]=i
	    return maxi




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends