elf = input().split()
c = int(elf[0])
for i in range(0,13) :
  if c <= int(elf[i+1]) :
      c = int(elf[i+1])
    

c += 1
if c <= int(elf[14]) :
  c = int(elf[14])


print(c)





