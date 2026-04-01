c = input().split()
c_x = int(c[0])
c_y = int(c[1])

people = int(input())

for n in range(people) :
  point = input().split()
  point_x = int(point[0])
  point_y = int(point[1])
  if point_x == c_x or point_y == c_y :
    print("0")
  else:
    print("1")



