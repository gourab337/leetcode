class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        
        rank = [0]*n
        parent = [i for i in range(n)]
        def find(x):
            if x==parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
       
        def union(x,y):
            a = find(x)
            b = find(y)
            
            if(rank[a]>rank[b]):
                parent[b]=a
            elif(rank[b]>rank[a]):
                parent[a]=b
            else:
                parent[b]=a
                rank[a]+=1
        
        for edge in edges:
            union(*edge)
        
        return find(source)==find(dest)
