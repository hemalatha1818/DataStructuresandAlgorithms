#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        s=set()
        arr.sort()
        l=[]
        if len(arr)<4:
            return l
        for i in range(len(arr)-3):
            if(i>0 and arr[i]==arr[i-1]):
                continue
            for j in range(i+1,len(arr)-2):
                if(j>i+1 and arr[j]==arr[j-1]):
                    continue
                p=j+1
                t=len(arr)-1
                while(p<t):
                  
                    sum=arr[i]+arr[j]
                    sum=sum+arr[p]+arr[t]
                    if sum==k:
                        l.append([arr[i],arr[j],arr[p],arr[t]])
                        p+=1
                        t-=1
                        while(p<t and arr[p]==arr[p-1]):
                            p+=1
                        while(p<t and arr[t]==arr[t+1]):
                            t-=1
                    elif sum>k:
                        t-=1
                    else:
                        p+=1
                        
        return l
                        
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends