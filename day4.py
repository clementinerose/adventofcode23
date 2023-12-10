import numpy as np


def part1():
  with open("input4.txt") as file:
    sum = []
    Lines = file.readlines()
    for line in Lines:
      win = []
      guess = []
      i, counter = 0, 0
      while line[i] != ':':
        i += 1
      for j in range(10):
        if line[i + 2] != " ":
          win.append(int(str(line[i + 2]) + str(line[i + 3])))
        else:
          win.append(int(line[i + 3]))
        i += 3

      i += 4
      for j in range(25):
        if line[i] != " ":
          guess.append(int(str(line[i]) + str(line[i + 1])))
        else:
          guess.append(int(line[i + 1]))
        i += 3

      for k in range(len(win)):
        for j in range(len(guess)):
          if win[k] == guess[j]:
            counter = 1 if counter == 0 else counter * 2

      sum.append(counter)

    print(np.sum(sum))


def part2():
  with open("input4.txt") as file:
    reps = [1 for _ in range(206)]
    Lines = file.readlines()
    for m in range(len(Lines)):
      line = Lines[m]
      win = []
      guess = []
      i, counter = 0, 0
      while line[i] != ':':
        i += 1
      for j in range(10):
        if line[i + 2] != " ":
          win.append(int(str(line[i + 2]) + str(line[i + 3])))
        else:
          win.append(int(line[i + 3]))
        i += 3

      i += 4
      for j in range(25):
        if line[i] != " ":
          guess.append(int(str(line[i]) + str(line[i + 1])))
        else:
          guess.append(int(line[i + 1]))
        i += 3

      p = m
      for _ in range(reps[m]):
        p = m
        for k in range(len(win)):
          for j in range(len(guess)):
            if win[k] == guess[j]:
              reps[p+1] += 1
              p += 1
            
  print(np.sum(reps))

part2()