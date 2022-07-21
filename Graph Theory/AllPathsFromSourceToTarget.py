class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        all_paths = []
        target = len(graph) - 1
   
        def dfs(node,path):
            #entry
            if(node == target):
                all_paths.append(list(path))
                return 
            #node processing
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor,path)
                path.pop()
            #exit (here exit is empty)
        
        path = deque([0])
        dfs(0,path)
        return all_paths
                
        
            
            
