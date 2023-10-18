
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        s={}
        l=[]
        for i in range(K):
            if A[i] in s:
                s[A[i]]+=1
            else:
                s[A[i]]=1
        l.append(len(s))
        
        for i in range(K,len(A)):
            s[A[i-K]]-=1
            if s[A[i-K]]==0:
                s.pop(A[i-K])
            if A[i] in s:
                s[A[i]]+=1
            else:
                s[A[i]]=1
            
            
            l.append(len(s))
            
        return l
            


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends