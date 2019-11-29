from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.adj_list=defaultdict(list)
        self.value=v
    def add(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def dfs(self,s,visited,stack):        
        visited[s]=1
        stack.append(s)
        print(stack)
        print(s)
        for x in self.adj_list[s]:
            if(visited[x]==1):
                continue
            else:
                #visited[x]=1
                #stack.append(x)
                self.dfs(x,visited,stack)
                
        stack.pop()
        
if __name__=='__main__':
    g=Graph(6)
    g.add(1,2)
    g.add(1,3)
    g.add(2,4)
    g.add(2,5)
    g.add(3,5)
    g.add(4,5)
    g.add(4,6)
    g.add(5,6)
    visited=[0 for i in range(7)]
    stack=[]
    g.dfs(1,visited,stack)
    
    #g.printAllPaths(1,5)
    

        
