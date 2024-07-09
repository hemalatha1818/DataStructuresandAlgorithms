# User function Template for python3

class Solution:
    def toh(self, n, fromm, to, aux):
        # Your code here
        if n==0:
            
            return 0
        self.c=0
        return self.solve(n, fromm, to, aux)
    def solve(self,n, fromm, to, aux):
        if n==1:
            print(
            'move disk {p} from rod {src} to rod {des}'.format(p=n,src=fromm,des=to))
            self.c+=1
            return 1
        
        self.solve(n-1, fromm, aux, to)
        self.c+=1
        print('move disk {p} from rod {src} to rod {des}'.format(p=n,src=fromm,des=to))
        
        self.solve(n-1, aux, to, fromm)
        return self.c
        
       



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends