from collections import defaultdict
class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    
    def frequencyCount(self, arr, N, P):
        # code here
        d=defaultdict(int)
        for i in arr:
            if d[i]!=0:
                d[i]+=1
            else:
                d[i]=1
    
        for i in range(1,len(arr)+1):
            arr[i-1]=d[i]
                                        
        return arr




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends