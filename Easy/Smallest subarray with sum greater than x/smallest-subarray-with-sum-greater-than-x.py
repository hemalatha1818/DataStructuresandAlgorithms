class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        i=0
        j=0
        mini=99999
        sum=0
        while(i<n):
            sum=sum+a[i]
            while(sum>x):
                sum=sum-a[j]
                mini=min(mini,i-j+1)
                j=j+1
            i+=1
        if mini==99999:
            return 0
        return mini


#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends