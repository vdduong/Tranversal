# walking through a connected component of a graph represented using adjacency sets
def walk(G,s,S=set()):  # walk the graph from s
  P, Q = dict(), set()  # predecessors + "to do" queue
  P[s] = None           # s hqs no predecessor
  Q.add(s)              # we plan on starting with s
  while Q:              # still nodes to visit
    u =Q.pop()          # pick one
    for v in G[u].difference(P,S):  # new nodes ?
      Q.add(v)          # we plan to visit them
      P[v]=u            # remember where we came from
  return P              # the traversal tree
  
# finding connected components
def components(G):      # the connected component
  comp = []   
  seen = set()          # nodes we've already seen
  for u in G:           # try every starting point
    if u in seen: continue  # seen ? ignore it
    C = walk(G,u)           # traverse problem
    seen.update(C)          # add keys of C to seen
    comp.append(C)          # collect the components
  return comp

# recursive tree-traversal
def tree_walk(T,r):   # traverse T from root r
  for u in T[r]:      # for each child
    tree_walk(T,u)    # traverse its sub tree

# recursive DFS
def rec_dfs(G,s,S=None):
  if S is None: S = set() # initialize the history
  S.add(s)                # we've visited s
  for u in G[s]:          # explore neighbors
    if u in S: continue   # already visited: skip
    rec_dfs(G,u,S)        # new: explore recursively

# iterative DFS
def iter_dfs(G,s):
  S,Q = set(),[]  # visited-set and queue
  Q.append(s)     # we plan on visiting s
  while Q:        # planned nodes left
    u = Q.pop()   # get one
    if u in S:continue  # already visited ? skip it
    S.add(u)      # we've visited it now
    Q.extend(G[u])  # schedule all neighbors
    yield u     # report u as visited

# a general graph traversal function
def traverse(G,s,qtype=set):
  S,Q = set(),qtype()
  Q.add(s)
  while Q:
    u = Q.pop()
    if u in S: continue
    S.add(u)
    for v in G[u]:
      Q.add(v)
    yield u

