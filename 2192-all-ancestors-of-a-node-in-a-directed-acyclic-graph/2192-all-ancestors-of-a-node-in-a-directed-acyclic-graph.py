#from collections import Counter

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        l = [set() for _ in range(n)]
        pf = [0] * n
        dd = collections.defaultdict(list)
        
        for i, j in edges:
            dd[i].append(j)
            pf[j] += 1
        q = deque()
        
        for i in range(len(pf)):
            if not pf[i]:
                q.append(i)
        while q:
            node = q.popleft()
            for k in dd[node]:
                l[k].update(l[node], [node])
                pf[k] -= 1
                if not pf[k]:
                    q.append(k)
            l[node] = sorted(l[node])
        
        return l
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
#         c = Counter([i[1] for i in edges])
#         res = []
#         edges = sorted(edges, key = lambda x:x[1])
#         idx = 0
        
#         for i in range(n):
#             temp = []
#             if c[i] == 0:
#                 res.append(temp)
#             else:
#                 temp.extend(list(set([k[0]]).union(set(res[k[0]]))) for k in edges[idx:idx+c[i]])
                
#                 if len(temp) == 1:
#                     res.extend(temp)
#                 else:
#                     l = len(temp)
#                     j = 0
#                     base = set()
                    
#                     while j<l:
#                         base = base.union(set(temp[j]))
#                         j += 1
                    
#                     res.append(list(base))
#                     #print(base)
#                     #print(res)
                    
#                     #print(temp)
#                     #print(list(set(temp[j]).union(set(temp[j+1])) for j in range(len(temp)-1)))
                
#                 idx = idx+c[i]
                
#         return res