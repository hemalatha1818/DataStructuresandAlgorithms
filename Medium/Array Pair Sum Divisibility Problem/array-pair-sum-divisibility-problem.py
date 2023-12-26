#User function Template for python3

class Solution:
	def canPair(self, nuns, k):
		# Code here
		d={}
		for i in nuns:
		    if i%k in d:
		        d[i%k]+=1
		    else:
		        d[i%k]=1
        for i in d:
            if i==0:
                if d[i]%2!=0:
                    return False
                    
            elif k-i not in d:
                return False
            elif d[i]!=d[k-i]:
                return False
        return True
		    
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends