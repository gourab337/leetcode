"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}
        
        def dfs(node):
            #entry
            if node == None:
                return None
            if node in hashmap:
                return hashmap[node]
            copyNode = Node(node.val)
            hashmap[node] = copyNode
            #node processing
            for neighbor in node.neighbors:
                copyNeighbor = dfs(neighbor)
                copyNode.neighbors.append(copyNeighbor)
            #exit
            return copyNode
        
