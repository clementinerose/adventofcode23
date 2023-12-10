time = [59688274]
distance = [543102016641022]
waystowin = [0]
sum = 1

for i in range(len(time)):   
  speed = list(range(1, time[i]))
  print(speed)
  for j in range(len(speed)):
    go  = (int(time[i]) - speed[j]) * speed[j]
    if go > distance[i]:
      waystowin[i] += 1
print(waystowin)
for l in range(len(waystowin)):
  sum = waystowin[l] * sum
      
print(sum)

#part 2 run on pc takes 5 min