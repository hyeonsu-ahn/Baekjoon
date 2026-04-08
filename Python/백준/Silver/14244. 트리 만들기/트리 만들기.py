n,m = map(int,input().split())

leaf = 1
node = 0
branchpoint = 0
while node != n-1 :
  if node != 0 and leaf < m :
    if branchpoint == 0 :
      branchpoint = node
    print(branchpoint, leaf + 1)
    node += 1
    leaf += 1
  else :
    print(node, node +1)
    node += 1

    
  