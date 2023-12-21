#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        c=0
        sum=0
        d={0:0}
        for i in range(0,len(arr)):
            if arr[i]==0:
                arr[i]=-1
            
        for i in range(0,len(arr)):
            sum+=arr[i]
            if sum==0 or sum in d:
                
                d[sum]+=1
                c+=d[sum]
                
            else:
                d[sum]=0
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends