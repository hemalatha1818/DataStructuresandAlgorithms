#User function Template for python3

class Solution:
    def sumClosest(self, arr, x):
        # code here
        i=0
        j=len(arr)-1
        a,b=0,0
        mini=99999
        
        while(i<j):
            if i!=j and mini>min(mini,abs(x-(arr[i]+arr[j]))):
                mini=abs(x-(arr[i]+arr[j]))
                a,b=i,j

            elif arr[i]+arr[j]<x:
                i+=1
            elif arr[i]+arr[j]==x:
                return arr[i],arr[j]
            else:
                j-=1
            
        return arr[a],arr[b]
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumClosest(arr, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1
# } Driver Code Ends