class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
      
        x=abs(sum(a)-sum(b))
        p=sum(a)
        q=sum(b)
        if x==0:
            return 1
        i=0
        j=0
        a.sort()
        b.sort()
        while(i<n and j<m):
            if(2*b[j]==q-p+2*a[i]):
                return 1
            elif(2*b[j]>q-p+2*a[i]):
                i=i+1
            else:
                j=j+1
        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends