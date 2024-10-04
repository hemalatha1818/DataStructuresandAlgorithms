#User function Template for python3

class Solution:
    def bottomView(self, root):
        # code here
        def dfs(node, hd, depth, hd_map):
            if not node:
                return
            
            # If this is the first node at this HD, or if the node is deeper than the current one at this HD
            if hd not in hd_map or depth >= hd_map[hd][1]:
                hd_map[hd] = (node.data, depth)
            
            # Traverse the left subtree with HD - 1 and depth + 1
            dfs(node.left, hd - 1, depth + 1, hd_map)
            
            # Traverse the right subtree with HD + 1 and depth + 1
            dfs(node.right, hd + 1, depth + 1, hd_map)
    
    # Edge case: empty tree
        if not root:
            return
        
        # Dictionary to store the node's value and its depth for each horizontal distance (HD)
        hd_map = {}
        
        # Start DFS with root, HD = 0, and depth = 0
        dfs(root, 0, 0, hd_map)
        l=[]
        # Extract the bottom view by sorting based on horizontal distance (HD)
        for hd in sorted(hd_map):
            l.append(hd_map[hd][0])
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
#Contributed by Sudarshan Sharma
from collections import deque
from collections import defaultdict
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.bottomView(root)
        for i in res:
            print (i, end = " ")
        print()


# } Driver Code Ends