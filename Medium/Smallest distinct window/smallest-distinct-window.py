#User function Template for python3

class Solution:
    def findSubString(self, str):
        l=len(set(str))
        d={}
        mini=99999
        j=0
        for i in range(len(str)):
            if len(d)<l:
                if str[i] in d:
                    d[str[i]]+=1
                else:
                    d[str[i]]=1
            elif len(d)>l:
                d[str[j]]-=1
                if d[str[j]]==0:
                    d.pop(str[j])
                j+=1
            while(len(d)==l):
                mini=min(mini,i-j+1)
                d[str[j]]-=1
                if d[str[j]]==0:
                    d.pop(str[j])
                j+=1
        return mini
        # Your code goes here
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	str = input()
    	ob=Solution()
    	print(ob.findSubString(str))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends