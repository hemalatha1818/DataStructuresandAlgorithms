#User function Template for python3

class Solution:

    def getSubstringWithEqual012(self, Str):
        # code here
        
        count_of_0=0
        count_of_1=0
        count_of_2=0
        c=0
        x01=count_of_1-count_of_0
        x21=count_of_2-count_of_1
        k=x01,x21
        d={k:1}
        for i in range(len(Str)):
            if(Str[i]=="0"):
                count_of_0+=1
            elif(Str[i]=="1"):
                count_of_1+=1
            else:
                count_of_2+=1
            x01=count_of_1-count_of_0
            x21=count_of_2-count_of_1
            k=x01,x21
            if k in d:
                c+=d[k]
                d[k]+=1
                
            else:
                d[k]=1
        return c
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.getSubstringWithEqual012(Str))

# } Driver Code Ends