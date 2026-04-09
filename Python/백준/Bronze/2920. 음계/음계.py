li = list(map(int, input().split()))

if li == sorted(li) :
  print('ascending')
elif li == list(reversed(sorted(li))) :
  print('descending')
else :
  print('mixed')