class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        hashmap = {}
        count = 0
        
        def rank(string):
            rank = (10000*ord(string[0]))+(100*ord(string[1]))+ord(string[2])-656565
            return rank
        
        for node in tickets:
            a = node[0]
            b = node[1]
            if a not in hashmap.values():
                hashmap[rank(a)] = a
            if b not in hashmap.values():
                hashmap[rank(b)] = b           
        print(len(hashmap))  
        def findkey(value):
            for itr in hashmap:
                if hashmap[itr] == value:
                    return itr
        #constructing graph
        graph = defaultdict(list)
        
        for ticket in tickets:
            graph[findkey(ticket[0])].append(findkey(ticket[1]))
        
        # print(graph)
        
        def dfs(curr_node):
            #entry
            while graph[curr_node]:
            #node_processing
                next_node = min(graph[curr_node])
                graph[curr_node].remove(next_node)
                dfs(next_node)
            #exit
            ans.append(curr_node)
            
         
        dfs(findkey("JFK"))
        new_ans = reversed(ans)
        path = []
        for i in new_ans:
            path.append(hashmap[i])
            
