#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        j=0
        i=0
        d={}
        maxi=-1
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
            while(j<=i and len(d)>k):
                if s[j] in d and d[s[j]]==1:
                    d.pop(s[j])
                else:
                    d[s[j]]-=1
                    
                j+=1
            if(len(d)==k):
                maxi=max(maxi,i-j+1)
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends