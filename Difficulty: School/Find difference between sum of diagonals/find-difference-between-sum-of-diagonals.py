#User function Template for python3

class Solution:
    def diagonalSumDifference(self,N,Grid):
        #code here
        suma=0
        sumb=0
        for i in range(len(Grid)):
            for j in range(len(Grid[0])):
                if i==j:
                    suma+=Grid[i][j]
                elif i+j==len(Grid)-1:
                    sumb+=Grid[i][j]
                    
                if len(Grid)%2!=0 and i==len(Grid)//2 and j==len(Grid)//2:
                    sumb+=Grid[i][j]
        return abs(suma-sumb)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Grid = [[0 for i in range(N)] for j in range(N)]
        for i in range(N):
            s=list(map(int,input().strip().split(' ')))
            for j in range(N):
                Grid[i][j]=s[j]
        ob=Solution()
        print(ob.diagonalSumDifference(N,Grid))
# } Driver Code Ends